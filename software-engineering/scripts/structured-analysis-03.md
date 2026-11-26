---
title: Structured Analysis · 3 — Follow the Data
slug: structured-analysis-03-follow-the-data
season: 1
episode: 3
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 3
description: Top-down analysis, DeMarco's four tools, the empty box that shows a system from the outside, and the data dictionary that keeps everyone's words consistent. Plain English, read in full, with commentary.
---
Two people can argue for an hour, getting more and more frustrated, and then discover they agreed all along. They were simply using the same word to mean two different things. Now imagine that happening inside a company with fifty locations and a million records. It happens constantly, and it costs a fortune. [pause 1.5]

Software Engineering, structured analysis, part three: follow the data.

So here is what to listen for. First, the trade-off at the center of top-down thinking: more detail always means less breadth. Second, Tom DeMarco's four tools, and the moment when you should stop breaking things down. Third, the most useful picture in this entire method, a single box with nothing drawn inside it, and why that emptiness is the whole point.

Let's hear it.

{{read 1-3}}

Let's take the zoom trade-off down to the studs. Your attention is genuinely limited. You can examine the whole map, or you can examine one particular street, but you can't absorb every street in the country simultaneously. Top-down analysis accepts that limit instead of fighting it: study the top level first, then open one part at a time, and deliberately ignore whatever doesn't matter yet.
Here's a line worth remembering: you don't understand a system by seeing everything; you understand it by seeing the right level at the right time. [pause 2]

{{read 4-8}}

Notice the stopping rule. You keep breaking a process down until its job is easy to understand, and then you stop. Why does that matter? Because both mistakes are expensive. Stop too early, and the pieces stay confusing, so people misunderstand them. Keep going too far, and you drown in trivial detail, like writing an entire page of instructions for cutting a pizza into eight slices. The real skill is recognizing when a piece is simple enough. [pause 2]

{{read 9-10}}

And there's the answer to our opening puzzle. Once "order" has exactly one definition, nobody has to guess, and every arrow labeled "order" on every diagram means precisely the same thing. That's the whole cure for the hour-long argument: agree on the definitions first.

Our podcast system has a dictionary like this. Every episode is recorded in one file, with the same fields every time: a title, a description, a duration, a permanent identification number, a season, and an episode number. Because every episode follows the same definition, the feed can be rebuilt from that file at any moment, and nothing gets lost or mislabeled. [pause 2]

{{read 11-14}}

Now, this is the one I promised. Why is the most useful picture one with nothing drawn inside the box? Because the emptiness forces your attention outward. Before you study the inside of anything, you list everything that touches it from the outside, and every outside actor brings requirements with it. Forget one actor, and you forget all of their requirements at once.

Let's draw one for our podcast system. Put the tool in the middle as one sealed box. Around it: the person who sends the text and the style, the voice service that turns words into audio, the hosting service that stores the files, and the podcast app that reads the feed. Now notice what each one demands. The podcast app has strict rules about feeds and cover images, and the hosting service has size limits. Forget either one, and the system breaks in a way that no amount of clever code inside the box can fix.

So write this down: most surprises come from outside the box. [pause 2]

{{read 15-18}}

Here's the root of that pantry picture. The dictionary contains no data at all, only descriptions of the data, and yet without it, the data is practically useless. That sounds like a paradox, but it isn't. A library without a catalog still owns every one of its books, but nobody can locate any of them. And notice that "one customer places many orders" is a business rule, not just a drawing. [pause 2]

{{read 19-20}}

That chain of pizza shops is the hour-long argument from the start of this episode, multiplied by fifty. It's unglamorous work to agree on every code and every label, but it prevents an enormous amount of confusion later. [pause 2]

So let's put this episode together.

Follow the data, one level at a time, because more detail always means less breadth. [pause 1.5]

Break processes down until each one is simple, and then stop. [pause 1.5]

Before studying the inside of a system, draw it as an empty box and list everything that touches it from the outside. [pause 1.5]

Define your data once, and make everyone use the same definitions. [pause 2]

Here's your challenge for this week. Draw a context diagram for something you use or run: a project, a small business, or a tool you've built. Put it in the middle as one empty box. Around it, list every person, organization, and system that sends something in or takes something out, and label each arrow with what flows. Then ask yourself one question: which of these did I forget to plan for?

In the final part, you'll trace a pizza order through an entire business with one finger, see the family tree that serves as a program's blueprint, and finally learn those two words from the 1970s that explain why a small change in one place can break something far away.
