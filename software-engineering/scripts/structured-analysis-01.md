---
title: Structured Analysis · 1 — Describe the Work Before You Build It
slug: structured-analysis-01-big-picture
season: 1
episode: 1
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 1
description: Why most failed software is the wrong thing built well, the three parts of every real system, and the chain of ideas from clean code to clear analysis. Plain English, read in full, with commentary.
---
Most software that fails doesn't fail because of bad code. It fails because someone built the wrong thing, beautifully, and nobody noticed until the money was gone. [pause 1.5]

By the end of this series, you'll be able to sketch almost any system, a pizza shop, a hospital, or the app on your phone, on a single napkin, and then use a handful of simple pictures to explain everything happening inside it. And along the way, you'll meet two words from the 1970s that are still the most important words in software design. [pause 1.5]

Software Engineering, season one: structured analysis and structured design. Part one: describe the work before you build it.

So here is what to listen for. First, the difference between analysis and design, and why the order matters so much. Second, the three parts of every real system, including the one that almost everyone forgets. Third, the chain of ideas that took the industry from writing one clean program to describing an entire business.

And here's something fun before we begin. This very episode was produced by a small system: text goes in, a script comes out, a computer voice reads it, and a feed tells your podcast app that it exists. We'll use that system throughout the series as our laboratory, so every idea you hear gets tested on something real. Let's hear it.

{{read 1-3}}

Let's take that down to the studs. Why can't a computer simply figure out what you meant? Because people operate on assumptions and common sense, and they quietly fill in every gap. A machine fills in nothing. It does precisely what it's told, so somebody has to make every step explicit: what comes in, what happens to it, and what goes out. That's the entire reason analysis exists.

Here's a line worth remembering: you can't automate what you can't describe. [pause 2]

{{read 4-7}}

This is the one almost everyone forgets: the manual procedures. People describe the software, maybe the hardware, and then they're surprised when the system fails because of a step a human was supposed to perform.

Let's apply it to our podcast system. The program is the code. The hardware is the laptop, plus the servers that host the audio files. But there's also a manual procedure: a person still chooses the text, picks the style, and listens to the result. Remove that person, and the system doesn't just get worse; it stops having a purpose. Describe only the software, and you've described only part of the system. [pause 2]

{{read 8-10}}

Here's the root of it. Methods appear when pain appears. Nobody invents a discipline for entertainment; people invent one because the old way of working has stopped functioning. When programs were small, one clever person could hold the entire thing in their head. As programs grew, that became impossible, and teams needed shared rules and shared pictures, so that many people could work on one system without stepping on each other.

You'll see this pattern throughout software engineering. Every major method is an answer to a particular kind of mess. Understand the mess, and the method makes sense. [pause 2]

{{read 11-12}}

You don't need to memorize those names and dates. What matters is the shape of the timeline: in roughly twenty years, the industry went from almost no guidance to a whole family of methods, each one building on the ones before. Keep an ear out for Larry Constantine, Ed Yourdon, and Tom DeMarco, because their ideas outlived their diagrams. [pause 2]

{{read 13-15}}

This chain is the most important idea in today's episode, so let's slow down. Each step zooms out from the one before, and each step moves the thinking earlier, before the expensive part begins.

Why does that matter so much? Because a mistake becomes more expensive the longer it survives. A wrong idea on a whiteboard costs you an eraser. The same wrong idea, discovered after the software is built and people depend on it, can cost you months. And here's the twist: the CASE tools tried to make all that early thinking faster by having computers draw the diagrams. The tools changed, but the lesson didn't.

So write this down: the earlier you think clearly, the cheaper everything after it becomes. [pause 2]

So let's put this episode together.

Analysis describes the work; design plans the program. [pause 1.5]

A real system includes the programs, the hardware, and the manual steps people still perform. [pause 1.5]

Structured methods were invented because software grew too large for any one person to hold in their head. [pause 1.5]

And the history moves in one direction: from writing code well, to designing well, to understanding the need before building anything. [pause 2]

Here's your challenge for this week. Choose one process you perform regularly, at work or at home, and describe it the way an analyst would. What comes in? What happens to it? What goes out? And which steps are still done by hand? Don't design any solution yet. Just describe the work precisely, and notice how much you didn't know until you wrote it down.

Next time, we'll answer a puzzle. A diagram with five circles can be the clearest picture of a business you've ever seen, while a diagram with eighty circles, drawn with exactly the same rules, is completely useless. What happened in between? And you'll meet a single box with four arrows that can describe almost any job on earth.
