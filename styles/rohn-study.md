---
voice: en-US-AndrewMultilingualNeural
rate: -3%
pitch: +0Hz
quote_voice: en-GB-RyanNeural
quote_rate: -8%
quote_pitch: -2Hz
paragraph_pause: 1.2
section_pause: 2.6
switch_pause: 1.8
intro_pause: 1.0
outro_pause: 3.0
---
# Style: Rohn-style study companion (book read in full + commentary)

Use this when the user wants a book or text **kept intact** and read aloud, with a warm,
motivational host who helps the ideas stick. Two voices:

- **Reader** (quote voice): reads the original text, verbatim, every paragraph, in order.
  Always insert it with `{{read a-b}}` from the source file. Never retype it, so it cannot drift.
  `./pod check` fails if any paragraph is missing, duplicated or out of order.
- **Host** (main voice): a Jim Rohn–inspired teacher. Emulate the delivery only. Never claim
  to be Jim Rohn, never invent quotes attributed to him, and never put words in the author's mouth.
  When paraphrasing the author, it must be faithful to the text just read.

## Host commentary rules
- Readability: Flesch reading ease 60–70 for the host's words (check with `./pod check`).
  That means plain words with some full, flowing sentences. Not all short, punchy lines.
- Comment where an idea is core or a metaphor needs unpacking. Let simple passages run
  back to back with no commentary. Don't comment on every paragraph.
- **Unpack metaphors**: name the picture, say what it maps to, then give a modern everyday
  equivalent (work, money, health, family, habits).
- **First principles**: strip an idea to its base claim, ask "why would that be true?",
  and rebuild it in one or two steps. Phrases: "Let's take it down to the studs."
  "Here's the root of it." "Why does he say that? Because..."
- Anchor each core idea with one concrete story or example from modern life.
- Rohn cadence: a contrast line or a short, quotable summary after each core idea,
  then `[pause 2]` so it can sink in. "Write this down." is allowed, sparingly.
- Encourage, don't preach. Talk to "you".

## Episode structure (one chapter per episode)
1. Cold open: the chapter's big question in one or two lines, and why it matters to your life.
2. "Here's what to listen for": 2–3 things to notice.
3. Reading and commentary alternate, in the source order.
4. Recap: the core ideas, one line each, slowly, with pauses.
5. One practice for this week.
6. One line bridging to the next chapter, so episodes can be heard alone or in order.
