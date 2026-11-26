---
title: Software Architecture · 4 — Deciding, Remembering, and Fighting Decay
slug: software-architecture-04-fighting-decay
season: 2
episode: 4
style: rohn-study
source: software-engineering/sources/software-architecture.md
chapter: 4
description: The four activities architects repeat, two traps that catch almost everyone, decision records, erosion and the two lost years, and fitness functions. A plain-English version of the Wikipedia article, read in full, with commentary.
---
Here's a thought that should make every builder a little nervous. You can design a system almost perfectly, with every decision correct and every trade-off considered, and still watch it fall apart. Not because of one terrible day, but through a thousand small, reasonable changes over several years. So how do you keep a good design good? [pause 1.5]

Software architecture, part four, the final part: deciding, remembering, and fighting decay.

So here is what to listen for. First, the four activities architects repeat for as long as a system exists. Second, two traps that catch almost everyone, and the simple document that rescues you from the second one. Third, how good designs gradually decay. And yes, we'll finally return to that company that lost two years rebuilding its own product.

Let's hear it.

{{read 1-6}}

Let's take it down to the studs: understand the problem, propose a solution, test the solution, and keep it healthy. That's not only architecture. It's how a doctor treats a patient, how a coach develops a team, and how you'd plan a business. And notice the word "repeat." Architecture isn't a phase you complete; it's a loop you stay inside.

That phrase, "architecturally significant requirements," is a long name for a simple idea. Out of a hundred requirements, perhaps five genuinely shape the system, and identifying those five is half the job. [pause 2]

{{read 7-13}}

Notice how much of this concerns people rather than code. Knowledge that exists only in someone's head is like cash hidden under a mattress: it's real, but it's fragile, and when that person leaves, it walks out the door with them. That's why the job includes asking, sharing, and writing things down. [pause 2]

{{read 14-17}}

Here's where it gets personal, because I'd bet you've been caught in both of these traps.

The first one is fear. You don't decide, because you might be wrong. But not deciding is also a decision, and usually a worse one. The last responsible moment is the cure: decide when you know enough, and not a day later. It's like crossing a busy street. You wait for a gap in the traffic, but you don't wait forever for the street to be completely empty.

The second trap is the one the decision record fixes, and here's a real example. Our podcast system has a project notes file containing a rule: don't enable a particular setting that hides the show from Apple's directory. Why not? Because when that setting is enabled, Apple refuses to follow the show by its address at all. That single line is a decision record in miniature, because it explains both what and why. Without it, someone would eventually think, "let's make this more private," flip that setting, and break the entire show. Then they'd waste an afternoon rediscovering a lesson that had already been learned.

So write this down: a decision without a written reason will be argued about forever. [pause 2]

{{read 18-19}}

The root of that tension is simple. Plan too much, and you build the wrong thing very carefully. Plan too little, and you build quickly on a foundation that cracks. "Just enough" means deciding the things that are difficult to change, and leaving everything else flexible, which is exactly the test from part one. [pause 2]

{{read 20-23}}

There it is: the two years. And notice what the text identifies as the cause. Not a single disaster, but a poor beginning, followed by constant changes, each one making the next more difficult. That's erosion, and it resembles a neglected garden. Nobody decides to grow weeds. You simply skip the weeding a few times, and one day you can't find the vegetables.

Now here's the hopeful part, and it's my favorite idea in this entire series: the fitness function. The name comes from physical fitness tests, like a check-up at the gym. Instead of hoping the architecture stays healthy, you write checks that measure it, repeatedly, without anyone having to remember.

Our podcast system has one. Before each episode in this series was published, a check examined its script. It confirmed that every paragraph of the reading was present, in order, with nothing skipped and nothing repeated, and it measured how easy the commentary is to follow, so anything outside the target gets caught before publication. That check is a fitness function. It doesn't rely on anyone's memory. It simply measures, every single time.

Here's a line worth remembering: what gets checked automatically stays true; what only gets remembered gradually fades. [pause 2]

{{read 24-25}}

Think of recovery as a building inspector without blueprints, walking the hallways, tapping on the walls, and drawing what's actually there. It works, but it's slower and more difficult than keeping good records from the beginning, which is the whole point of everything you've heard today. [pause 2]

So let's put this whole series together.

Architecture is the set of decisions that are difficult to undo. [pause 1.5]

Everything is a trade-off, and the why matters more than the how. [pause 1.5]

Qualities shape the system, and systems imitate the teams that build them. [pause 1.5]

Choose the shape that fits, contain your failures, and divide the work into properly sized pieces. [pause 1.5]

Decide at the last responsible moment, write down why, and check the architecture automatically, so it doesn't quietly decay. [pause 2]

Here's your final challenge, and it's the most useful one yet. Choose the most important decision in something you've built or managed, and write a one-page decision record with four parts: the decision, the reasons, the alternatives you rejected, and what would make you change your mind. Then add one simple check, something you can test in a minute, that tells you whether the decision still holds. Do that once, and you'll never again waste an afternoon arguing about the same choice.

That's the end of our series on software architecture. Remember the company that lost two years? The text says it came from a poor beginning and growing erosion, and you now know the defense against both. Think carefully about the few decisions you can't undo, write down why you made them, and check them automatically. That's how you build things that last.
