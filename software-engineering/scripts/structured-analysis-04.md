---
title: Structured Analysis · 4 — Data Flows, Structure Charts, and Good Modules
slug: structured-analysis-04-good-modules
season: 1
episode: 4
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 4
description: Data-flow diagrams, structure charts, and the two principles that outlasted every method: cohesion and coupling. Plus how all the pieces fit together. Full text read, with commentary.
---
Software Engineering. Structured analysis and structured design, part four: data flows, structure charts, and good modules.

Here's the question for today: what separates a design that stays easy to change from one that breaks every time you touch it? [pause 1.5]

The answer in this episode is older than most of the programming languages in use today, and it still holds. It comes down to two ideas: keep related things together, and keep the connections between parts few and simple.

So here is what to listen for. First, why a data-flow diagram is as much a communication tool as a technical one. Second, the structure chart, and the reason everything must be cut into pieces small enough for a human brain. Third, cohesion and coupling, the two principles that tie this entire series together.

Let's hear it.

{{read 1-7}}

Notice who the data-flow diagram is really for. It isn't only for programmers. It's for the sponsor who pays and the people who will actually use the system, so that everyone can see the same picture before anything is built.

That last example, the waiter typing "no onions," captures something important. When people can see where their data travels, they understand why accuracy matters. A note that looks trivial at the counter turns out to affect the kitchen, the bill, and the complaints.

And these diagrams are still in use. Security teams today often begin by drawing a data-flow diagram of a system, because once you can see every place data crosses from one part to another, you can see where it might be stolen or tampered with. [pause 2]

{{read 8-15}}

Let's take the human brain down to the studs.

You can only hold a handful of things in mind at once. That's not a weakness to overcome; it's a fixed condition to design around. Any problem bigger than that limit has to be divided into pieces that each fit in a single head. The structure chart is simply the record of those divisions, with each box small enough that one person can understand it completely.

And notice the comparison between the two diagrams. A data-flow diagram is a river map that shows where things move. A structure chart is a family tree that shows who is in charge of whom. You need both views, because a system has both movement and authority.

Here's a line worth remembering: the size of a problem doesn't matter; the size of each piece does. [pause 2]

{{read 16-27}}

This is the heart of the entire series, so let's slow down.

Cohesion means everything inside a module belongs together. Coupling means how much separate modules depend on each other. Good design aims for strong cohesion and loose coupling.

Why would that be true? Because change is inevitable. Every system you build will need to change, and the real question is how far each change spreads. With strong cohesion, a change usually stays inside one module, because everything related is already in one place. With loose coupling, a change in one module rarely forces changes in others, because they share so little.

Let's make it concrete with that text-to-podcast tool. Suppose the voice sounds wrong and you want to switch to a different one. In a well-designed tool, the voice is chosen in one place, and nothing else needs to change: not the feed, not the publishing, not the scripts. That's loose coupling at work. In a badly designed tool, the voice name would be scattered throughout the code, and changing it would mean hunting through every file and hoping you found them all.

And this lesson reaches far beyond software. A team where every person must check with every other person before acting has high coupling, and it moves slowly. A team where each person owns a clear area and passes along only what's necessary moves quickly.

So write this down: put related things together, and keep the connections few and simple. [pause 2]

{{read 28-31}}

Notice the payoff at the end. Once the analysis and design are precise enough, a machine can generate the empty shells of the program automatically. That idea was ahead of its time. Today, tools routinely generate starter code from precise descriptions, and the lesson is the same as it was then: the clearer your description, the more of the work can be automated. [pause 2]

{{read 32-41}}

And there's the whole series in a single line: start outside, follow the data inward, break the work down until it's simple, define every piece of data, and arrange the program as a tree of tidy, loosely connected modules.

So let's put the series together.

You can't automate what you can't describe. [pause 1.5]

Start from the outside: the events, the actors, and everything that crosses the edge. [pause 1.5]

Follow the data, one level at a time, and stop breaking things down when each piece is simple. [pause 1.5]

Define your words once, so everyone means the same thing. [pause 1.5]

And design for change: strong cohesion inside each part, loose coupling between the parts. [pause 2]

Here is a practice for this week. Look at something you've built or organized, whether it's code, a spreadsheet, or a team. Find the one change you've been avoiding because it feels risky, and ask why it feels risky. Usually, the answer is coupling: that change would ripple into too many other places. Then ask what it would take to gather the related pieces together, and to shrink the connections between them.

That's the end of this series on structured analysis and structured design. The diagrams have mostly been replaced by newer ones, but the thinking underneath them hasn't been replaced at all. Describe the work before you build it, follow the data, and keep your pieces small, focused, and loosely connected.
