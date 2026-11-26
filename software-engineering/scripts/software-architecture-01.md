---
title: Software Architecture · 1 — The Decisions You Can't Undo
slug: software-architecture-01-decisions-you-cant-undo
season: 2
episode: 1
style: rohn-study
source: software-engineering/sources/software-architecture.md
chapter: 1
description: What software architecture really is, the one-question test for spotting it, and the two laws every architect lives by. A plain-English version of the Wikipedia article, read in full, with commentary.
---
One software company spent two full years rebuilding its own product, just to get back to where it started, while everyone around it kept moving. And the cause wasn't a single disaster. It was a weak beginning, followed by years of small changes, each of which made the next one a little more difficult. [pause 1.5]

By the end of this series, you'll understand exactly how that happens, and how to make sure it never happens to anything you build. It starts today, with one question: which decisions in a system can you never easily take back? [pause 1.5]

Software Engineering, season two: software architecture. Part one: the decisions you can't undo.

So here is what to listen for. First, a simple test that tells you immediately whether a decision is architecture or just a detail. Second, the two laws that every architect lives by, including the one that most people get exactly backwards. Third, five competing definitions of architecture, and why every one of them is partly right.

And here's something fun before we begin. This very episode was produced by a small system: text goes in, a script comes out, a computer voice reads it, and a feed tells your podcast app that it exists. We'll use that system all season as our laboratory, so every idea you hear gets tested on something real. Let's hear it.

{{read 1-3}}

Let's take that down to the studs. Remove the technical vocabulary, and architecture comes down to three things: the parts, the connections between the parts, and the qualities of both. A house has rooms, hallways, and qualities like comfortable or drafty. A software system has components, the paths its information travels between them, and qualities like reliable or fragile. [pause 2]

{{read 4-5}}

This is the test I promised, so lock it in. Before you call something architecture, ask yourself one question: how painful would it be to change this later?

Let's apply that test to our podcast system. The colors on the cover art could be changed in a minute, so they're a detail. But every episode carries a permanent identification number, and your podcast app uses that number to recognize which episode is which. Change it, and every listener's app believes it's looking at a completely new episode. That's a foundation decision: inexpensive to make on day one, and extremely expensive to change on day one hundred.

Here's a line worth remembering: the light switch can move; the foundation can't. [pause 2]

{{read 6-9}}

These two laws sound simple, but there's more underneath them than you'd expect.

Everything is a trade-off. Our podcast system stores its audio at a fairly modest quality, in mono, at sixty-four kilobits per second. Why would anybody choose that? Because the free hosting service has a limit of roughly one gigabyte, and higher-quality sound would consume that space much faster. So there's no universally "best" setting, only the setting that fits the goal. Anyone who claims a decision has no downside simply hasn't discovered the downside yet.

Now the second law, the one most people get backwards. They study how a successful system is built, and they imitate it. But the reasoning is the part that transfers. If you know the audio is small because of a storage limit, then the day that limit disappears, you'll recognize that you're free to change it. Without the reason, you're left guessing, and guessing is exactly how good systems gradually deteriorate.

So write this down: copy the reasons, not just the results. [pause 2]

{{read 10-11}}

Here's the root of it. Features describe what a system does, while architecture determines how well it does those things. Two applications can have identical buttons, and one is fast and secure while the other crashes every Friday afternoon. Same features, different architecture.

Hold on to that phrase, "non-functional requirements," because in part two you'll discover that these "how well" requirements quietly control almost every important decision. [pause 2]

{{read 12-19}}

These five definitions aren't really competing; each one is a different flashlight pointed into the same room. The fourth definition contains a surprising twist: if you make a decision easy to reverse, it stops being architecture. That means one of the smartest moves an architect can make is converting a frightening, permanent choice into an inexpensive, reversible one.

And the fifth definition connects directly to the second law. Diagrams show the how, while decisions, with their reasoning attached, preserve the why. [pause 2]

{{read 20-21}}

Look at the pattern in that history: an intuition, then rough sketches of boxes and lines, then a shared vocabulary, then official standards. That's how almost every discipline matures. And notice that the modern standard includes people and processes as part of the system. The humans belong in the blueprint, too. [pause 2]

{{read 22-23}}

Why can you evaluate a building before constructing it? Because the blueprint is inexpensive and the building is not. Erasing a line costs nothing, while demolishing a wall costs a fortune. Architecture gives software that same inexpensive place to make mistakes: on paper, where mistakes are almost free. [pause 2]

So let's put this episode together.

Architecture is the parts, the connections, and the qualities of both. [pause 1.5]

If it would be painful to change later, it's architecture. [pause 1.5]

Law one: everything is a trade-off. Law two: why matters more than how. [pause 1.5]

Features describe what a system does; architecture determines how well it does it. [pause 2]

Here's your challenge for this week. Choose one thing you've built or managed, whether it's an application, a spreadsheet, a small business, or even your weekly routine. List five decisions inside it, and score each one from one to ten according to how painful it would be to change. Your two highest scores are your architecture. Then, for each of those two, write one sentence explaining why you chose it. If you can't write that sentence, you've just discovered your biggest risk.

Next time, we'll discover what really shapes a system, because it's almost never the features. And you'll hear about a strange law from 1967 which predicts that your software will eventually resemble your organization chart. Once you understand it, you'll never look at a company the same way again.
