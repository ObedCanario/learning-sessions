---
title: Structured Analysis · 4 — Data Flows, Structure Charts, and Good Modules
slug: structured-analysis-04-good-modules
season: 1
episode: 4
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 4
description: Trace an order through a whole business with one finger, the family tree behind every program, and the two words that explain why small changes break faraway things. Plain English, read in full, with commentary.
---
There's one kind of change that every builder secretly fears: the small one. You adjust something tiny in one place, and something completely unrelated breaks somewhere far away. By the end of this episode, you'll know the two words that explain exactly why that happens, and how to design so it almost never does. [pause 1.5]

Software Engineering, structured analysis, part four, the final part: data flows, structure charts, and good modules.

So here is what to listen for. First, a picture that lets you trace an order through an entire business with one finger. Second, the family tree that serves as a program's blueprint, and why every piece must fit inside a single human brain. Third, cohesion and coupling, the two words I've been promising since part one.

Let's hear it.

{{read 1-5}}

Notice the instruction at the end: trace the loop with your finger. That's the real power of a data-flow diagram, because it transforms an invisible process into something you can physically follow. And look at the order of work: context first, then the data flow, then the explosion into detail. It's the napkin sketch from part one, followed by a zoom, followed by another zoom. [pause 2]

{{read 6-7}}

That "no olives" example captures something important. When people can see where their data travels, they understand why accuracy matters. A note that looks trivial at the counter turns out to affect the kitchen, the receipt, and the complaints. And these diagrams are still in daily use: security teams often begin by drawing one, because every place data crosses from one part to another is a place it might be stolen. [pause 2]

{{read 8-12}}

Let's take the human brain down to the studs. You can only hold a handful of things in mind at once. That's not a weakness to overcome; it's a fixed condition to design around. Any problem bigger than that limit must be divided into pieces that each fit in a single head, and the structure chart is simply the record of those divisions.

Here's a line worth remembering: the size of a problem doesn't matter; the size of each piece does. [pause 2]

{{read 13-17}}

This is the heart of the entire series, and the answer to the fear from the start of this episode.

Why does a small change break something far away? Because of coupling: if two parts depend on each other in many hidden ways, a modification in one inevitably ripples into the other. Strong cohesion keeps a change inside one module, because everything related is already in one place. Loose coupling keeps that change from spreading, because the modules share so little.

Let's make it concrete with our podcast system. Suppose a voice sounds wrong, and you want to switch to a different one. In this system, the voices are chosen in one place, the style file, and nothing else needs to change: not the feed, not the publishing, not the scripts. That's loose coupling at work. In a badly designed tool, the voice name would be scattered throughout the code, and changing it would mean hunting through every file and hoping you found them all.
So write this down: put related things together, and keep the connections few and simple. [pause 2]

{{read 18-20}}

Notice the payoff. Once the analysis and design are precise enough, a machine can generate the empty shells of the program automatically. That idea was ahead of its time. Today, tools routinely generate code from precise descriptions, and the lesson hasn't changed: the clearer your description, the more of the work can be automated. [pause 2]

{{read 21-23}}

And there's the promise from part one, fulfilled. One napkin, with an empty box and the actors around it, and then a handful of pictures that explain everything inside. You can now sketch almost any system that way. [pause 2]

So let's put the whole series together.

You can't automate what you can't describe. [pause 1.5]

Start from the outside: the events, the actors, and everything that crosses the edge. [pause 1.5]

Follow the data, one level at a time, and stop when each piece is simple. [pause 1.5]

Define your words once, so everyone means the same thing. [pause 1.5]

And design for change: strong cohesion inside each part, and loose coupling between the parts. [pause 2]

Here's your final challenge. Look at something you've built or organized, whether it's code, a spreadsheet, or a team. Find the one change you've been avoiding because it feels risky, and ask why it feels risky. Usually, the answer is coupling: the change would ripple into too many other places. Then ask what it would take to gather the related pieces together, and to shrink the connections between them.

That's the end of this series on structured analysis and structured design. The diagrams have mostly been replaced by newer ones, but the thinking underneath them hasn't been replaced at all. Describe the work before you build it, follow the data, and keep your pieces small, focused, and loosely connected. And in season two, we'll zoom out even further, to the decisions that are hardest of all to undo: software architecture.
