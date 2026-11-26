# Procedure: hard-topic learning series (golden sample)

Use this when the user sends a hard text or URL (an article, paper, or Wikipedia page) and wants
to *fully grasp* it. The **golden sample** is Software Engineering S2, "Software Architecture":
- Source: `software-engineering/sources/software-architecture.md`
- Scripts: `software-engineering/scripts/software-architecture-01..04.md`
- Result: 4 episodes, 52:42 in total. Host FRE 61–66, reader FRE 61–70, every reading INTACT.

Read those files before writing a new series. Match their shape, tone, and pacing.

## 1. Budget first
- Ask for, or assume, a cap for the whole series (default: under an hour).
- Measured pace: about **132 spoken words per minute**, pauses included (rohn-study voices).
  So an hour holds about 7,900 words. Aim for **about 85% of the cap** (an hour gives about 6,600–7,000 words).
- Split the cap into 3–5 episodes of 12–15 minutes each. Per episode, aim for about 700–900 reader
  words and about 900–1,000 host words.

## 2. Write the plain-English source (the reader's text)
Save it to `<show>/sources/<name>.md`. The header comment names the original and its license, and
lists what was left out and why.
- **Restructure for learning, not for the original's order.** Use the arc *what it is → what shapes it →
  the shapes and tools → how it lives and dies over time*. Put the history where it helps (usually short, in part 1).
- **Keep every essential idea; cut only detail** (long lists of names, minor methods, citation notes).
  Name what you cut in the header comment.
- **Define every named term in plain words** right where it first appears.
- Reader FRE **60–70**. Use short paragraphs. Each heading goes on its own line, written as `**Bold**`.
- **No emoji, arrows, tables, or "4+1"-style symbols.** Write them as words. Lists become one paragraph per item.
- Diagrams: describe them as **one concrete, everyday example walked through step by step**
  ("Picture a box in the middle labeled..."). Never write "see figure". Reuse the same example across diagrams.
- Facts stay faithful to the source. Opinions, analogies, and "why it matters" go to the host, not the reader.
- Use `Chapter N: Title` lines, one chapter per episode.

## 3. Write each script (the host's commentary)
Front matter: `title, slug, season, episode, style: rohn-study, source, chapter, description`.
Titles: `<Series> · N — <Hooky title>`.

**Retention structure** (MrBeast-style pacing; emulate the structure only):
1. **Cold open with stakes** in the first 2–3 sentences: a surprising fact, a cost, or a mystery.
   In part 1, plant a **series-long open loop** (S2: "one company lost two years...") and pay it off in the final part.
2. Then the show line: `Software Engineering, season N: <series>. Part one: <title>.`
3. **"So here is what to listen for"**: 3 promises. At least one is a tease ("stay for this one",
   "you'll have both before the halfway mark").
4. **Read and comment, alternating** (`{{read a-b}}`). Pay off each promise where you said you would.
   Re-hook in the middle: "Here's where it gets interesting", "Now, this is the one I told you to stay for."
5. **Recap**: 4–5 lines, each followed by `[pause 1.5]` and the last by `[pause 2]`.
6. **"Here's your challenge for this week"**: a concrete 10-minute exercise with a payoff sentence.
7. **Cliffhanger bridge** to the next part, with a specific tease (not just a topic list).
   The final part closes the series-long loop and ends on one memorable line.

**Teaching moves** (Rohn-style delivery; never claim to be Rohn or invent quotes):
- First principles: "Let's take it down to the studs." "Here's the root of it." Ask "why would that be true?"
- Unpack every metaphor: name the picture, what it maps to, and a modern everyday version.
- One quotable line per core idea ("Here's a line worth remembering:" / "So write this down:"), then `[pause 2]`.
  Use about 3–4 per episode.
- **The lab**: test ideas on this podcast tool (text → script → TTS → feed → GitHub Pages → Apple).
  Real facts you can use: permanent GUIDs, 64 kbps mono because of the ~1 GB limit, TTS retries
  (up to 4 tries), the `check` command (a fitness function), the itunes_block rule in CLAUDE.md
  (a decision record), voices set in one style file, episodes.json as the source of truth.
  **Check any new claim about the tool against the code first.**
- Don't comment on every reading. Let simple passages run back to back.

## 4. Check, tune, measure
- `./pod --show <s> check <scripts...>`: each must say INTACT, with host FRE 60–70 and reader FRE 60–70.
- If FRE is too high (too easy): merge short sentences, and use precise words with more syllables
  ("decision", "determine", "particular"). Don't make it all choppy, punchy lines.
- If FRE is too low: split long sentences and swap jargon for plain words.
- Add up the words against the budget. **Render episode 1 first**, read its real duration, and
  re-project the series before rendering the rest. Trim if needed.

## 5. Publish and verify
- New episodes: publish in order (`./pod --show s publish <script>`), in the background, with
  `set -o pipefail` and `grep --line-buffered`.
- Redoing existing episodes: `./pod --show s replace <slug> <script> --description "..."`.
  Pass `--description`, because replace otherwise keeps the old one.
- Check that the feed has the right number of items and that one MP3 returns 206 on a range request.
  Send episode 1 to the user while the rest render.
- Report a table (episode, title, length), the FRE ranges, what was restructured or cut, the hooks used, and the feed URL.
