---
title: Software Architecture · 3 — Shapes, Styles, and Patterns
slug: software-architecture-03-shapes-styles-patterns
season: 2
episode: 3
style: rohn-study
source: software-engineering/sources/software-architecture.md
chapter: 3
description: Monolith versus distributed, four classic styles, the circuit breaker, and a six-step cycle for cutting a system into right-sized parts. A plain-English version of the Wikipedia article, read in full, with commentary.
---
For about a decade, one idea swept through the software industry: break your system into dozens of tiny services. The biggest companies did it, and soon everyone wanted to. Then something unexpected happened. Some teams that switched became slower than before, buried in problems they never had when everything lived in one place. So what went wrong? It wasn't the idea itself. It was choosing a shape without asking what it would cost. [pause 1.5]

Software architecture, part three: shapes, styles, and patterns.

So here is what to listen for. First, the one decision every system makes, one big piece or many small ones, and what each option really costs. Second, four classic layouts, and a pattern borrowed directly from the electrical panel in your house. Third, a six-step cycle for cutting a system into properly sized pieces. By the end, you'll be able to look at almost any application and make an educated guess about its shape.

Let's hear it.

{{read 1-2}}

Let's take it down to the studs, because this is the first law all over again. A monolith is like a food truck: one vehicle, one crew, and everything within arm's reach. It's simple and inexpensive to operate, but if the grill needs repairs, the entire truck stops serving.

A distributed system is like a food court, with many separate stalls, each one free to change its menu independently. But now customers travel between the stalls, orders get lost along the way, and when the electricity fails in one corner, you'd better have a plan. That journey between stalls is the network. A request across a network is much slower than a request inside one program, and occasionally it simply fails. So distributed systems purchase freedom, and they pay for it with complexity.

Here's a line worth remembering: one piece is simpler to operate, many pieces are easier to change independently, and neither one is free. [pause 2]

{{read 3-8}}

Notice that every style is really a rule about who's allowed to communicate with whom. Layers say: only talk to your neighbors. Events say: make your announcement, and don't worry about who's listening. Hexagonal says: the core only communicates through fixed doorways.

Let's apply that to our podcast system. Right now, it operates like a pipeline, a close relative of layers: the script comes first, then the audio, then the feed, then publishing, with each step handing its result to the next. Now imagine a hexagonal version. The core would know it needs "a voice," but not which company provides it. If the free voice service ever disappeared, you'd connect a replacement to the port, and nothing else would have to change. That's the benefit of fixed doorways: you can replace what's outside without rebuilding what's inside. [pause 2]

{{read 9-12}}

Let's unpack that electrical picture. Why does your house have a breaker? Because without one, a single defective toaster could overheat the wiring and start a fire. The breaker accepts a small loss, a dark kitchen, to prevent an enormous one. A circuit breaker in software makes the same bargain: when one service keeps failing, you stop calling it for a while, so the failure stays small and the rest of the system keeps running.

Remember the retry in our podcast system from last time, which tries the voice service up to four times? A circuit breaker is the next step up. After enough failures, it would stop trying for a while and report the problem clearly, instead of repeatedly hammering a service that's already down.

And notice the bigger idea here. A pattern is a solution that somebody else already paid for in pain, so when you use one, you're borrowing their lessons without repeating their mistakes. [pause 2]

{{read 13-21}}

This is the heart of the episode, so let's slow down. Why is choosing the right size so difficult? Because both mistakes are expensive. Make the pieces too big, and every change affects everything. Make them too small, and you spend all your time managing the connections, which is exactly the trap from the beginning of this episode.

Now consider that first step, the choice between splitting by technical layer and splitting by business area. Picture a restaurant kitchen. Splitting by technical layer means one team for all the chopping, another for all the cooking, and another for all the plating. Splitting by business area means one team for pizza, one for pasta, and one for desserts, where each team handles its own chopping, cooking, and plating. If you want to introduce a new pasta dish, the second arrangement means only one team has to change.

And notice the final step: go around again. Nobody gets the pieces right the first time, so the cycle assumes you'll learn and adjust. That isn't a weakness in the method; it is the method. [pause 2]

{{read 22-23}}

The word "kata" comes from the martial arts, where it means a practice routine, a sequence of movements you repeat until it becomes second nature. Architecture is a skill, and skills come from practice, not just from reading. And notice the phrase "just enough": a drawing that shows every detail is almost as useless as no drawing at all. [pause 2]

So let's put this episode together.

One piece is simpler to operate, many pieces are easier to change, and neither one is free. [pause 1.5]

A style is the overall layout; a pattern is a proven solution to a problem that keeps returning. [pause 1.5]

Contain your failures, the way a breaker protects a house. [pause 1.5]

Divide the system, assign the work, check the qualities, and then go around again. [pause 2]

Here's your challenge for this week: perform a miniature kata. Choose a simple business, like a coffee shop with online ordering, or a gym that schedules classes. In ten minutes, list its three most important qualities. Then sketch it two ways, once divided by technical layer and once divided by business area, and ask yourself which version would be easier to change when the owner introduces something new next year. There's no answer key. The thinking is the workout.

In the final part, we'll follow a system through its entire life: how architects make decisions and record them, the two traps that catch almost everyone, and how good designs gradually decay. And we'll finally return to that company that lost two years rebuilding its own product.
