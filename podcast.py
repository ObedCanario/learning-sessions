#!/usr/bin/env python3
"""Private podcast feed builder: script text -> TTS MP3 -> feed.xml -> git commit/push.

Usage:
  podcast.py publish SCRIPT --title "Title" [--style jim-rohn] [--description ".."] [--slug s] [--no-push]
  podcast.py replace SLUG SCRIPT [--title ..] [--style ..] [--description ..] [--no-push]
  podcast.py remove SLUG [--no-push]
  podcast.py list
  podcast.py feed            # rebuild feed.xml from episodes.json only
  podcast.py preview SCRIPT [--style ..] [-o out.mp3]   # render audio only, no feed/git

Script format (plain text / light markdown):
  - Blank line between paragraphs  -> paragraph pause (style setting)
  - "# Heading" lines              -> spoken, followed by a longer section pause
  - [pause] or [pause 3]           -> explicit silence (seconds; default 2)
  - "---"                          -> section break (section pause)
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
CONFIG = ROOT / "podcast.json"
EPISODES = ROOT / "episodes.json"
FEED = ROOT / "feed.xml"
AUDIO_DIR = ROOT / "episodes"
SCRIPTS_DIR = ROOT / "scripts"
STYLES_DIR = ROOT / "styles"

DEFAULT_STYLE = {
    "voice": "en-US-AndrewNeural",
    "rate": "-5%",
    "pitch": "+0Hz",
    "paragraph_pause": 1.2,
    "section_pause": 2.5,
    "sentence_pause": 0.0,
    "intro_pause": 1.0,
    "outro_pause": 2.0,
}


# ---------------------------------------------------------------- config / data

def load_json(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def load_config() -> dict:
    if not CONFIG.exists():
        sys.exit("podcast.json missing. Copy podcast.example.json and fill it in.")
    cfg = json.loads(CONFIG.read_text())
    cfg["base_url"] = cfg["base_url"].rstrip("/")
    return cfg


def load_style(name: str | None) -> dict:
    """Styles live in styles/<name>.md. Front matter (between --- lines) holds
    voice settings as `key: value`; the body is the writing guide used when
    turning raw text into a script in that style."""
    style = dict(DEFAULT_STYLE)
    style["name"] = name or "default"
    if not name:
        return style
    path = STYLES_DIR / f"{name}.md"
    if not path.exists():
        avail = ", ".join(p.stem for p in STYLES_DIR.glob("*.md"))
        sys.exit(f"Unknown style '{name}'. Available: {avail}")
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.strip().startswith("#"):
                k, v = line.split(":", 1)
                k, v = k.strip(), v.strip().strip('"')
                if k in DEFAULT_STYLE and isinstance(DEFAULT_STYLE[k], float):
                    v = float(v)
                style[k] = v
    return style


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60] or "episode"


# ---------------------------------------------------------------- script parsing

PAUSE_RE = re.compile(r"\[pause(?:\s+([\d.]+)s?)?\]", re.I)


def clean_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)[*_](.+?)[*_](?!\w)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)      # bullets
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)          # quotes
    return re.sub(r"\s+", " ", text).strip()


def parse_script(text: str, style: dict) -> list[tuple[str, float]]:
    """Return a list of segments: ("speech", text) or ("pause", seconds)."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)  # drop front matter
    segs: list[tuple[str, object]] = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if re.fullmatch(r"-{3,}|\*{3,}", block):
            segs.append(("pause", style["section_pause"]))
            continue
        heading = block.startswith("#")
        if heading:
            block = block.lstrip("#").strip()
        # split on explicit pause markers inside the block
        pos = 0
        for m in PAUSE_RE.finditer(block):
            chunk = clean_markdown(block[pos:m.start()])
            if chunk:
                segs.append(("speech", chunk))
            segs.append(("pause", float(m.group(1) or 2)))
            pos = m.end()
        chunk = clean_markdown(block[pos:])
        if chunk:
            segs.append(("speech", chunk))
        segs.append(("pause", style["section_pause"] if heading else style["paragraph_pause"]))
    # merge consecutive pauses (take the longest)
    merged: list[tuple[str, object]] = []
    for kind, val in segs:
        if kind == "pause" and merged and merged[-1][0] == "pause":
            merged[-1] = ("pause", max(merged[-1][1], val))
        else:
            merged.append((kind, val))
    while merged and merged[-1][0] == "pause":
        merged.pop()
    return merged


# ---------------------------------------------------------------- audio

def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Command failed: {' '.join(cmd)}\n{r.stderr[-2000:]}")
    return r.stdout


async def tts(text: str, out: Path, style: dict, retries: int = 3) -> None:
    for attempt in range(retries):
        try:
            comm = edge_tts.Communicate(text, style["voice"], rate=style["rate"], pitch=style["pitch"])
            await comm.save(str(out))
            if out.exists() and out.stat().st_size > 0:
                return
        except Exception as e:  # network hiccups
            if attempt == retries - 1:
                raise
            print(f"  tts retry ({e})", file=sys.stderr)
        await asyncio.sleep(2 * (attempt + 1))


def to_wav(src: Path, dst: Path) -> None:
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-ar", "44100", "-ac", "1", str(dst)])


def silence(seconds: float, dst: Path) -> None:
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
         "-t", f"{seconds:.2f}", str(dst)])


def render_audio(script_text: str, style: dict, out_mp3: Path, title: str, author: str) -> None:
    segs = parse_script(script_text, style)
    if not any(k == "speech" for k, _ in segs):
        sys.exit("Script has no speakable text.")
    segs = [("pause", style["intro_pause"])] + segs + [("pause", style["outro_pause"])]
    n_speech = sum(1 for k, _ in segs if k == "speech")
    print(f"Rendering {n_speech} spoken segments with {style['voice']} (rate {style['rate']})...")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        wavs: list[Path] = []
        i = spoken = 0
        for kind, val in segs:
            i += 1
            wav = td / f"{i:04d}.wav"
            if kind == "pause":
                if val > 0:
                    silence(val, wav)
                    wavs.append(wav)
            else:
                mp3 = td / f"{i:04d}.mp3"
                asyncio.run(tts(val, mp3, style))
                to_wav(mp3, wav)
                wavs.append(wav)
                spoken += 1
                print(f"  [{spoken}/{n_speech}] {val[:70]}{'...' if len(val) > 70 else ''}")
        listfile = td / "list.txt"
        listfile.write_text("".join(f"file '{w}'\n" for w in wavs))
        out_mp3.parent.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listfile),
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "96k",
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

def build_feed(cfg: dict, episodes: list[dict]) -> None:
    base = cfg["base_url"]
    now = email.utils.format_datetime(dt.datetime.now(dt.timezone.utc))
    items = []
    for ep in sorted(episodes, key=lambda e: e["published"], reverse=True):
        pub = email.utils.format_datetime(dt.datetime.fromisoformat(ep["published"]))
        url = f"{base}/episodes/{ep['file']}"
        desc = ep.get("description") or ep["title"]
        items.append(f"""    <item>
      <title>{escape(ep['title'])}</title>
      <description>{escape(desc)}</description>
      <itunes:summary>{escape(desc)}</itunes:summary>
      <enclosure url="{escape(url)}" length="{ep['bytes']}" type="audio/mpeg"/>
      <guid isPermaLink="false">{escape(ep['guid'])}</guid>
      <pubDate>{pub}</pubDate>
      <itunes:duration>{ep['duration']}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
    image = f"{base}/{cfg.get('image', 'cover.jpg')}"
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
    <itunes:image href="{escape(image)}"/>
    <image><url>{escape(image)}</url><title>{escape(cfg['title'])}</title><link>{escape(base)}/</link></image>
    <itunes:category text="{escape(cfg.get('category', 'Education'))}"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>episodic</itunes:type>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""
    FEED.write_text(feed)
    print(f"feed.xml updated ({len(episodes)} episodes)")


# ---------------------------------------------------------------- git

def git_commit_push(message: str, push: bool) -> None:
    if not (ROOT / ".git").exists():
        print("(not a git repo yet; skipping commit)")
        return
    subprocess.run(["git", "-C", str(ROOT), "add", "-A"], check=True)
    r = subprocess.run(["git", "-C", str(ROOT), "diff", "--cached", "--quiet"])
    if r.returncode == 0:
        print("Nothing to commit.")
        return
    subprocess.run(["git", "-C", str(ROOT), "commit", "-q", "-m", message], check=True)
    print(f"Committed: {message}")
    if push:
        subprocess.run(["git", "-C", str(ROOT), "push", "-q"], check=True)
        print("Pushed. GitHub Pages usually refreshes within a minute or two.")


# ---------------------------------------------------------------- commands

def make_episode(script_path: Path, slug: str, title: str, style_name: str | None,
                 description: str | None, existing: dict | None, cfg: dict) -> dict:
    style = load_style(style_name)
    text = script_path.read_text()
    version = (existing.get("version", 1) + 1) if existing else 1
    # versioned filename so Apple Podcasts re-downloads a replaced episode
    filename = f"{slug}.mp3" if version == 1 else f"{slug}-v{version}.mp3"
    out = AUDIO_DIR / filename
    render_audio(text, style, out, title, cfg.get("author", ""))

    SCRIPTS_DIR.mkdir(exist_ok=True)
    saved_script = SCRIPTS_DIR / f"{slug}.md"
    if script_path.resolve() != saved_script.resolve():
        shutil.copyfile(script_path, saved_script)

    if existing and existing["file"] != filename:
        old = AUDIO_DIR / existing["file"]
        if old.exists():
            old.unlink()

    sec = duration_seconds(out)
    ep = {
        "slug": slug,
        "title": title,
        "description": description or (existing or {}).get("description") or "",
        "style": style["name"],
        "file": filename,
        "bytes": out.stat().st_size,
        "duration": hms(sec),
        "guid": existing["guid"] if existing else str(uuid.uuid4()),
        "published": existing["published"] if existing
        else dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "version": version,
    }
    if existing:
        ep["updated"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    print(f"{out.relative_to(ROOT)}: {hms(sec)}, {ep['bytes'] / 1e6:.1f} MB")
    return ep


def cmd_publish(a) -> None:
    cfg = load_config()
    eps = load_json(EPISODES, [])
    slug = a.slug or slugify(a.title)
    if any(e["slug"] == slug for e in eps):
        sys.exit(f"Episode '{slug}' already exists. Use: podcast.py replace {slug} SCRIPT")
    ep = make_episode(Path(a.script), slug, a.title, a.style, a.description, None, cfg)
    eps.append(ep)
    save_json(EPISODES, eps)
    build_feed(cfg, eps)
    git_commit_push(f"Add episode: {a.title}", not a.no_push)


def cmd_replace(a) -> None:
    cfg = load_config()
    eps = load_json(EPISODES, [])
    idx = next((i for i, e in enumerate(eps) if e["slug"] == a.slug), None)
    if idx is None:
        sys.exit(f"No episode '{a.slug}'. Existing: {', '.join(e['slug'] for e in eps)}")
    old = eps[idx]
    style = a.style or (old["style"] if old["style"] != "default" else None)
    ep = make_episode(Path(a.script), a.slug, a.title or old["title"], style, a.description, old, cfg)
    eps[idx] = ep
    save_json(EPISODES, eps)
    build_feed(cfg, eps)
    git_commit_push(f"Replace episode: {ep['title']} (v{ep['version']})", not a.no_push)


def cmd_remove(a) -> None:
    cfg = load_config()
    eps = load_json(EPISODES, [])
    ep = next((e for e in eps if e["slug"] == a.slug), None)
    if not ep:
        sys.exit(f"No episode '{a.slug}'.")
    (AUDIO_DIR / ep["file"]).unlink(missing_ok=True)
    eps = [e for e in eps if e["slug"] != a.slug]
    save_json(EPISODES, eps)
    build_feed(cfg, eps)
    git_commit_push(f"Remove episode: {ep['title']}", not a.no_push)


def cmd_list(a) -> None:
    for e in sorted(load_json(EPISODES, []), key=lambda e: e["published"]):
        print(f"{e['published'][:10]}  {e['slug']:<40} {e['duration']:>8}  v{e.get('version', 1)}  [{e['style']}]  {e['title']}")


def cmd_feed(a) -> None:
    build_feed(load_config(), load_json(EPISODES, []))


def cmd_preview(a) -> None:
    style = load_style(a.style)
    out = Path(a.output)
    render_audio(Path(a.script).read_text(), style, out, out.stem, "")
    print(f"{out}: {hms(duration_seconds(out))}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("publish")
    s.add_argument("script")
    s.add_argument("--title", required=True)
    s.add_argument("--style")
    s.add_argument("--description")
    s.add_argument("--slug")
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

    s = sub.add_parser("preview")
    s.add_argument("script")
    s.add_argument("--style")
    s.add_argument("-o", "--output", default="preview.mp3")
    s.set_defaults(func=cmd_preview)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
