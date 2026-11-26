# Structured Analysis and Structured Design, Made Plain (v2)
# Source: Wikipedia, "Structured analysis" (CC BY-SA 4.0), https://en.wikipedia.org/wiki/Structured_analysis
# Rewritten for this show (2026-11-26) from the user's plain-English version (structured-analysis-original.md),
# following procedures/learning-series.md. The diagrams are now walked through with one pizza-shop example.
# Cut as non-essential: the full timeline (Nassi–Shneiderman, Warnier/Orr, HIPO, Hatley–Pirbhai,
# information engineering, and more), and the list of published methodologies other than SSADM.

Chapter 1: Describe the Work Before You Build It

**What structured analysis and structured design are**

A business already does its work somehow. People take orders, fill out forms, and pass papers around. One day, the business wants a computer to do some of that work. But a computer can't guess. Before anyone builds anything, someone has to describe exactly what the work is: what comes in, what happens to it, and what goes out.

Structured analysis is a careful way of writing that description. Structured design is a careful way of turning the description into a plan for the actual program. Together, they help with two jobs. The first job is to work out what the business really needs. The second is to write precise instructions, called specifications, for turning the business's way of working into a computer system.

**A system is more than software**

Those specifications cover three things, not one. The first is the computer programs, the software itself. The second is the hardware: which machines are needed, and how they're set up. The third is the manual procedures: the steps that people still do by hand around the computer.

Picture a pizza shop that wants to take orders through an app. The program is the ordering app. The hardware is the customers' phones, the tablet behind the counter, and the printer in the kitchen. And a manual procedure is a rule like this one: the cook checks each ticket before the pizza goes into the oven. Leave out any one of the three, and the system doesn't work.

These methods are basic tools of systems analysis, the job of studying how a system works and what it needs. They grew out of the classic systems analysis of the 1960s and 1970s.

**Why these methods were invented**

From the 1960s to the 1980s, a family of "structured methods" grew up to solve four problems. Most business programs were written in languages like COBOL and Fortran, and later C and BASIC. There was little guidance on how to design and program well. There was no standard way to write down what a system needed, or how it should be built. And systems kept getting bigger and more complex, so they kept getting harder to build.

Picture a kitchen where every cook invents their own way to write order tickets. In a food truck, that works fine. In a hotel kitchen that feeds five hundred people, it's chaos. The structured methods were the shared ticket format.

**The key names and dates**

The methods arrived one after another. In the late 1960s, Edsger Dijkstra's famous letter, "Go To Statement Considered Harmful," launched structured programming: writing each program in clean, orderly blocks. In 1971, Niklaus Wirth described stepwise design. Around 1975, Larry Constantine, Ed Yourdon, and Wayne Stevens gave us structured design. Around 1978, Tom DeMarco, Ed Yourdon, and others gave us structured analysis, and DeMarco wrote the classic book on it. Douglas Ross created a related method, called SADT, which later became IDEF0. In 1983, the British government introduced a complete method, called SSADM. And in 1989, Yourdon wrote Modern Structured Analysis.

**The chain of ideas**

The writer David Hay said these methods grew out of each other in a chain: first structured programming, then structured design, then structured systems analysis. People first learned to write one program cleanly. Then they learned to arrange many program pieces cleanly. Then they learned to describe the whole business need cleanly, before building anything at all. Each step zooms out from the one before.

All of these methods used diagrams, such as structure charts and data-flow diagrams, to help people talk to each other and to keep the work disciplined. In the 1980s, software tools appeared that drew these diagrams automatically and kept track of every item in a data dictionary. Engineers already had computer-aided design tools for machines and buildings, so these new tools were called CASE tools, short for computer-aided software engineering.

Chapter 2: Breaking a System Down

**Data and control**

Structured analysis became popular in the 1980s. Its core job is to take an idea for a system, or a real-world situation, and translate it into two kinds of things: data, which is information such as an order, a price, or a name, and control, which is a signal telling part of the system when to act, or whether to act at all, such as "start," "stop," or "the order is ready."

Both are drawn in data-flow diagrams, where each process, meaning a step that does work, is drawn as a circle called a bubble, and information that is kept for later sits in a data store. The method has a known weakness: following the data from a bubble, to a store, to another bubble can get difficult to track, and the number of bubbles can keep growing. With five bubbles, the picture is clear. With eighty, it looks like a plate of spaghetti.

**How to build the diagram**

One way to build the diagram has four steps. First, start from outside events: list the things in the outside world that the system must react to. For the pizza shop, a customer places an order, a customer pays, and a supplier delivers flour and cheese. Second, give each event its own bubble, the process that responds to it. Third, connect the bubbles that need to work together, until the whole system is described. Fourth, group small bubbles into bigger ones, to cut down the clutter. For example, "take the order," "confirm the order," and "send it to the kitchen" can fold into one bigger bubble called "Ordering."

Two documents go with the diagram: a data dictionary, which says exactly what each piece of information contains, and a process specification, which says exactly what each process does with it. The diagram shows that an order flows from one bubble to another, but only the dictionary can say what an order is made of, and only the process specification can say what happens to it next.

Altogether, structured analysis and design use three kinds of diagram: structure charts, which show how a program's parts are arranged; data-flow diagrams, which show how information moves; and data-model diagrams, which show how stored information is organized. These techniques were later bundled into complete, step-by-step recipes for building a system, such as SSADM.

**One way to zoom**

To abstract means to hide detail on purpose, so you can think about the big picture. "Make dinner" is an abstraction, and "chop the onions, heat the pan, add the oil" is the detail hidden inside it. Structured analysis builds a top-to-bottom tree with only one way to zoom: breaking a job into smaller jobs. Run the pizza shop. Inside that, make the pizzas. Inside that, bake the pizza. It never switches to a different kind of view, such as "who is this person?" or "what does this screen look like?" It's always a job inside a job.

The method starts with the work being done, not with things or screens. It begins with a purpose, which is why we're describing the system, and a viewpoint, which is whose eyes we're looking through. Then it finds the overall job and keeps dividing it, tracking four things for each job: inputs, which are what comes in to be worked on; outputs, which are what comes out; controls, which are the rules or signals that govern the work; and mechanisms, which are the people or tools that do it.

**Picture the box diagram**

A diagram style called IDEF0 draws all four on a single box. Picture a box labeled "Bake the pizza." An arrow comes in from the left: the input, a raw pizza. An arrow leaves on the right: the output, a baked pizza. An arrow comes down from the top: the control, the order ticket that says "extra crispy." And an arrow comes up from the bottom: the mechanism, the cook and the oven. Left is what goes in, right is what comes out, the top is the rules, and the bottom is who does the work. Then you can open the box. Inside are three smaller boxes, set out like a staircase: "put it in the oven," "check it at ten minutes," and "take it out and slice it," with an arrow passing from each step to the next.

This approach is called functional decomposition, which means breaking the work down into its jobs. It pays attention to two things: cohesion, meaning everything inside one job belongs together, and coupling, meaning how much separate jobs depend on each other.

**What it shows well, and what it doesn't**

Functional decomposition shows what jobs get done, but not how the system behaves from moment to moment. It shapes the system as a list of required jobs, with the inputs and outputs of each one. It's popular because it's intuitive, and it communicates big processes clearly, for one system or for a whole organization. Its weak spot is object-oriented development, the most common style in the industry, because it's unclear how objects would carry out these jobs.

Structured analysis organizes the world by jobs: take the order, bake, deliver. Object-oriented development organizes it by things that hold their own data and abilities: an Order that knows its own pizzas and can add up its own price, a Customer, a Driver. The two cut the world in different directions, so it's hard to map one onto the other.

UML, the standard diagram language for object-oriented design, works differently from IDEF0. It starts from how parts connect and talk to each other, and it has several ways to zoom, not just one. That makes it useful for describing service-oriented systems, which are built from separate services that talk through agreed connections. Picture the pizza shop run as separate counters for orders, the kitchen, and payments, each with its own service window. In that kind of system, what matters most is the window: what you can hand through it, and what you get back.

Chapter 3: Follow the Data

**Follow the data**

Structured analysis looks at a system from the point of view of the data flowing through it. What the system does is described as processes that change data: data comes in, gets changed, and goes out. It hides detail by breaking things down level by level, which is called top-down analysis. You look at the top level first, and then open up one part at a time, so your attention stays on the details that matter right now. The trade-off is that as the detail goes up, the breadth goes down. It's like a map app. Zoomed out, you see the whole country, but no streets. Zoomed in, you see every street, but only in one neighborhood.

What you end up with is a set of linked diagrams, process descriptions, and data definitions: two halves that fit together, the processes, which are what gets done, and the data, which is what gets used.

**DeMarco's four tools**

Tom DeMarco's approach uses four tools: the context diagram, the data-flow diagram, the process specification, and the data dictionary.

A data-flow diagram is what mathematicians call a directed graph. A graph, here, means dots connected by lines, and directed means each line has an arrow pointing one way. The arrows stand for data, and the dots, drawn as bubbles, stand for processes that change the data.

Any bubble can be opened up into a more detailed diagram of its own, showing the smaller steps inside it and the data passing between them. Those steps can be opened up again, and so on, until each one's job is easy to understand. A step that doesn't need breaking down any further is called a functional primitive, the smallest useful piece. Each one gets a short, precise description, called a mini-spec. A mini-spec can be written as pseudo-code, which is program-like steps in plain words, as a flowchart of boxes and arrows, or in structured English, which is plain English with strict rules. For example: if the pizza is extra crispy, then bake it for two more minutes.

Here's how the opening up works. "Make the pizza" opens into "add the toppings," "bake," and "slice." "Slice" opens into "move it to the board," "cut eight pieces," and "box it." "Cut eight pieces" is so simple that opening it further is pointless, so it's a functional primitive. Its mini-spec might just say: cut the pizza into eight equal slices.

**The data dictionary**

The data dictionary is a set of definitions for every flow of data, every data element, every file, and every database. The entries go from big items to small ones, and they can point to each other. For example: an order is a customer, a list of pizzas, a delivery address, and the time it was placed. And then: a pizza is a size, a crust, and a list of toppings. The second entry is used inside the first, and every arrow labeled "order," on every diagram, points back to that one definition.

**The context diagram: the system from the outside**

A context diagram shows the actors outside a system that could interact with it. Actors can be people, organizations, or other systems. It's the highest-level view of a system: a simple picture of boxes and lines. It shows the whole system, which may or may not be software, with its inputs and outputs to and from the outside world. As one textbook puts it, the system sits at the center, with no details of its inside, surrounded by everything it interacts with.

Picture it for the pizza shop. One box sits in the middle, labeled "Pizza Shop System," with nothing drawn inside it. Around it are four outside actors, each joined to the middle by labeled arrows. The customer sends in orders and payments, and gets back pizzas and receipts. The payment company receives card charges, and sends back approvals or declines. The delivery driver gets addresses, and sends back "delivered." And the supplier gets purchase orders, and sends back flour, cheese, and an invoice.

The goal is to focus attention on the outside events you must consider, so you can build a complete set of requirements, which are the things the system must do, and constraints, which are the limits it must work within.

**The database's table of contents**

A data dictionary can also mean a file that defines how a database is organized. It lists every file in the database, the number of records in each one, and the name and type of each field. A record is one entry, like one customer. A field is one slot in that record, like a phone number, and its type says whether it holds text, a number, or a date. Most database software hides this file from users, so nobody destroys it by accident. It holds no actual data, only bookkeeping. And yet without it, the database can't reach its data at all. It's like the labels in a pantry: the labels contain no food, but without them, nobody can find anything.

**Picture the entity-relationship diagram**

A related picture, called an entity-relationship diagram, is essential for designing database tables. It draws the things a database stores, called entities, as boxes, and the lines between the boxes show how they relate. For the pizza shop, picture three boxes: Customer, Order, and Pizza. A line from Customer to Order says "one customer places many orders." A line from Order to Pizza says "one order contains one or more pizzas." In one glance, you can see how the stored information hangs together.

**A shared document for people**

Developers and users also benefit from an official data dictionary document, which lists the tables and fields in each database, with details like each field's type and length. It may also explain codes, such as "S" for small, "M" for medium, and "L" for large. Its main benefit is consistency. Picture a chain of fifty pizza shops. If one shop writes "LG," another writes "L," and another writes "large," head office can't combine their sales reports. One shared dictionary fixes that.

Chapter 4: Data Flows, Structure Charts, and Good Modules

**Data-flow diagrams: how information moves**

A data-flow diagram is a picture of how data moves through an information system. It's different from a system flowchart: a data-flow diagram shows data moving through processes, while a flowchart shows it moving through hardware. The first says the order goes from "take the order" to "make the pizza." The second says it goes from the customer's phone to the kitchen printer. The idea came from Larry Constantine, who also developed structured design.

The usual order of work has three steps. First, draw a context diagram showing how the system deals with the outside world. Next, draw a data-flow diagram that splits the system into smaller parts, and shows the data flowing between them. Then "explode" it, which means opening each part up to show more detail.

**Picture the data-flow diagram**

A data-flow diagram uses four kinds of shapes. Circles are processes. Open-ended boxes are data stores. Squares are outside actors. And arrows, labeled with the data they carry, show the movement. Now picture one for the pizza shop. Start at the square labeled "Customer." An arrow labeled "order" runs to the first circle, "Take Order." From there, an arrow labeled "card details" runs to a circle called "Check Payment," and an arrow labeled "approved" comes back. "Take Order" saves the order in a store called "Orders," and sends a "pizza ticket" to the circle "Make Pizza." "Make Pizza" sends a "ready" signal to the circle "Deliver," which reads the address from the Orders store, and sends the pizza back out to the Customer square. Trace that loop once with your finger, and you understand the whole business.

**Why data-flow diagrams matter**

In the complete method called SSADM, data flow is one of three essential points of view. The people paying for a project, and the people who will use it, need to be consulted at every stage, and a data-flow diagram lets them see how the system will work, what it will do, and how it will be built. You can draw the old system and the new one, and compare them. And users can see how the data they type in affects the whole system. If a customer types "no olives," the diagram shows that note traveling to the kitchen ticket, onto the receipt, and into the complaints store if the pizza comes out wrong. Now everyone understands why it has to be typed correctly.

**Structure charts: the program's family tree**

A structure chart shows how a system breaks down into its lowest manageable levels. It arranges the program's modules, which are self-contained pieces of a program, in a tree. Each module is a box with its name inside, and the tree shows how the modules relate.

Picture one for the pizza shop. At the top is one box: "Pizza Shop System." Below it are three boxes: "Ordering," "Kitchen," and "Delivery." Below "Ordering" are three more: "Show the Menu," "Build the Cart," and "Take Payment." Each line in the tree means that the box above calls on the box below to do part of its job. Each bottom box is small enough to hand to one programmer, who knows exactly where their piece fits.

Structure charts lay out the high-level design, or architecture, of a program. They help a programmer divide and conquer a large problem, by breaking it again and again into parts small enough for a human brain to understand, which is called top-down design. Programmers use a structure chart the way an architect uses a blueprint: during design, it's a shared language between the client and the designers, and during building, it's the master plan.

So here's how the two pictures differ. A data-flow diagram shows how data moves between processes, like a map of rivers. A structure chart shows which part of the program is in charge of which, like a family tree.

**Structured design: building with good modules**

Structured design is about creating modules, and arranging them into a module hierarchy: a tree where higher modules call on lower ones. To design the best modules, and the best connections between them, called interfaces, two principles matter most.

The first principle is cohesion: put the work that belongs together in the same module. A pizza station that holds the dough, the sauce, and the oven has high cohesion. A station that makes pizzas, fixes the printer, and does the payroll has low cohesion, and nobody knows what it's for.

The second principle is coupling: how much modules have to pass back and forth, and depend on each other. Good design keeps these connections few and simple, which keeps the whole program simpler. The oven cook needs only a ticket: "large, pepperoni, extra crispy." That's low coupling. If the cook had to check the cash drawer, the driver's schedule, and the supplier's invoices before baking, that's high coupling, and a change anywhere would break the kitchen.

Together, strong cohesion and loose coupling mean that each part makes sense on its own, and that changing one part rarely breaks another.

**Where structured design came from**

Larry Constantine developed structured design in the late 1960s, and refined and published it with others in the 1970s. In 1980, Meilir Page-Jones proposed a version with three main tools. The structure chart shows which modules call which, and in what order. Each module on the chart gets its own module specification, written in pseudo-code or in a program design language, a semi-formal way to describe a program before writing the real code. And a data dictionary works like the one in structured analysis.

Then came the payoff. Once the analysis and design were done, a computer could automatically produce the code that defines each kind of data, and an empty starter template for each module. It's like a pizza shop where, once the menu and recipes are fully written down, a machine prints every station's labeled, empty containers, and the cooks just fill them in.

**How it all fits together**

Here are the eight pieces in one place. The context diagram answers: who and what is outside, and what crosses the edge? The data-flow diagram answers: how does information move inside? The mini-spec answers: what exactly does the smallest step do? The data dictionary answers: what exactly is each piece of data? The structure chart answers: how is the program split into modules, and who calls whom? The module specification answers: what does each module do? Cohesion asks: does each module hold only related work? And coupling asks: do the modules depend on each other as little as possible?

So the whole story fits in one line. Start outside with the context diagram, follow the data inward with data-flow diagrams, break each step down until it's simple, define every piece of data, and then arrange the program as a tree of tidy, loosely connected modules.
