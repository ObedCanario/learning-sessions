# Private podcast feeds

Text → styled script → TTS MP3 → `feed.xml` → git commit/push → GitHub Pages → Apple Podcasts.

## Shows ("albums")
Each show is its own Apple Podcasts subscription with its own feed:
- Root folder = **Learning Sessions**: https://obedcanario.github.io/learning-sessions/feed.xml
- `aristotle/` = **Aristotle** (serial; season = book number, episode = chapter):
  https://obedcanario.github.io/learning-sessions/aristotle/feed.xml
  Works so far: Physics II.3 (S2 E3, before Ethics) and Ethics III (S3 E1–12). Titles carry the
  work name ("Physics II · 3 — …"). If two works share a book number, pick a new scheme first.

- `software-engineering/` = **Software Engineering** (serial; season = topic/series, episode = part):
  https://obedcanario.github.io/learning-sessions/software-engineering/feed.xml
  S1 = Structured Analysis (4 parts). v2 (2026-11-26) was redone with the learning-series procedure: our own plain-English
  source, diagrams walked through with one pizza-shop example. The user's write-up is kept in `sources/structured-analysis-original.md`.
  S2 = Software Architecture (4 parts). The user gave the raw Wikipedia text, so the plain-English
  source (`sources/software-architecture.md`) was written by us, and the reader text is also FRE 60–70.
  Episodes use hooks and open loops (a cold-open teaser paid off later), and the series stays under an hour.
  The commentary uses this podcast tool as a running "lab" example; keep its facts true to the code.

Use `./pod --show <folder> ...` for any show other than the root one.
New show: `./pod new-show <folder> --title "Title" [--serial]`, then
`.venv/bin/python make_cover.py <folder> --subtitle "..." [--colors R,G,B:R,G,B]` (give each show its own colors).
When the user says "album", make or reuse a show. Use seasons for books or parts inside it.

## When the user sends "<style>" + text
1. Read `styles/<style>.md` (body = writing guide). If it doesn't exist, create one modeled on
   `styles/jim-rohn.md`. For a real person's style, emulate the delivery only: never claim to be
   them or invent quotes attributed to them.
2. Rewrite the text into a spoken script. Keep all the substance. Save it to `<show>/scripts/<slug>.md`.
3. `./pod [--show s] publish <script> --title "..." --style <style> --description "..."`
4. Report title, duration, and the feed URL.

## When the user wants a text kept intact (book read in full + commentary)
Use `styles/rohn-study.md`. Save the source verbatim to `<show>/sources/<name>.md` with
`Chapter N: Title` lines. One script per chapter, with front matter
(`title, slug, season, episode, style, source, chapter, description`). Insert the original text only with
`{{read a-b}}` (paragraph numbers within the chapter), never by retyping it. Then:
- `./pod --show s check <scripts...>` must say INTACT for each script, and host FRE should be in
  the user's target (Aristotle: 60–70).
- Publish in chapter order so dates and episode numbers line up.

## When the user sends a hard text or URL to learn ("plain English", "first principles", "MrBeast style")
Follow `procedures/learning-series.md`. It is the user's preferred format (golden sample:
Software Engineering S2). Plain-English source written by us, FRE 60–70 for both voices, hooks and open loops,
a challenge each week, a cliffhanger bridge, and the series under the user's time cap.

## Script syntax
- blank line = paragraph pause · `# Heading` = spoken + section pause · `---` = section break
- `[pause]` / `[pause 3]` = silence in seconds
- `> text` = read by the style's quote voice · `{{read 3-5}}` = verbatim source paragraphs (quote voice)
- Front matter `notes: host` = `[bracketed notes]` inside `{{read}}` text are read by the host voice
  (for user-supplied plain-English versions). A paragraph that is all **bold** = heading (section pause)
- `SAY` in podcast.py = spoken-only fixes for the reader voice (`&c.` → etcetera, `2:1` → two to one);
  sources stay verbatim

## Replacing an episode
`./pod [--show s] replace <slug> <script>`: same GUID and date (Apple treats it as the same
episode) and a versioned file (`<slug>-v2.mp3`) so apps re-download it.

## Other commands
`list`, `remove <slug>`, `feed` (rebuild from episodes.json), `preview <script> -o x.mp3` (audio
only), `check <scripts>` (includes + readability).

## Files and setup
- Per show: `podcast.json`, `episodes.json` (source of truth), `feed.xml` + `index.html`
  (generated), `episodes/` (MP3), `scripts/`, `sources/`
- TTS: edge-tts (free Microsoft neural voices). Voices: `.venv/bin/edge-tts --list-voices`
- Setup: `python3 -m venv .venv && .venv/bin/pip install edge-tts pillow textstat` (needs ffmpeg)
- Audio is 64 kbps mono (~0.5 MB/min). The GitHub Pages site limit is ~1 GB, so watch total size.

Feeds are unlisted, not secret: anyone with the URL can listen. They stay out of Apple's
directory because they were never submitted to Podcasts Connect. Do NOT set `itunes_block: true`:
Apple then refuses "Follow a Show by URL" ("server or feed could not be found").
