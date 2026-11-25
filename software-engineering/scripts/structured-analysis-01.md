---
title: Structured Analysis · 1 — The Big Picture and Where It Came From
slug: structured-analysis-01-big-picture
season: 1
episode: 1
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 1
description: What structured analysis and structured design are, why they were invented, and the chain from programming to design to analysis. Full text read, with commentary.
---
Software Engineering. Structured analysis and structured design, part one: the big picture, and where it came from.

Here's the question for today: before anyone writes a single line of code, how do you figure out what the code is supposed to do? [pause 1.5]

That sounds like a small question, but it's where most software succeeds or fails. Programs rarely fail because someone typed the wrong symbol. They fail because someone built the wrong thing, or built the right thing without understanding the work it was supposed to support. Structured analysis is one of the first serious attempts to solve that problem, and the ideas it introduced are still hiding inside almost every system you use today.

So here is what to listen for. First, the difference between analysis and design: describing the work, versus planning the program. Second, the three things a business actually needs when it automates its work, and why only one of them is software. Third, the chain of ideas that grew from writing a single clean program to describing an entire business.

Today's reading is a plain-English version of the Wikipedia article on structured analysis, with a restaurant example running through it. Let's hear it.

{{read 1-3}}

Let's take that down to the studs.

A computer can't guess what you intended. People can operate with vague instructions, because they fill the gaps with common sense and experience, but a machine does exactly what it's told and nothing more. So somebody has to make the work completely explicit: what comes in, what happens to it, and what goes out. That's the entire reason analysis exists.

Here's a line worth remembering: you can't automate what you can't describe. [pause 2]

{{read 4-8}}

Notice the three things a business needs: the programs, the hardware, and the manual procedures. That third item is the one people forget most often.

Think about any tool you've ever built for yourself. Imagine a small system that takes a piece of text, turns it into audio with a computer voice, and publishes it as a podcast. The program is the code. The hardware is the laptop and the servers that host the files. But there's also a manual procedure: a person still chooses the text, picks the style, and checks the result. If you describe only the software, you've described only part of the system. [pause 2]

{{read 9-12}}

Here's the root of it. Methods appear when pain appears. Nobody invents a discipline for entertainment; they invent it because the old way of working has stopped functioning. When programs were small, one clever person could keep the entire thing in their head. As programs grew larger, that became impossible, and teams needed shared rules and shared pictures so that many people could work on one system without interfering with each other.

You'll see this pattern again and again in software engineering. Every major method is an answer to a specific kind of mess. If you understand the mess, the method makes sense. [pause 2]

{{read 13-30}}

You don't need to memorize those names and dates. What matters is the shape of the timeline. In roughly twenty years, the industry went from almost no guidance to a whole family of methods, each one building on the ones before. A few of these names, especially Larry Constantine, Ed Yourdon, and Tom DeMarco, will come up again in this series, because their ideas outlived their diagrams.

{{read 31-34}}

This chain is the most important idea in today's episode, so let's slow down.

First, people learned to write one program cleanly. Then they learned to arrange many program pieces cleanly. Then they learned to describe the whole business need before building anything at all. Each step zooms out from the one before, and each step moves the thinking earlier, before the expensive part begins.

Why does that matter? Because a mistake costs less the earlier you catch it. A wrong idea on a whiteboard costs you an eraser. The same wrong idea, discovered after the software is built and people depend on it, can cost months.

So write this down: the earlier you think clearly, the cheaper everything after it becomes. [pause 2]

So let's put this episode together.

Analysis describes the work. Design plans the program. [pause 1.5]

A real system includes programs, hardware, and the manual steps people still perform. [pause 1.5]

Structured methods were invented because software grew too large for any one person to hold in their head. [pause 1.5]

And the history moves in one direction: from writing code well, to designing well, to understanding the need before building anything. [pause 2]

Here is a practice for this week. Choose one process you do regularly, whether it's at work or at home, and describe it the way an analyst would. What comes in? What happens to it? What goes out? And which steps are still done by hand? Don't design any solution yet. Just describe the work precisely, and notice how much you didn't know until you wrote it down.

In part two, we'll see what structured analysis actually does: how it turns a business into data and control, how it breaks a system into smaller and smaller jobs, and where that approach runs into its limits.
