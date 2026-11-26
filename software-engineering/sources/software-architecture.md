# Software Architecture, Made Plain
# Source: Wikipedia, "Software architecture" (CC BY-SA 4.0), https://en.wikipedia.org/wiki/Software_architecture
# Plain-English version written for this show (2026-11-25): restructured into four chapters,
# with the named terms defined. The less essential details were left out: the four families of erosion
# detection, the TARA and SARA reports, and the UC Irvine research program.

Chapter 1: The Decisions You Can't Undo

**What software architecture is**

Every piece of software has a shape. It is made of parts, the parts are connected, and both the parts and the connections have qualities: how fast they are, how safe, how easy to change. Software architecture is the set of big structures you need in order to think clearly about a system. It is also the skill of choosing those structures well.

The name comes from buildings. An architect draws the blueprints before anyone pours concrete. A software architecture works the same way. It is the blueprint for the system, and it is also a blueprint for the project. A manager can look at it and work out which tasks each team needs to do.

**Decisions that are costly to change**

Here is the simplest way to tell what counts as architecture. Architecture is the set of big structural choices that are expensive to change once they are built. Moving a light switch is cheap. Moving the foundation of a house is not. In software, the foundation includes choices like how the system is split into parts, how those parts talk to each other, and where the data lives.

**The two laws**

Two rules sit under the whole field.

The first law: everything is a trade-off. Every choice gives you something and costs you something. There is no perfect design, only a design that fits your needs better than the others.

The second law: why matters more than how. Anyone can copy how a system is built. But if you don't know why it was built that way, you can't tell when the reason no longer holds. Then you either keep a bad choice too long, or you break a good one by accident.

**Architecture versus design**

People often compare architecture with application design. Application design is about the features: what the system does, and the steps and data behind each feature. Architecture is about the ground the features stand on. It makes sure the features are delivered in a way that is fast enough, safe enough, reliable enough, and easy enough to change. Those "how well" needs are called non-functional requirements. Architects also call them architectural characteristics.

**Five ways to draw the line**

Experts don't fully agree on where architecture ends. There are five common views, and each one adds something.

One: architecture is the big-picture structure. The system is a set of components, plus connectors that show how those components work together.

Two: architecture is "the important stuff, whatever that is." The architect should focus on the decisions with the biggest effect on the system and on the people who depend on it.

Three: architecture is whatever you must understand to see how the system fits into its surroundings.

Four: architecture is whatever people think is hard to change. Those are the decisions that have to be right the first time. And if someone finds a way to make a decision easy to undo, it stops being architecture.

Five: architecture is a set of decisions, not just a set of diagrams. It includes the reasons behind each structure. This idea led to a lot of research on how to capture and keep that knowledge.

In the end, there is no sharp line between requirements, architecture, and design. They form one chain, from high-level intentions down to small details.

**Where the idea came from**

People first compared software to building architecture in the late 1960s. Edsger Dijkstra in 1968, and David Parnas in the early 1970s, argued that the structure of a program matters, and that getting it right is critical. Early attempts to describe an architecture were loose sketches of boxes and lines. The term "software architecture" only caught on in the 1990s. In 1996, Mary Shaw and David Garlan of Carnegie Mellon wrote a key book that gave the field its basic words: components, connectors, and styles. The first formal standard, IEEE 1471, came in 2000, and it later became the international standard ISO/IEC/IEEE 42010. Its 2011 version says a system includes not just hardware and software, but also people, processes, buildings, and materials.

**Why it's worth the effort**

A good architecture is a picture of a complex system that a human mind can actually hold. That brings real benefits. You can test whether a system will meet people's needs before you build it, which saves money and lowers risk. You can reuse proven parts and decisions in other systems. You get the early, high-impact choices right, which keeps schedules and budgets on track. And you can talk about a design with the people who will pay for it and use it, while changes are still cheap.

Chapter 2: The Hidden Forces That Shape a System

**Quality drives architecture**

Older design methods were driven by features, and by the flow of data through the system. Today's insight is different. The architecture of a system is shaped most by its quality attributes. People call them the "ilities," because so many of them end that way: reliability, availability, security, usability, maintainability, extensibility, backward compatibility, fault tolerance, and more. They are also called non-functional requirements.

Here is what a few of them mean. Availability: the system is up when people need it. Fault tolerance: it keeps working when one part fails. Scalability: it can handle more users or more data. Maintainability: it is easy to fix and improve. Extensibility: it is easy to add new features. Interoperability: it can work with other systems. Deployability: new versions are easy to release.

**From business goals to "ilities"**

A key job of the architect is to match these qualities to the goals of the business. Some examples follow.

If the business wants happy customers, the system needs availability, fault tolerance, security, testability, recoverability, agility, and performance.

If the business plans to merge with or buy other companies, the system needs extensibility, scalability, adaptability, and interoperability.

If money and time are tight, the system needs feasibility and simplicity.

If the business wants to ship faster than its rivals, the system needs maintainability, testability, and deployability.

You can't max out every quality at once, because each one costs something. So the architect ranks them, picks the few that matter most, and designs the parts around those.

**Many people, many concerns**

A system serves many people at once: owners, managers, users, and the people who run it day to day. Each group cares about different things. The owner cares about cost. The user cares about speed and ease. The operator cares about uptime. Balancing these concerns, and showing that each one is handled, is a core part of the job. That's why architecture draws on many fields at once.

**Separate the concerns**

The standard way to tame this complexity is to separate the concerns. Instead of one giant diagram, the architect describes the system from several points of view. Each one is called a view, and each view answers one group's questions. Three views are common. A static view shows how the code is organized. A dynamic view shows what the system does while it runs. A deployment view shows which machines each part runs on. A well-known set of views is called the "four plus one" view model.

**Conceptual integrity: one vision**

In 1975, in his book The Mythical Man-Month, Fred Brooks named an idea he called conceptual integrity. A system should feel like it came from one mind, with one clear vision of what it does and how it does it. That vision should be kept separate from the code that carries it out. The architect is the keeper of the vision. Each time something new is added, the architect checks that it fits.

**Conway's Law: systems copy the teams that build them**

In 1967, a programmer named Melvin Conway noticed something. Organizations that design systems end up with designs that copy their own lines of communication. If three separate teams build one product, it tends to end up with three main parts, which talk to each other the way the teams do. Fred Brooks spread the idea in his book, and he called it Conway's Law. The lesson: you can't design the system without thinking about the teams.

**Connections tie parts together**

One more rule. When one part calls another and waits for the answer, that's called synchronous communication. It ties the two parts together. If the second part is slow, the first one is slow. If the second part goes down, the first one is stuck. So parts that talk this way must share the same characteristics, such as the same need for speed and uptime.

Chapter 3: Shapes, Styles, and Patterns

**Two big families**

Almost every architecture falls into one of two families. A monolith is built and released as one single unit. A distributed architecture is split into separate parts that run on their own and talk to each other over a network. Each family has its own sub-types.

**Styles: the overall layout**

An architecture style is the overall layout of a system. It says what kinds of parts there are, how they're arranged, how they interact, and what rules limit those interactions. It is the most zoomed-out level of organization. Here are four common styles.

Layered architecture stacks the system in layers, like a cake. Each layer only talks to the layers next to it. For example, the screens sit on top, the business rules sit in the middle, and the data sits at the bottom.

Microservices split the system into many small services. Each one does one job, and each one can be released on its own.

In event-driven architecture, some parts announce events, such as "order placed," and other parts react to them. The part that makes the announcement doesn't need to know who's listening.

Hexagonal architecture puts the core logic in the middle. It connects that core to the outside world, such as databases, screens, and other services, only through fixed ports. You can swap what's plugged into a port without touching the core.

**Patterns: proven fixes for common problems**

An architecture pattern is a reusable, proven solution to a problem that keeps coming up at the level of the whole system. It deals with the overall structure, with how the parts interact, and with the system's qualities. Architecture patterns work at a higher level than design patterns, which solve smaller problems inside the code. The line between a pattern and a style can be blurry.

One example is the circuit breaker. When one service keeps failing, the circuit breaker stops sending it requests for a while, like the breaker in your house that cuts the power before the wires overheat. That way, one failure doesn't drag the whole system down. Another well-known example is Model-View-Controller. It keeps the data, the screen, and the logic that connects them in separate parts.

Architects use other names for standard solutions, too. A tactic is a small, focused move that improves one quality. A reference architecture is a ready-made template for a whole kind of system.

**Splitting the system into parts**

The size of each part can make or break a system. Neal Ford and Mark Richards suggest a repeating cycle for finding the right parts, and the right size for each one. You won't get it right the first time, so you refine as you learn.

First, choose how to split the system at the top. You can split it by technical layer, such as screens, logic, and data. Or you can split it by business area, such as orders, payments, and shipping. Also decide on the smallest part that can be released on its own. This is called a quantum, and the plural is quanta. These choices come early, but you can revisit them later.

Second, name the first set of components, using that split.

Third, assign each requirement to a component.

Fourth, check each component's role, so each job is clear and no two parts do the same thing.

Fifth, check the architectural characteristics, such as scalability, fault tolerance, and maintainability.

Sixth, reshape the components based on feedback from the developers. Then go around again.

This cycle is a general framework, and you can adapt it to your own field.

**Practice and pictures**

Teams can practice all this with an exercise called an architectural kata. Each team gets a problem, picks out and ranks the qualities that matter most, and then models the components to fit. To draw the result, a team can use the C4 model. It's a simple way to sketch an architecture at a few zoom levels, with just enough detail, and no more.

Chapter 4: Deciding, Remembering, and Fighting Decay

**The four core activities**

Architecture work has four core activities. Teams repeat them, at the start of a project and for as long as the system lives.

Analysis: understand the world the system will live in, and work out what it needs. The inputs come from many people. They include what the system must do, and how well it must run: how reliable, how secure, and how fast. They include how easy it must be to maintain. And they include the business, legal, and money pressures that may change over time. The output is the short list of requirements that truly shape the architecture. These are called architecturally significant requirements.

Synthesis, also called design: create the architecture, and keep improving it, based on those requirements, the current design, and the results of any reviews.

Evaluation: check how well the design meets the requirements. This can happen at any time: before a decision, partway through, after the design is done, or after the system is built. One formal method is called ATAM, the Architecture Tradeoff Analysis Method.

Evolution: keep the architecture fit as needs and surroundings change. Because the architecture is the system's foundation, changing it touches everything. So evolution means adding new features while keeping the old ones working.

**The work behind the work**

Three supporting activities run through all four.

Knowledge management and communication. Architects don't work alone. Much of what they need to know lives only in people's heads. So they search for proven patterns, build prototypes, ask experienced people, study similar systems, and write down what they learn, for example on a wiki. A gap in knowledge can lead straight to a wrong design.

Design reasoning and decision-making. This means framing the problem, finding the options, and weighing the trade-offs before choosing.

Documentation. This means recording the design, often in several views, along with the reasons behind it.

**How to make a decision**

Making an architecture decision has four steps. Gather enough of the right information. Justify the choice. Write down the decision and the reasons for it. Then tell the right people.

**Two traps**

Two common mistakes, called anti-patterns, tend to show up one after the other. Fixing one can lead you into the next.

The first trap is fear. The architect puts off a decision because they're afraid of getting it wrong. The fix is to work closely with the developers, and to adjust choices based on their feedback. Make each decision at the "last responsible moment." That means waiting until you have enough information to justify it, but not so long that the team stalls. Waiting too long has its own name: analysis paralysis.

The second trap is forgotten decisions. A decision gets made, but it isn't written down, or nobody understands it, so the same argument happens again and again. This often happens when decisions live in email. The fix is an Architecture Decision Record. It's one record per decision, with both the technical reasons and the business reasons, such as cost, happy users, and time to market. It lives in one shared place, such as a wiki. Emails then just say what changed, go only to the people who need to know, and link to the record. That way there's always one up-to-date source of truth. And if a decision gives no real business value, or the business doesn't agree with it, it may need a second look.

**Architecture and agile**

Some people, especially fans of agile development, worry that architecture means too much "big design up front": planning everything before building anything. Several methods try to balance the two. One agile method, called DSDM, has a "Foundations" phase, where the team lays down just enough architecture to start.

**Erosion: how good designs decay**

Architectures tend to grow more complex over time. Erosion is the slowly growing gap between the architecture you planned and the one that's actually in the code. Dewayne Perry and Alexander Wolf first pointed it out in 1992. It happens when people break the architecture's rules, when shortcuts pile up as technical debt, and when knowledge simply vanishes as people forget or leave.

A famous case is the Mozilla web browser, built by Netscape. Its code was complex, and its design was poor from the start. Constant changes made it harder and harder to maintain, until Netscape spent two years rebuilding it.

Erosion slows teams down, makes every change cost more, and lowers quality. To catch it, teams use automated checks that compare the code with the planned architecture, along with tools that analyze the code. To prevent it, they enforce the architecture's rules, review each other's code, and run automated tests. To repair it, they refactor, redesign, and update the documents. Architects can also use fitness functions: checks, usually automated, that run again and again to confirm the architecture still has the qualities it needs.

**Recovery: finding a lost architecture**

Sometimes the documents are out of date, and the code has drifted away from the plan. Architecture recovery, also called reverse engineering, rebuilds a picture of the real architecture from the code and from whatever documents exist. It often uses tools that study the code without running it. Only then can a team make good decisions about what to fix.
