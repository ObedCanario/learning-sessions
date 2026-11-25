---
title: Structured Analysis · 3 — Follow the Data
slug: structured-analysis-03-follow-the-data
season: 1
episode: 3
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 3
description: Top-down analysis, DeMarco's four tools, the context diagram, and the data dictionary that keeps a system's words consistent. Full text read, with commentary.
---
Software Engineering. Structured analysis and structured design, part three: follow the data.

Here's the question for today: if you want to understand how a system really works, what should you follow? [pause 1.5]

Structured analysis gives a clear answer: follow the data. Don't start with the screens, the code, or the org chart. Pick up one piece of information and trace where it goes, what changes it, and where it ends up. That single habit will teach you more about a system than hours of reading documentation.

So here is what to listen for. First, the trade-off at the center of top-down thinking: more detail means less breadth. Second, Tom DeMarco's four tools, and the moment when you should stop breaking things down. Third, two tools that every builder should know: the context diagram, which looks at a system from the outside, and the data dictionary, which pins down what every word means.

Let's hear it.

{{read 1-6}}

Let's take the zoom trade-off down to the studs.

Your attention is genuinely limited. You can examine the whole map, or you can examine one particular street, but you can't absorb every street in the country simultaneously. Top-down analysis accepts that limit instead of fighting it. You study the top level first, then open one part at a time, and you deliberately ignore the details that don't matter yet.

That's not just a technique for software. It's how you learn anything difficult. Get the outline first, then fill in one section at a time.

Here's a line worth remembering: you don't understand a system by seeing everything; you understand it by seeing the right level at the right time. [pause 2]

{{read 7-16}}

Notice the stopping rule. You keep breaking a process down until its job is easy to understand, and then you stop. That smallest useful piece is called a functional primitive, and it gets a short, precise description.

Why does that matter? Because both mistakes are expensive. If you stop too early, the pieces remain confusing, and people will inevitably misunderstand them. If you continue too far, you drown in trivial detail, like writing an entire page of instructions for flipping a burger. The real skill is recognizing when a piece is simple enough.

And look at the dictionary entries: an order is a table number, a list of items, and a time. An item is a dish, a quantity, and a special request. Once those definitions exist, nobody has to guess. Every arrow labeled "order" on every diagram means exactly the same thing. [pause 2]

{{read 17-25}}

This is one of the most practical tools in the entire article, and it's still in daily use. Today, many teams draw what they call a system context diagram as the very first picture of a new system, for exactly the reason given here.

Let's take it down to the studs. Before you study the inside of anything, list everything that touches it from the outside. Every outside actor brings requirements with it, so if you forget one actor, you forget all of their requirements at once.

Let's apply it to that text-to-podcast tool. Put the tool in the middle as one sealed box. Around it: the person who sends the text and the style. The voice service that turns words into audio. The hosting service that stores the files. And the podcast app that reads the feed and plays the episodes. Now notice what each one demands. The podcast app has rules about feeds and cover images. The hosting service has size limits. Forget either one, and the system breaks in a way no amount of clever code inside the box can fix.

So write this down: most surprises come from outside the box. [pause 2]

{{read 26-34}}

Here's the root of the data dictionary. It contains no data at all, only descriptions of the data, and yet without it the data is practically useless. That sounds like a paradox, but it isn't one. A library without a catalog still possesses every one of its books, but nobody can locate any of them.

And notice the final example, the chain of restaurants where one kitchen writes "MED," another writes "M," and another writes "medium." That problem appears everywhere: in spreadsheets, in companies, and even in conversations. Two people argue for an hour, and it turns out they were using the same word to mean different things.

The fix is always the same: agree on the definitions first. It's unglamorous work, but it prevents an enormous amount of confusion later. [pause 2]

So let's put this episode together.

Follow the data, and study one level at a time: more detail always means less breadth. [pause 1.5]

Break processes down until each one is simple, and then stop. [pause 1.5]

Before studying the inside of a system, list everything that touches it from the outside. [pause 1.5]

Define your data once, and make everyone use the same definitions. [pause 2]

Here is a practice for this week. Draw a context diagram for something you use or run: a project, a small business, or a tool you've built. Put it in the middle as one box. Around it, list every person, organization, and system that sends something in or takes something out, and label each arrow with what flows. Then ask yourself one question: which of these did I forget to plan for?

In part four, the final part of this series, we'll look at data-flow diagrams in action, the structure chart that serves as a program's blueprint, and the two design principles that have outlasted every method in this story: cohesion and coupling.
