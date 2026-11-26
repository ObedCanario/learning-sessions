---
title: Structured Analysis · 2 — Breaking a System Down
slug: structured-analysis-02-breaking-it-down
season: 1
episode: 2
style: rohn-study
source: software-engineering/sources/structured-analysis.md
chapter: 2
description: Data and control, building a diagram from outside events, the box with four arrows that describes any job, and why jobs and objects cut the world in different directions. Plain English, read in full, with commentary.
---
Here's a puzzle. A diagram with five circles can be the clearest picture of a business you've ever seen. A diagram with eighty circles, drawn with exactly the same rules, is completely useless. Same shapes, same arrows, same method. So what went wrong between five and eighty? [pause 1.5]

Software Engineering, structured analysis, part two: breaking a system down.

So here is what to listen for. First, the difference between data and control, the information that moves and the signals that say when to act. Second, a practical recipe for building a diagram, starting from events in the outside world. Third, and stay for this one, a single box with four arrows that can describe almost any job on earth, from baking a pizza to performing surgery.

Let's hear it.

{{read 1-3}}

Let's take data and control down to the studs. Data is the material being worked on: the order, the price, the name. Control is the permission or the trigger: start now, stop, this is ready. In a kitchen, the pizza is data, and the bell that says "order up" is control. You need both. Data without control just sits there, and control without data has nothing to act on.

And there's the answer to our puzzle. Eighty bubbles isn't a flaw in one particular diagram; it's a law of complexity. Every picture that tries to show everything at once eventually drowns in its own detail. The solution, as you're about to hear, is to stop showing everything at once. [pause 2]

{{read 4-7}}

This recipe contains a genuinely powerful idea: start from outside events.

Most people describe a system from the inside, beginning with the screens, the buttons, and the database. But a system exists to respond to things that happen in the world. A customer orders. A customer pays. A supplier delivers. If you list those events first, every bubble in your diagram has a reason to exist, and you're far less likely to build something nobody needs.

Then notice how the three documents divide the work. The diagram shows that something flows, the dictionary says exactly what it is, and the process specification says exactly what happens to it. Each one answers a question the other two can't.

Here's a line worth remembering: a picture shows the shape, but only words can pin down the meaning. [pause 2]

{{read 8-10}}

Notice the discipline in that single way of zooming. It's like a set of nesting dolls: open one, and you always find the same kind of thing inside, only smaller. In our podcast system, "publish an episode" contains "write the script," "turn it into audio," "update the feed," and "upload the files." [pause 2]

{{read 11-13}}

Now, this is the one I told you to stay for. Why can one box with four arrows describe almost any job? Because every job, anywhere, has the same four ingredients. Something comes in, something goes out, something sets the rules, and someone or something does the work. A surgeon's operation has a patient going in, a recovering patient coming out, medical guidelines setting the rules, and a surgical team doing the work. Same box, same four arrows.

Let's draw it for our podcast system. The box says "turn the script into audio." The input, from the left, is the written script. The output, on the right, is the audio file. The control, from the top, is the style file, which chooses the voices and the length of the pauses. And the mechanism, from the bottom, is the online voice service and the audio software that stitches everything together.

And notice those two words at the end: cohesion and coupling. Those are the two words from the 1970s I promised you in part one. We'll come back to them in the final part, because they turned out to be the most durable ideas in this entire field. [pause 2]

{{read 14-17}}

Here's the root of the weakness. Structured analysis organizes the world by verbs: take the order, bake, deliver. Object-oriented development organizes it by nouns: an order, a customer, a driver. Both are legitimate ways to cut up reality, but they cut in different directions, so translating one into the other is awkward.

And notice what UML emphasizes: the service window. That's a profound shift. In a large system, the most important decisions often aren't about what happens inside each part, but about what can pass between the parts. Today, we call those windows interfaces, and much of modern software is built from services that communicate through them.

So write this down: in a big system, the connections matter as much as the pieces. [pause 2]

So let's put this episode together.

Data is what moves; control says when to act. [pause 1.5]

Start from the events in the outside world, and give each one a process that responds to it. [pause 1.5]

Every job has four arrows: inputs, outputs, controls, and mechanisms. [pause 1.5]

Jobs and objects cut the world in different directions, and the connections grow more important as systems grow. [pause 2]

Here's your challenge for this week. Take the process you described last time, and draw it as one box with four arrows. Write the input on the left, the output on the right, the rules on top, and the people or tools underneath. Then open the box, and break it into three smaller boxes. You'll quickly find a step where something comes in with no clear source, or goes out with nowhere to go. Those gaps are exactly what analysis is meant to find.

Next time, we'll follow the data, and you'll discover that the most useful picture in this entire method is one with almost nothing in it: a single empty box. Understanding why it's empty can save you from building the wrong system. And you'll find out why two people can argue for an hour and then discover they agreed all along.
