#!/usr/bin/env python3
"""Private podcast feeds: script text -> TTS MP3 -> feed.xml -> git commit/push.

Usage (add --show NAME before the command for a show other than the root one):
  pod publish SCRIPT --title "Title" [--style s] [--description ..] [--slug s]
                     [--season N] [--episode N] [--no-push]
  pod replace SLUG SCRIPT [--title ..] [--style ..] [--description ..] [--no-push]
  pod remove SLUG [--no-push]
  pod list | feed
  pod preview SCRIPT [--style ..] [-o out.mp3]     # audio only, nothing published
  pod check SCRIPT                                  # includes + readability, no audio
  pod new-show NAME --title "Title" [--description ..] [--serial]

Shows: the root folder is the default show ("Learning Sessions"). Any other show lives
in its own folder (e.g. aristotle/) with its own podcast.json, feed.xml, episodes/.

Script format (plain text / light markdown):
  - Blank line between paragraphs  -> paragraph pause
  - "# Heading"                    -> spoken, then a section pause
  - "> quoted block"               -> read by the style's quote voice (the original text)
  - {{read 3-5}}                   -> paragraphs 3..5 of `chapter` from `source`
                                      (front matter), inserted verbatim as a quote block
  - [pause] or [pause 3]           -> explicit silence (seconds; default 2)
  - "---"                          -> section break
"""
from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import email.utils
import json
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path
from xml.sax.saxutils import escape

import edge_tts

ROOT = Path(__file__).resolve().parent
STYLES_DIR = ROOT / "styles"

DEFAULT_STYLE = {
    "voice": "en-US-AndrewNeural",
    "rate": "-5%",
    "pitch": "+0Hz",
    "quote_voice": "",        # empty = same as voice
    "quote_rate": "",
    "quote_pitch": "",
    "paragraph_pause": 1.2,
    "section_pause": 2.5,
    "switch_pause": 1.6,      # pause when switching between host and quote voice
    "intro_pause": 1.0,
    "outro_pause": 2.0,
}
BITRATE = "64k"  # mono speech; ~0.5 MB per minute


class Show:
    def __init__(self, name: str | None):
        self.name = name or ""
        self.dir = ROOT / name if name else ROOT
        if name and not self.dir.is_dir():
            sys.exit(f"No show folder '{name}'. Create it with: pod new-show {name} --title ...")
        self.config_path = self.dir / "podcast.json"
        self.episodes_path = self.dir / "episodes.json"
        self.feed_path = self.dir / "feed.xml"
        self.audio_dir = self.dir / "episodes"
        self.scripts_dir = self.dir / "scripts"

    def config(self) -> dict:
        if not self.config_path.exists():
            sys.exit(f"{self.config_path} missing.")
        cfg = json.loads(self.config_path.read_text())
        cfg["base_url"] = cfg["base_url"].rstrip("/")
        return cfg

    def episodes(self) -> list[dict]:
        return load_json(self.episodes_path, [])

    def save_episodes(self, eps: list[dict]) -> None:
        save_json(self.episodes_path, eps)


# ---------------------------------------------------------------- helpers

def load_json(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[m.end():]


def load_style(name: str | None) -> dict:
    """styles/<name>.md: front matter = voice settings, body = writing guide."""
    style = dict(DEFAULT_STYLE)
    style["name"] = name or "default"
    if name:
        path = STYLES_DIR / f"{name}.md"
        if not path.exists():
            avail = ", ".join(p.stem for p in STYLES_DIR.glob("*.md"))
            sys.exit(f"Unknown style '{name}'. Available: {avail}")
        meta, _ = front_matter(path.read_text())
        for k, v in meta.items():
            if k in DEFAULT_STYLE:
                style[k] = float(v) if isinstance(DEFAULT_STYLE[k], float) else v
    for k in ("voice", "rate", "pitch"):
        style[f"quote_{k}"] = style[f"quote_{k}"] or style[k]
    return style


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60] or "episode"


# ---------------------------------------------------------------- sources / includes

def load_source_chapters(path: Path) -> dict[int, dict]:
    """Split a source text into chapters on lines like 'Chapter 3: Title'.
    Paragraphs are separated by blank lines."""
    chapters: dict[int, dict] = {}
    cur = None
    for block in re.split(r"\n\s*\n", path.read_text().strip()):
        block = block.strip()
        m = re.match(r"^Chapter\s+(\d+)\s*:\s*(.+?)\s*$", block.split("\n")[0])
        if m:
            cur = int(m.group(1))
            chapters[cur] = {"title": m.group(2), "paras": []}
            rest = block.split("\n", 1)[1].strip() if "\n" in block else ""
            if rest:
                chapters[cur]["paras"].append(rest)
        elif cur is not None:
            chapters[cur]["paras"].append(block)
    return chapters


READ_RE = re.compile(r"^\{\{read[ \t]+(\d+)(?:[ \t]*-[ \t]*(\d+))?\}\}[ \t]*$", re.M)


def expand_includes(text: str, script_path: Path | None, strict: bool = True) -> tuple[str, dict]:
    """Replace {{read a-b}} with verbatim quoted paragraphs. Returns (text, info)."""
    meta, body = front_matter(text)
    info: dict = {"meta": meta}
    if not READ_RE.search(body):
        return body, info
    if "source" not in meta or "chapter" not in meta:
        sys.exit("Script uses {{read}} but front matter lacks `source:` and `chapter:`.")
    src = (ROOT / meta["source"]).resolve()
    chapter = int(meta["chapter"])
    chapters = load_source_chapters(src)
    if chapter not in chapters:
        sys.exit(f"Chapter {chapter} not found in {src}")
    paras = chapters[chapter]["paras"]
    used: list[int] = []

    def sub(m):
        a = int(m.group(1))
        b = int(m.group(2) or a)
        if not (1 <= a <= b <= len(paras)):
            sys.exit(f"{{{{read {a}-{b}}}}} out of range (chapter {chapter} has {len(paras)} paragraphs)")
        used.extend(range(a, b + 1))
        return "\n\n".join("\n".join("> " + ln for ln in paras[i - 1].split("\n")) for i in range(a, b + 1))

    body = READ_RE.sub(sub, body)
    missing = sorted(set(range(1, len(paras) + 1)) - set(used))
    dupes = sorted({i for i in used if used.count(i) > 1})
    out_of_order = used != sorted(used)
    info.update(chapter=chapter, chapter_title=chapters[chapter]["title"], n_paras=len(paras),
                missing=missing, dupes=dupes, out_of_order=out_of_order)
    if strict and (missing or dupes or out_of_order):
        sys.exit(f"Source not intact in {script_path}: missing={missing} duplicated={dupes} "
                 f"out_of_order={out_of_order}")
    return body, info


# ---------------------------------------------------------------- script parsing

PAUSE_RE = re.compile(r"\[pause(?:\s+([\d.]+)s?)?\]", re.I)


def clean_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)[*_](.+?)[*_](?!\w)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)      # links
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)      # bullets
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)          # quote markers
    text = text.replace("[", "").replace("]", "")             # editorial brackets
    return re.sub(r"\s+", " ", text).strip()


def parse_script(body: str, style: dict) -> list[tuple]:
    """Segments: ("speech", text, "host"|"quote") or ("pause", seconds)."""
    segs: list[tuple] = []
    for block in re.split(r"\n\s*\n", body.strip()):
        block = block.strip()
        if not block:
            continue
        if re.fullmatch(r"-{3,}|\*{3,}", block):
            segs.append(("pause", style["section_pause"]))
            continue
        is_quote = all(ln.lstrip().startswith(">") for ln in block.splitlines() if ln.strip())
        who = "quote" if is_quote else "host"
        heading = block.startswith("#")
        if heading:
            block = block.lstrip("#").strip()
        pos = 0
        for m in PAUSE_RE.finditer(block):
            chunk = clean_markdown(block[pos:m.start()])
            if chunk:
                segs.append(("speech", chunk, who))
            segs.append(("pause", float(m.group(1) or 2)))
            pos = m.end()
        chunk = clean_markdown(block[pos:])
        if chunk:
            segs.append(("speech", chunk, who))
        segs.append(("pause", style["section_pause"] if heading else style["paragraph_pause"]))

    # longer pause whenever the speaker changes
    out: list[tuple] = []
    last_who = None
    for s in segs:
        if s[0] == "speech":
            if last_who and s[2] != last_who:
                out.append(("pause", style["switch_pause"]))
            last_who = s[2]
        out.append(s)
    merged: list[tuple] = []
    for s in out:
        if s[0] == "pause" and merged and merged[-1][0] == "pause":
            merged[-1] = ("pause", max(merged[-1][1], s[1]))
        else:
            merged.append(s)
    while merged and merged[-1][0] == "pause":
        merged.pop()
    return merged


def readability(segs: list[tuple]) -> dict:
    import textstat
    res = {}
    for who in ("host", "quote"):
        text = " ".join(s[1] for s in segs if s[0] == "speech" and s[2] == who)
        if text:
            res[who] = {"words": len(text.split()), "fre": round(textstat.flesch_reading_ease(text), 1)}
    return res


# ---------------------------------------------------------------- audio

def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Command failed: {' '.join(cmd)}\n{r.stderr[-2000:]}")
    return r.stdout


async def tts(text: str, out: Path, voice: str, rate: str, pitch: str, retries: int = 4) -> None:
    for attempt in range(retries):
        try:
            await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(str(out))
            if out.exists() and out.stat().st_size > 0:
                return
        except Exception as e:  # network hiccups
            if attempt == retries - 1:
                raise
            print(f"  tts retry ({e})", file=sys.stderr)
        await asyncio.sleep(2 * (attempt + 1))
    sys.exit(f"TTS produced no audio for: {text[:80]}")


def silence(seconds: float, dst: Path) -> None:
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
         "-t", f"{seconds:.2f}", "-c:a", "pcm_s16le", str(dst)])


def render_audio(body: str, style: dict, out_mp3: Path, title: str, author: str) -> None:
    segs = parse_script(body, style)
    if not any(s[0] == "speech" for s in segs):
        sys.exit("Script has no speakable text.")
    segs = [("pause", style["intro_pause"])] + segs + [("pause", style["outro_pause"])]
    n_speech = sum(1 for s in segs if s[0] == "speech")
    print(f"Rendering {n_speech} segments (host {style['voice']}, quote {style['quote_voice']})...")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        wavs: list[Path] = []
        spoken = 0
        for i, s in enumerate(segs):
            wav = td / f"{i:04d}.wav"
            if s[0] == "pause":
                if s[1] > 0:
                    silence(s[1], wav)
                    wavs.append(wav)
                continue
            _, text, who = s
            p = "quote_" if who == "quote" else ""
            mp3 = td / f"{i:04d}.mp3"
            asyncio.run(tts(text, mp3, style[p + "voice"], style[p + "rate"], style[p + "pitch"]))
            run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3), "-ar", "24000", "-ac", "1",
                 "-c:a", "pcm_s16le", str(wav)])
            wavs.append(wav)
            spoken += 1
            if spoken % 10 == 0 or spoken == n_speech:
                print(f"  {spoken}/{n_speech}")
        listfile = td / "list.txt"
        listfile.write_text("".join(f"file '{w}'\n" for w in wavs))
        out_mp3.parent.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listfile),
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", BITRATE,
             "-id3v2_version", "3", "-metadata", f"title={title}", "-metadata", f"artist={author}",
             str(out_mp3)])


def duration_seconds(path: Path) -> int:
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)])
    return int(round(float(out.strip())))


def hms(sec: int) -> str:
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


# ---------------------------------------------------------------- feed

def build_feed(show: Show) -> None:
    cfg, episodes = show.config(), show.episodes()
    base = cfg["base_url"]
    serial = cfg.get("type") == "serial"
    now = email.utils.format_datetime(dt.datetime.now(dt.timezone.utc))

    def order(e):
        return (e.get("season") or 0, e.get("episode") or 0, e["published"])

    items = []
    for ep in sorted(episodes, key=order, reverse=True):
        pub = email.utils.format_datetime(dt.datetime.fromisoformat(ep["published"]))
        url = f"{base}/episodes/{ep['file']}"
        desc = ep.get("description") or ep["title"]
        extra = ""
        if ep.get("season"):
            extra += f"\n      <itunes:season>{ep['season']}</itunes:season>"
        if ep.get("episode"):
            extra += f"\n      <itunes:episode>{ep['episode']}</itunes:episode>"
        items.append(f"""    <item>
      <title>{escape(ep['title'])}</title>
      <description>{escape(desc)}</description>
      <itunes:summary>{escape(desc)}</itunes:summary>
      <enclosure url="{escape(url)}" length="{ep['bytes']}" type="audio/mpeg"/>
      <link>{escape(base)}/</link>
      <guid isPermaLink="false">{escape(ep['guid'])}</guid>
      <pubDate>{pub}</pubDate>
      <itunes:duration>{ep['duration']}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>{extra}
      <itunes:explicit>false</itunes:explicit>
    </item>""")
    image = f"{base}/{cfg.get('image', 'cover.jpg')}"
    # itunes:block makes Apple refuse "Follow a Show by URL", so it's opt-in only
    block = "    <itunes:block>Yes</itunes:block>\n" if cfg.get("itunes_block") else ""
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(cfg['title'])}</title>
    <link>{escape(base)}/</link>
    <atom:link href="{escape(base)}/feed.xml" rel="self" type="application/rss+xml"/>
    <description>{escape(cfg.get('description', cfg['title']))}</description>
    <language>{cfg.get('language', 'en-us')}</language>
    <lastBuildDate>{now}</lastBuildDate>
    <itunes:author>{escape(cfg.get('author', ''))}</itunes:author>
    <itunes:owner><itunes:name>{escape(cfg.get('author', ''))}</itunes:name></itunes:owner>
    <itunes:image href="{escape(image)}"/>
    <image><url>{escape(image)}</url><title>{escape(cfg['title'])}</title><link>{escape(base)}/</link></image>
    <itunes:category text="{escape(cfg.get('category', 'Education'))}"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>{'serial' if serial else 'episodic'}</itunes:type>
{block}{chr(10).join(items)}
  </channel>
</rss>
"""
    show.feed_path.write_text(feed)
    rows = "".join(f"<li>{escape(e['title'])} <small>({e['duration']})</small></li>"
                   for e in sorted(episodes, key=order, reverse=not serial))
    (show.dir / "index.html").write_text(
        f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width'>"
        f"<meta name=robots content=noindex><title>{escape(cfg['title'])}</title>"
        f"<body style='font-family:system-ui;max-width:40em;margin:2em auto;padding:0 1em'>"
        f"<h1>{escape(cfg['title'])}</h1><p>Feed: <a href='feed.xml'>{escape(base)}/feed.xml</a></p>"
        f"<ul>{rows}</ul></body>\n")
    print(f"{show.feed_path.relative_to(ROOT)} updated ({len(episodes)} episodes)")


# ---------------------------------------------------------------- git

def git_commit_push(message: str, push: bool) -> None:
    if not (ROOT / ".git").exists():
        print("(not a git repo yet; skipping commit)")
        return
    subprocess.run(["git", "-C", str(ROOT), "add", "-A"], check=True)
    if subprocess.run(["git", "-C", str(ROOT), "diff", "--cached", "--quiet"]).returncode == 0:
        print("Nothing to commit.")
        return
    subprocess.run(["git", "-C", str(ROOT), "commit", "-q", "-m", message], check=True)
    print(f"Committed: {message}")
    if push:
        subprocess.run(["git", "-C", str(ROOT), "push", "-q"], check=True)
        print("Pushed. GitHub Pages usually refreshes within a minute or two.")


# ---------------------------------------------------------------- commands

def prepare(script_path: Path) -> tuple[str, dict]:
    return expand_includes(script_path.read_text(), script_path)


def make_episode(show: Show, script_path: Path, slug: str, title: str, style_name: str | None,
                 description: str | None, existing: dict | None, season, episode) -> dict:
    cfg = show.config()
    body, info = prepare(script_path)
    style_name = style_name or info["meta"].get("style")
    style = load_style(style_name)
    version = (existing.get("version", 1) + 1) if existing else 1
    filename = f"{slug}.mp3" if version == 1 else f"{slug}-v{version}.mp3"
    out = show.audio_dir / filename
    render_audio(body, style, out, title, cfg.get("author", ""))

    # keep a copy of the script with the show, unless it already lives there
    show.scripts_dir.mkdir(exist_ok=True)
    if script_path.resolve().parent != show.scripts_dir.resolve():
        shutil.copyfile(script_path, show.scripts_dir / f"{slug}.md")
    if existing and existing["file"] != filename:
        (show.audio_dir / existing["file"]).unlink(missing_ok=True)

    sec = duration_seconds(out)
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    ep = {
        "slug": slug,
        "title": title,
        "description": description or (existing or {}).get("description") or info["meta"].get("description", ""),
        "style": style["name"],
        "file": filename,
        "bytes": out.stat().st_size,
        "duration": hms(sec),
        "guid": existing["guid"] if existing else str(uuid.uuid4()),
        "published": existing["published"] if existing else now,
        "version": version,
    }
    for k, v in (("season", season), ("episode", episode)):
        v = v if v is not None else (existing or {}).get(k) or info["meta"].get(k)
        if v:
            ep[k] = int(v)
    if existing:
        ep["updated"] = now
    print(f"{out.relative_to(ROOT)}: {hms(sec)}, {ep['bytes'] / 1e6:.1f} MB")
    return ep


def cmd_publish(a, show: Show) -> None:
    eps = show.episodes()
    meta, _ = front_matter(Path(a.script).read_text())
    title = a.title or meta.get("title") or sys.exit("--title required (or `title:` in front matter)")
    slug = a.slug or meta.get("slug") or slugify(title)
    if any(e["slug"] == slug for e in eps):
        sys.exit(f"Episode '{slug}' already exists. Use: pod {'--show ' + show.name + ' ' if show.name else ''}replace {slug} SCRIPT")
    ep = make_episode(show, Path(a.script), slug, title, a.style, a.description, None, a.season, a.episode)
    eps.append(ep)
    show.save_episodes(eps)
    build_feed(show)
    git_commit_push(f"Add episode: {title}", not a.no_push)


def cmd_replace(a, show: Show) -> None:
    eps = show.episodes()
    idx = next((i for i, e in enumerate(eps) if e["slug"] == a.slug), None)
    if idx is None:
        sys.exit(f"No episode '{a.slug}'. Existing: {', '.join(e['slug'] for e in eps)}")
    old = eps[idx]
    meta, _ = front_matter(Path(a.script).read_text())
    style = a.style or meta.get("style") or (old["style"] if old["style"] != "default" else None)
    title = a.title or meta.get("title") or old["title"]
    ep = make_episode(show, Path(a.script), a.slug, title, style, a.description, old, None, None)
    eps[idx] = ep
    show.save_episodes(eps)
    build_feed(show)
    git_commit_push(f"Replace episode: {ep['title']} (v{ep['version']})", not a.no_push)


def cmd_remove(a, show: Show) -> None:
    eps = show.episodes()
    ep = next((e for e in eps if e["slug"] == a.slug), None)
    if not ep:
        sys.exit(f"No episode '{a.slug}'.")
    (show.audio_dir / ep["file"]).unlink(missing_ok=True)
    show.save_episodes([e for e in eps if e["slug"] != a.slug])
    build_feed(show)
    git_commit_push(f"Remove episode: {ep['title']}", not a.no_push)


def cmd_list(a, show: Show) -> None:
    for e in sorted(show.episodes(), key=lambda e: (e.get("season") or 0, e.get("episode") or 0, e["published"])):
        num = f"S{e['season']}E{e['episode']:02d}" if e.get("season") and e.get("episode") else "      "
        print(f"{num} {e['slug']:<44} {e['duration']:>8}  v{e.get('version', 1)}  {e['title']}")


def cmd_feed(a, show: Show) -> None:
    build_feed(show)


def cmd_check(a, show: Show) -> None:
    ok = True
    for sp in a.scripts:
        body, info = expand_includes(Path(sp).read_text(), Path(sp), strict=False)
        style = load_style(a.style or info["meta"].get("style"))
        r = readability(parse_script(body, style))
        intact = not (info.get("missing") or info.get("dupes") or info.get("out_of_order"))
        ok &= intact
        src = (f"source ch{info['chapter']}: {info['n_paras']} paras, "
               f"{'INTACT' if intact else 'NOT INTACT missing=%s dupes=%s order=%s' % (info['missing'], info['dupes'], info['out_of_order'])}"
               if "chapter" in info else "no source includes")
        rd = "  ".join(f"{w}: {v['words']} words, FRE {v['fre']}" for w, v in r.items())
        print(f"{Path(sp).name}: {src} | {rd}")
    if not ok:
        sys.exit(1)


def cmd_preview(a, show: Show) -> None:
    body, info = prepare(Path(a.script))
    style = load_style(a.style or info["meta"].get("style"))
    out = Path(a.output)
    render_audio(body, style, out, out.stem, "")
    print(f"{out}: {hms(duration_seconds(out))}")


def cmd_new_show(a, _show: Show) -> None:
    d = ROOT / a.name
    if (d / "podcast.json").exists():
        sys.exit(f"Show '{a.name}' already exists.")
    root_cfg = json.loads((ROOT / "podcast.json").read_text())
    d.mkdir(exist_ok=True)
    cfg = {
        "title": a.title,
        "description": a.description or a.title,
        "author": root_cfg.get("author", ""),
        "base_url": f"{root_cfg['base_url'].rstrip('/')}/{a.name}",
        "language": root_cfg.get("language", "en-us"),
        "category": root_cfg.get("category", "Education"),
        "image": "cover.jpg",
        "type": "serial" if a.serial else "episodic",
    }
    save_json(d / "podcast.json", cfg)
    save_json(d / "episodes.json", [])
    print(f"Created {a.name}/podcast.json. Make a cover: .venv/bin/python make_cover.py {a.name}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--show", help="show folder name (default: root show)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("publish")
    s.add_argument("script")
    s.add_argument("--title")
    s.add_argument("--style")
    s.add_argument("--description")
    s.add_argument("--slug")
    s.add_argument("--season", type=int)
    s.add_argument("--episode", type=int)
    s.add_argument("--no-push", action="store_true")
    s.set_defaults(func=cmd_publish)

    s = sub.add_parser("replace")
    s.add_argument("slug")
    s.add_argument("script")
    s.add_argument("--title")
    s.add_argument("--style")
    s.add_argument("--description")
    s.add_argument("--no-push", action="store_true")
    s.set_defaults(func=cmd_replace)

    s = sub.add_parser("remove")
    s.add_argument("slug")
    s.add_argument("--no-push", action="store_true")
    s.set_defaults(func=cmd_remove)

    sub.add_parser("list").set_defaults(func=cmd_list)
    sub.add_parser("feed").set_defaults(func=cmd_feed)

    s = sub.add_parser("check")
    s.add_argument("scripts", nargs="+")
    s.add_argument("--style")
    s.set_defaults(func=cmd_check)

    s = sub.add_parser("preview")
    s.add_argument("script")
    s.add_argument("--style")
    s.add_argument("-o", "--output", default="preview.mp3")
    s.set_defaults(func=cmd_preview)

    s = sub.add_parser("new-show")
    s.add_argument("name")
    s.add_argument("--title", required=True)
    s.add_argument("--description")
    s.add_argument("--serial", action="store_true", help="episodes meant to be heard in order")
    s.set_defaults(func=cmd_new_show)

    a = p.parse_args()
    show = Show(a.show) if a.cmd != "new-show" else None
    a.func(a, show)


if __name__ == "__main__":
    main()
