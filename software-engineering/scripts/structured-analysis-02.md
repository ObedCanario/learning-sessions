---
title: Structured Analysis · 2 — Breaking a System Down
slug: structured-analysis-02-breaking-it-down
season: 1
episode: 2
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 2
description: Data and control, building a diagram from outside events, functional decomposition, and why jobs and objects cut the world in different directions. Full text read, with commentary.
---
Software Engineering. Structured analysis and structured design, part two: breaking a system down.

Here's the question for today: when a system is too big to understand all at once, where do you start cutting? [pause 1.5]

Every complicated thing you've ever understood, you understood in pieces. The real skill isn't breaking something apart. Anyone can do that. The skill is breaking it apart along the right lines, so that each piece makes sense on its own.

So here is what to listen for. First, the difference between data and control, the information that moves, and the signals that say when to act. Second, a practical recipe for building a diagram, starting from events in the outside world. Third, the idea of a single way of zooming, and why that one choice is both the strength and the weakness of this approach.

Let's hear it.

{{read 1-6}}

Let's take data and control down to the studs.

Data is the stuff being worked on: an order, a price, a name. Control is the permission or the trigger: start now, stop, this is ready. In a kitchen, the burger is data and the bell that says "order up" is control. You need both. Data with no control just sits there, and control with no data has nothing to act on.

And notice the honest admission about the problem. With five bubbles, the diagram is clear. With eighty, it becomes spaghetti. That's not a flaw in one diagram; it's a law of complexity. Every method that tries to show everything at once eventually drowns in its own detail. [pause 2]

{{read 7-10}}

This recipe contains a genuinely powerful idea: start from outside events.

Most people start describing a system from the inside, with the screens, the buttons, and the database. But a system exists to respond to things that happen in the world. A customer orders. A supplier delivers. A customer pays. If you list those events first, every bubble in your diagram has a reason to exist, and you're much less likely to build something nobody needs.

Then notice the three documents working together. The diagram shows that something flows. The dictionary says exactly what it is. The process specification says exactly what happens to it. Each one answers a question the other two can't.

Here's a line worth remembering: a picture shows the shape, but only words can pin down the meaning. [pause 2]

{{read 11-14}}

Those lists are mostly history. The diagrams were the lasting contribution, and the big published methodologies were attempts to package them into complete recipes for an entire project.

{{read 15-22}}

This is the heart of the episode, so let's slow down.

Abstraction means hiding detail on purpose, so you can think. "Make dinner" hides a hundred smaller steps, and that's exactly why it's useful. You couldn't plan your evening if you had to think about every onion.

Structured analysis has one way to zoom: job inside job. Run the restaurant, serve food, cook, grill the burger. And at every level, it tracks the same four things: what comes in, what goes out, what rules control the work, and who or what does it.

Let's make it modern. Take that text-to-podcast tool. The overall job is "publish an episode." Inside it: write the script, turn the script into audio, update the feed, and upload the files. Inside "turn the script into audio": split the script into pieces, send each piece to the voice, and stitch the pieces together with pauses. Input: a script. Output: an audio file. Control: the chosen style. Mechanism: the voice service and the audio software.

And then come two words you'll hear for the rest of your career: cohesion and coupling. Everything inside one function should belong together, and separate functions should depend on each other as little as possible. We'll come back to these in part four, because they turned out to be the most durable ideas in this entire field. [pause 2]

{{read 23-27}}

Here's the root of the weakness. Structured analysis organizes the world by verbs: cook, bill, deliver. Object-oriented development organizes the world by nouns: an order, a table, a cook. Both are legitimate ways to cut up reality, but they cut in different directions, so translating one into the other is awkward.

Neither one is simply right. Some problems are naturally about steps and flows, and some are naturally about things and their behavior. A skilled engineer learns to notice which kind of problem is in front of them. [pause 2]

{{read 28-30}}

Notice what UML emphasizes: the window between the counters. That's a deep shift. In a large system, the most important decisions often aren't about what happens inside each part. They're about what can pass between the parts. Today we call those windows interfaces, or APIs, and much of modern software is built from services that talk to each other through them.

So write this down: in a big system, the connections matter as much as the pieces. [pause 2]

So let's put this episode together.

Data is what moves. Control says when to act. [pause 1.5]

Start from the events in the outside world, and give each one a process that responds to it. [pause 1.5]

Structured analysis zooms in only one way: job inside job, tracking inputs, outputs, controls, and mechanisms. [pause 1.5]

Jobs and objects cut the world in different directions, and interfaces become more important as systems grow. [pause 2]

Here is a practice for this week. Take that process you described last time, and break it down two levels: the overall job, the three or four jobs inside it, and the steps inside one of those. For each piece, write its input and its output. You'll quickly find the places where something comes in with no clear source, or goes out with nowhere to go. Those gaps are exactly what analysis is meant to find.

In part three, we'll follow the data: DeMarco's four tools, the context diagram that shows a system from the outside, and the data dictionary that keeps everyone using words the same way.
