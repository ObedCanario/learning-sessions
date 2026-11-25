# Private podcast feed

Text → styled script → TTS MP3 → `feed.xml` → git commit/push → GitHub Pages → Apple Podcasts.

## When the user sends "<style>" + text

1. Read `styles/<style>.md` (body = writing guide). If the style doesn't exist, create a new
   `styles/<slug>.md` modeled on `styles/jim-rohn.md` (pick voice/rate/pauses to fit), then use it.
   For a real person's style, emulate the delivery only: never claim to be them or invent quotes
   attributed to them.
2. Rewrite the user's text into a spoken script following that guide. Keep all the substance.
   Save it to `scripts/<slug>.md`. Script syntax:
   - blank line between paragraphs = paragraph pause
   - `# Heading` = spoken, then a section pause
   - `[pause]` / `[pause 3]` = explicit silence in seconds
   - `---` = section break
3. Publish (renders audio, updates feed, commits, pushes):
   `./pod publish scripts/<slug>.md --title "Title" --style <style> --description "One line"`
4. Report the episode title, duration, and the feed URL.

## Replacing an episode
`./pod replace <slug> scripts/<slug>.md [--title ..] [--style ..]`
Keeps the same GUID and publish date (Apple treats it as the same episode) and writes a
versioned file name (`<slug>-v2.mp3`) so podcast apps re-download the new audio.

## Other commands
- `./pod list` — episodes
- `./pod remove <slug>`
- `./pod preview scripts/x.md --style jim-rohn -o preview.mp3` — audio only, nothing published
- `./pod feed` — rebuild feed.xml from episodes.json
- `.venv/bin/python make_cover.py` — regenerate cover.jpg from the title in podcast.json

## Files
- `podcast.json` — show settings (title, author, base_url)
- `episodes.json` — source of truth for the feed; `feed.xml` is generated from it
- `episodes/` — MP3s, `scripts/` — the spoken scripts, `styles/` — voice + writing presets
- TTS: edge-tts (Microsoft neural voices, free, no key). List voices: `.venv/bin/edge-tts --list-voices`
- Setup on a new machine: `python3 -m venv .venv && .venv/bin/pip install edge-tts pillow` (needs ffmpeg)

The feed has `<itunes:block>Yes</itunes:block>` so it never appears in Apple's directory.
It is unlisted, not secret: anyone with the URL can listen.
