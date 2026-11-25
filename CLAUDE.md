# Private podcast feeds

Text → styled script → TTS MP3 → `feed.xml` → git commit/push → GitHub Pages → Apple Podcasts.

## Shows ("albums")
Each show is its own Apple Podcasts subscription with its own feed:
- Root folder = **Learning Sessions**: https://obedcanario.github.io/learning-sessions/feed.xml
- `aristotle/` = **Aristotle** (serial; season = book number, episode = chapter):
  https://obedcanario.github.io/learning-sessions/aristotle/feed.xml

Use `./pod --show <folder> ...` for any show other than the root one.
New show: `./pod new-show <folder> --title "Title" [--serial]`, then
`.venv/bin/python make_cover.py <folder> --subtitle "..."`.
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

## Script syntax
- blank line = paragraph pause · `# Heading` = spoken + section pause · `---` = section break
- `[pause]` / `[pause 3]` = silence in seconds
- `> text` = read by the style's quote voice · `{{read 3-5}}` = verbatim source paragraphs (quote voice)

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
