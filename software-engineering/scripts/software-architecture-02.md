---
title: Software Architecture · 2 — The Hidden Forces That Shape a System
slug: software-architecture-02-hidden-forces
season: 2
episode: 2
style: rohn-study
source: software-engineering/sources/software-architecture.md
chapter: 2
description: Why qualities, not features, decide a system's shape; how business goals turn into "ilities"; views, conceptual integrity, and Conway's Law. A plain-English version of the Wikipedia article, read in full, with commentary.
---
Here's a strange fact. Two companies can build applications with identical features, the same buttons and the same screens, and end up with systems that look completely different on the inside. One is a single program. The other is a hundred small programs communicating across a network. Same features, entirely different shape. So if the features don't determine the shape of a system, what does? [pause 1.5]

Software architecture, part two: the hidden forces that shape a system.

So here is what to listen for. First, the real driver of architecture, and a practical way to translate business goals into technical qualities. Second, the technique architects use to avoid drowning in complexity. Third, and stay for this one, a law from 1967 that predicts what your software will look like just by examining your organization chart. It's one of the strangest and most reliable ideas in the entire field.

Let's hear it.

{{read 1-3}}

Let's take it down to the studs. A feature is a verb: send, pay, play. A quality is an adverb: how quickly, how safely, how reliably. And here's the root of it: the adverbs are what force the big structural decisions. "Let people play an episode" fits into almost any design, but "let a million people play an episode at the same moment, without a single failure" eliminates most designs immediately.

So write this down: features tell you what to build; qualities tell you how to shape it. [pause 2]

{{read 4-10}}

This is the most practical tool in the episode. Business leaders rarely announce, "we need interoperability." They say, "we're acquiring a competitor next year." The architect's job is to hear that sentence and translate it: we'll need to connect two systems that were never designed to communicate, so we'd better prepare for that now.

Let's apply it to our podcast system. The goal is one listener, learning on the go, at no cost. So the qualities that matter are simplicity and affordability. Notice what's missing from that list: scalability. The system doesn't need to serve a million listeners, so designing for a million would be wasted effort. That isn't laziness; it's the first law in action. Every quality costs something, so you only pay for the qualities you actually need. But if you ever decided to sell this tool to thousands of customers, the goal would change, the qualities would change, and the architecture would have to change along with them. [pause 2]

{{read 11-14}}

Notice the problem, and then the solution. The problem is that one picture can't answer everyone's questions. The owner asks what it costs to operate, the developer asks where the code belongs, and the operator asks which machine it's running on. Cram all of that into a single diagram, and nobody can read it.

The solution is the same technique a mapmaker uses. A road map, a weather map, and a terrain map all describe the same territory, but each one answers a different question. Architectural views work the same way: the same system, different questions, and a separate picture for each. [pause 2]

{{read 15-16}}

Here's why that matters. You've probably used software that feels like it was assembled by ten strangers who never met, where every screen behaves differently and every button is somewhere unexpected. That's a system without conceptual integrity. Each addition made sense individually, but nobody was protecting the whole. The architect's job is to be the person who can say, "that's a good idea, but it doesn't belong here." [pause 2]

{{read 17-18}}

Now, this is the one I told you to stay for. Why would a system imitate the shape of the organization that builds it? Let's take it down to the studs. Software components have to agree on how they connect, and people have to communicate in order to agree on anything. So wherever two teams communicate easily, their components connect smoothly. And wherever two teams rarely talk, you get a hard boundary in the code, precisely where the boundary between the teams is.

Look at our podcast system. It was built by one person, so it's mostly one program, in one folder, with one consistent way of doing things. That's not a coincidence; it's Conway's Law. And the law works in reverse, too: some companies deliberately organize their teams in the shape of the system they want, so the system naturally grows into that shape.

Here's a line worth remembering: if you want to change the system, you may have to change the team. [pause 2]

{{read 19-20}}

Let's make that concrete. When our podcast system converts a script into audio, it sends the words to an online voice service, and then it waits. If that service is slow, publishing is slow, and if it's unavailable, publishing stops. The two are chained together. In fact, the system already anticipates this: when the voice service fails, it waits a few seconds and tries again, up to four attempts in total. That's a small but genuine architectural decision, made because of this exact rule. [pause 2]

So let's put this episode together.

Qualities, not features, determine the shape of a system. [pause 1.5]

Translate every business goal into the few qualities that matter, and pay only for those. [pause 1.5]

Use separate views, so each person gets the picture that answers their question. [pause 1.5]

Protect one vision, and remember that systems imitate the teams that build them. [pause 2]

Here's your challenge for this week. Choose any application you use every day, and write down what you believe its three most important qualities are. A banking application? Probably security, availability, and accuracy. A video game? Perhaps speed and smooth graphics. Then ask yourself what that application would look like if it had chosen a different three. You'll start to realize that every product you love is really a collection of trade-offs that someone chose deliberately.

Next time, we'll examine the shapes themselves: the single giant program versus the swarm of tiny services, a pattern that prevents one failure from taking down everything, and a six-step cycle for cutting a system into properly sized pieces. And you'll hear why the most popular choice of the last decade can be exactly the wrong one for a small team.
