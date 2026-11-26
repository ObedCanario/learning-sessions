# Structured Analysis and Structured Design, Made Plain
# Source: Wikipedia, "Structured analysis" (CC BY-SA 4.0), plain-English version supplied by the user (2026-11-25).
# Kept intact except: headings written as bold lines, the two tables written as spoken lists,
# figure callouts without the '>' marker, and notes addressed to the user left out.

Chapter 1: The Big Picture and Where It Came From

**0. The big picture first**

**🔧 First principles.** A business already does its work somehow: people take orders, fill out forms, pass papers around. One day it wants a computer to do some of that work. But a computer can't guess. Before anyone builds anything, someone has to describe exactly what the work is: what comes in, what happens to it, and what goes out. Structured analysis is a careful way of writing that description. Structured design is a careful way of turning the description into a plan for the actual program.

**🍳 Analogy.** Picture a busy restaurant that runs on paper tickets. The owner wants a computer system to run orders. Before a programmer writes any code, someone stands in the kitchen and maps how an order travels: from the customer, to the waiter, to the cook, to the plate, to the bill. That map is the analysis. The blueprint for the software is the design.

**1. What structured analysis and structured design are**

In software engineering, **structured analysis (SA)** and **structured design (SD)** are methods. They help you do two jobs:
1. Analyze business requirements, meaning figure out what the business actually needs.
2. Develop specifications, meaning precise written instructions, for turning the business's way of working into three things:
   - computer programs (the software);
   - hardware configurations (which machines are needed, and how they're set up);
   - related manual procedures (the steps people still do by hand around the computer).

**🍳 Analogy.** For the restaurant, that means: the ordering app (program), the tablets and kitchen printer (hardware), and the rule "the waiter checks the ticket before sending it" (manual procedure).

Structured analysis and design techniques are basic tools of **systems analysis**, the job of studying how a system works and what it needs. They grew out of the "classical" systems analysis of the 1960s and 1970s.

**🖼️ Figure: "Example of a structured analysis approach."** This is the article's opening picture. Its caption only says it is an example of the approach. From the rest of the article, a picture like this shows a system broken into processes and data, with the big picture splitting into smaller and smaller parts.

**2. History: where these methods came from**

**🔧 First principles.** Methods appear when there's a problem. Here, the problem was that software was getting big and messy, and nobody had agreed rules for designing it well.

Structured analysis belongs to a family of "structured methods" for analysis, design, and programming. They were developed from the 1960s to the 1980s to deal with problems in making software:
- Most business programming was done in the languages COBOL and Fortran, and later C and BASIC.
- There was little guidance on how to design and program well.
- There were no standard ways to write down requirements (what's needed) and designs (how to build it).
- Systems kept getting bigger and more complex, so building them kept getting harder.

**🍳 Analogy.** Imagine every restaurant kitchen inventing its own way to write tickets, with no shared format. It works for a food truck. In a 500-seat hotel kitchen, it's chaos. Structured methods were the shared ticket format.

From the late 1960s, structured methods appeared one after another:

1967: Structured programming, with the paper "Go To Statement Considered Harmful." By Edsger Dijkstra.

1971: Stepwise design. By Niklaus Wirth.

1972: The Nassi–Shneiderman diagram.

1974: The Warnier/Orr diagram, from *Logical Construction of Programs*.

1974: HIPO: "hierarchy, input, process, output" (the article notes it should really be read as output, input, process). By IBM.

About 1975: Structured design. By Larry Constantine, Ed Yourdon, and Wayne Stevens.

About 1975: Jackson structured programming. By Michael A. Jackson.

About 1978: Structured analysis. By Tom DeMarco, Edward Yourdon, Gane & Sarson, and McMenamin & Palmer.

Structured analysis and design technique (SADT). By Douglas T. Ross.

The Yourdon structured method. By Edward Yourdon.

1978: The book *Structured Analysis and System Specification*. By Tom DeMarco.

1983: The structured systems analysis and design method (SSADM), first presented. By the UK Office of Government Commerce.

Essential Systems Analysis. By Stephen M. McMenamin and John F. Palmer.

1985: IDEF0, based on SADT. By Douglas T. Ross.

1988: Hatley–Pirbhai modeling, from *Strategies for Real-Time System Specification*. By Derek J. Hatley and Imtiaz A. Pirbhai.

1989: *Modern Structured Analysis*, written after Essential Systems Analysis. By Edward Yourdon.

About 1990: Information technology engineering, popularized by James Martin. By Finkelstein.

David C. Hay (1999) said information engineering grew logically out of the 1970s structured techniques. The chain went:

**structured programming → structured design → structured systems analysis.**

All of these used diagrams, such as structure charts and data-flow diagrams, to help people communicate and to keep the work disciplined. In the 1980s, software tools appeared that drew these diagrams automatically and kept track of the items in a data dictionary. Following the example of CAD/CAM (computer-aided design and manufacturing, used in engineering), these tools were called **CASE**: computer-aided software engineering.

**🔧 First principles on the chain.** People first learned to write a single program cleanly (programming). Then they learned to arrange many program pieces cleanly (design). Then they learned to describe the whole business need cleanly before building anything (analysis). Each step zooms out from the one before.

Chapter 2: Breaking a System Down

**3. What structured analysis tries to do**

Structured analysis became popular in the 1980s. The article says it is still used today, though that claim is marked "citation needed," meaning no source backs it up yet.

**Its core job:** take the idea of the system, or a real-world situation, and translate it into **data** terms and **control** terms. These are drawn as **data-flow diagrams**.
- **Data** = information: an order, a price, a name.
- **Control** = signals that tell parts of the system *when* or *whether* to act: "start," "stop," "order is ready."

In these diagrams, each process (a step that does work) is drawn as a **bubble**, and stored information sits in a **data store**.

**A known problem:** following data and control as they go from a bubble, to a data store, to another bubble can get hard to track. And the number of bubbles can keep growing.

**🍳 Analogy.** Draw every step of the kitchen as a circle: "take order," "cook," "plate," "bill." Draw the fridge and the order spike as storage boxes. Now trace one burger from circle to fridge to circle to spike. With 5 circles it's easy. With 80, it's spaghetti.

**One way to build the diagram**

1. **Start from outside events.** List the things in the outside world that the system must react to.
   *🍳 A customer orders. A supplier delivers. A customer pays.*
2. **Give each event its own bubble.** Each bubble is the process that responds to that event.
3. **Connect the bubbles that need to work together.** Keep going until the whole system is described.
4. **Group bubbles into bigger bubbles.** This cuts down complexity.
   *🍳 "Take order," "send to kitchen," and "confirm order" can all fold into one bigger bubble called "Ordering."*

Two supporting documents are needed:
- **Data dictionaries** describe the data flows and command flows. They say exactly what each piece of information is.
- **Process specifications** record what each process does to the information: the transaction or transformation it performs.

**🔧 First principles.** A diagram shows *that* an order flows from A to B. It can't show what an order *contains* (that's the dictionary's job) or exactly *what B does with it* (that's the process spec's job). You need all three to describe a system fully.

**How SA and SD are drawn, and who drew them**

SA and SD are shown with three kinds of diagram:
- **structure charts** (how a program's parts are arranged);
- **data-flow diagrams** (how information moves);
- **data-model diagrams** (how stored information is organized).

There were many versions of these. They were developed by Tom DeMarco, Ken Orr, Larry Constantine, Vaughn Frick, Ed Yourdon, Steven Ward, Peter Chen, and others.

These techniques were then bundled into full published **methodologies**, step-by-step recipes for building a system from start to finish. Examples:
- Structured systems analysis and design method (SSADM)
- Profitable information by design (PRIDE)
- Nastec structured analysis & design
- SDM/70
- Spectrum structured system development methodology

**4. One way of zooming: the "single abstraction mechanism"**

**🔧 First principles: what "abstraction" means.** To abstract is to hide detail so you can think about the big picture. "Make dinner" is an abstraction. "Chop onions, heat pan, add oil" is the detail inside it. An **abstraction mechanism** is the *method* you use to hide or reveal detail.

Structured analysis usually builds a **hierarchy**, a top-to-bottom tree, using **only one abstraction mechanism**: breaking a function (a job the system does) into smaller functions.

**🍳 Analogy.** There's only one way to zoom in on the restaurant: "What job is this, and what smaller jobs make it up?" "Run the restaurant" → "Serve food" → "Cook" → "Grill the burger." You never switch to a different kind of view, like "Who is this person?" or "What does this screen look like?" It's always "job inside job."

How the method works:
- It can use **IDEF** (see figure below).
- It is **process driven**: it starts with the work being done, not with things or screens.
- It starts with a **purpose** (why we're modeling this) and a **viewpoint** (whose eyes we're looking through).
- It finds the **overall function**, then keeps dividing functions into smaller ones, one step at a time.
- At each split it keeps track of four things for every function:
  - **inputs**: what comes in to be worked on;
  - **outputs**: what comes out;
  - **controls**: rules or signals that govern the work;
  - **mechanisms**: the people or tools that do the work.
  Keeping these lets you improve the processes.

*🍳 For "Grill the burger": input = raw patty; output = cooked patty; control = the ticket saying "medium"; mechanism = the cook and the grill.*

This is also called the **functional decomposition** approach ("decompose" = break into parts). It focuses on two things:
- **cohesion within functions**: everything inside one function belongs together;
- **coupling between functions**: how much separate functions depend on each other.

Paying attention to both leads to well-organized ("structured") data.

**🖼️ Figure: "Structured analysis example."** The article says this method "can employ IDEF (see figure)," so this picture is an IDEF-style example. In IDEF0, each function is a box. Inputs enter from the left, outputs leave on the right, controls come in from the top, and mechanisms come in from the bottom. A big box is then broken into a few smaller boxes, usually set out like a staircase, with arrows passing between them.

**What this approach shows well, and what it doesn't**

- Functional decomposition **describes the process without spelling out the system's behavior**. It shows what jobs get done, not how the system acts and reacts moment to moment.
- It **sets the system's structure as a list of required functions**. The system is shaped like its jobs.
- It identifies **inputs and outputs** as they relate to each activity.
- **Why it's popular:** it's intuitive. It communicates high-level processes and ideas clearly, whether for one system or a whole enterprise (a big organization with many systems).
- **Its weak spot:** it is unclear how *objects* would support these *functions* in object-oriented development, which is the most common style in the industry.

**🔧 First principles: functions vs. objects.** Structured analysis organizes everything around *jobs* ("cook," "bill"). Object-oriented development organizes everything around *things* that hold their own data and abilities ("an Order," "a Table," "a Cook"). The two cut the world in different directions, so it's hard to map one onto the other.

*🍳 Structured analysis files the kitchen by task: the grilling station, the billing station. Object-oriented thinking files it by thing: each Order carries its own items, status, and price, and knows how to total itself.*

**The contrast with UML.** IDEF is process driven with one abstraction mechanism. **UML** (Unified Modeling Language, the standard diagram language for object-oriented design) is different:
- it is **interface driven**: it starts from how parts connect and talk to each other;
- it has **multiple abstraction mechanisms**: several different ways to zoom and view a system.

That makes UML useful for describing **service-oriented architectures (SOAs)**: systems built from separate services that talk to each other through agreed connections.

*🍳 An SOA restaurant runs as separate counters (orders, kitchen, payments), each with a service window. What matters most is the window: what you can hand through it and what you get back. UML is built to describe windows. IDEF is built to describe jobs.*

Chapter 3: Follow the Data

**5. The approach: follow the data**

Structured analysis looks at a system **from the point of view of the data flowing through it.**

- What the system *does* is described as **processes that transform data flows**. Data comes in, gets changed, and goes out.
- It uses **information hiding** through **successive decomposition**, also called **top-down** analysis. You look at the top level first, then open up one part at a time.
- **Why:** this keeps your attention on the details that matter right now, and avoids confusion from looking at details that don't.
- **The trade-off:** as the detail goes up, the breadth goes down. Each deeper diagram shows more about a smaller slice.

*🍳 A map app: zoomed out, you see the whole country with no streets. Zoomed in, you see every street, but only of one neighborhood. You can't see both at once, and you don't need to.*

**What you end up with:** a set of linked graphical diagrams, process descriptions, and data definitions. Together they describe the **transformations** that must happen and the **data** needed to meet the system's **functional requirements** (the things it must be able to do).

**🖼️ Figure: "The structured analysis approach develops perspectives on both process objects and data objects."** This picture shows the approach as two connected sides. One side is **processes**: what gets done, shown in diagrams and process specs. The other side is **data**: what gets used, defined in the data dictionary. The article introduces DeMarco's four objects with "(see figure)," so the picture shows how those four fit together.

**DeMarco's approach: the four pieces**

Tom DeMarco's approach is made of four objects:
1. **Context diagram**
2. **Data-flow diagram**
3. **Process specifications**
4. **Data dictionary**

**Data-flow diagrams (DFDs) are "directed graphs."**

*🔧 A graph here means dots connected by lines. "Directed" means each line has an arrow: it goes one way.*

- The **arcs** (arrows) represent **data**.
- The **nodes** (circles, or "bubbles") represent **processes** that transform the data.

**Breaking it down:**
- Any process can be opened up into a more detailed DFD. That diagram shows the **subprocesses** and the data flowing between them.
- Those subprocesses can be opened up again with another set of DFDs, and so on, until each one's job is easy to understand.
- A process that doesn't need breaking down any further is called a **functional primitive**: the smallest useful piece.
- Each functional primitive is described by a **process specification**, also called a **mini-spec**. A mini-spec can be written as:
  - **pseudo-code**: program-like steps in plain words, not real code;
  - **flowcharts**: boxes and arrows showing steps and decisions;
  - **structured English**: plain English with strict, simple rules ("IF the steak is rare THEN grill 3 minutes").

*🍳 "Cook the order" opens into "grill," "fry," "plate." "Grill" opens into "check temperature," "place patty," "flip," "remove." "Flip" is so simple that opening it further is pointless. That makes it a functional primitive, and it gets a mini-spec: "After 3 minutes, flip once."*

- Altogether, the DFDs model the system's structure as a **network of connected processes**, built up from functional primitives.

**The data dictionary:**
- It is a set of entries (definitions) for **data flows, data elements, files, and databases**.
- The entries are organized **top-down**, from big items to small ones.
- Entries can be referenced by other entries, and from the data-flow diagrams.

*🍳 Dictionary entry: "Order = table number + list of items + time placed." Then: "Item = dish name + quantity + special request." The second entry is used inside the first, and the arrow labeled "Order" on the DFD points to this entry.*

**6. The context diagram: the system from the outside**

**🖼️ Figure: "Example of a system context diagram."** One box sits in the middle: the system, with nothing shown inside it. Around it are the outside people and systems it deals with, joined to the middle box by arrows labeled with what flows in or out.

**What it is:** a context diagram shows the **actors outside a system** that could interact with it. "Actors" are people, organizations, or other systems.

- It is the **highest-level view** of a system, similar to a **block diagram** (a simple boxes-and-lines picture).
- It shows the whole system, which may or may not be software, along with its **inputs and outputs** to and from **external factors**.

According to Kossiakoff (2003), this diagram usually "pictures the system at the center, with no details of its interior structure, surrounded by all its interacting systems, environment and activities."

The **goal** is to focus attention on the **outside** factors and events you need to consider to build a **complete set of system requirements and constraints**. Requirements are what it must do. Constraints are the limits it must work within.

- Context diagrams are related to data-flow diagrams. They show the interactions between the system and the other actors it is designed to deal with.
- They help you understand the setting the system will fit into, as part of software engineering.

**🔧 First principles.** Before you study the inside of anything, list everything that touches it from outside. Miss one outside actor and you miss a whole set of requirements.

*🍳 The restaurant as one sealed box. Around it: Customers (send orders and payments, get food and receipts), Suppliers (deliver ingredients, receive purchase orders), the Bank (receives card payments), the Health Inspector (receives reports). Forget the Health Inspector, and nobody builds the report feature.*

**7. The data dictionary: the database's table of contents**

**🖼️ Figure: "Entity–relationship diagram, essential for the design of database tables, extracts, and metadata."** An entity–relationship diagram draws the *things* a database stores (entities, like Customer or Order) as boxes. Lines between the boxes show how those things relate ("a Customer places many Orders"). The caption says it is essential for designing **database tables** (where data is stored), **extracts** (pulled-out copies of data), and **metadata** (data about data).

**What it is:** a **data dictionary**, or database dictionary, is a file that defines how a database is basically organized.

It contains:
- a list of all **files** in the database;
- the **number of records** in each file (*a record is one entry, like one customer*);
- the **names and types** of each **data field** (*a field is one slot in a record, like "phone number," and its type says whether it holds text, a number, a date, and so on*).

Also:
- Most **database management systems** (the software that runs a database) **hide** the data dictionary from users, so nobody accidentally destroys it.
- It holds **no actual data**, only **bookkeeping** information for managing the database.
- **Yet without it, the database system can't get at the data at all.**

*🍳 It's like the kitchen's labeling system: which shelf holds what, how many containers are on each shelf, and what each label means. It contains no food. But without it, nobody can find anything, so it's useless to have the food at all.*

**The data dictionary as a document for people.** Database users and developers benefit from an **authoritative** (official, trusted) data dictionary *document* that catalogs the organization, contents, and conventions (agreed habits and rules) of one or more databases. It usually includes:
- the names and descriptions of the **tables** and **fields** in each database;
- extra details, such as the **type** and **length** of each data element.

Some more points:
- There's **no universal standard** for how detailed it should be.
- It is mainly a summary of **metadata** about the database's **structure**, not the data itself.
- It may also explain how data elements are **encoded** (*for example, "M = medium, W = well done"*).
- **Main benefit:** a well-made one keeps things **consistent** across a complex database, or across a large group of **federated databases** (separate databases that work together as one).

*🍳 A chain of 50 restaurants. If one kitchen writes "MED," another "M," and another "medium," the head office can't combine the reports. One shared dictionary fixes that.*

Chapter 4: Data Flows, Structure Charts, and Good Modules

**8. Data-flow diagrams: how information moves**

**🖼️ Figure: "Data-flow diagram example."** A typical DFD shows processes as circles or rounded boxes, data stores as open-ended boxes or parallel lines, outside actors as squares, and arrows labeled with the data that moves between them.

**What it is:** a **data-flow diagram (DFD)** is a picture of how data "flows" through an information system.

- **How it differs from a system flowchart:** a DFD shows data moving through **processes**. A system flowchart shows it moving through **computer hardware**.
  *🍳 A DFD says "the order goes from Taking Orders to Cooking." A hardware flowchart says "the order goes from the tablet to the kitchen printer."*
- **Who invented it:** Larry Constantine, who also developed structured design. He based it on Martin and Estrin's "data-flow graph" model of computation.

**The usual order of work:**
1. First, draw a **system context diagram** showing how the system interacts with outside entities.
2. The DFD then shows how the system is **divided into smaller parts**, and highlights the **data flowing between** those parts.
3. This context-level DFD is then "**exploded**": opened up to show more detail of the system being modeled.

**Why DFDs matter:**
- They are one of the **three essential perspectives** of SSADM. *(The article doesn't name the other two here.)*
- The project's **sponsor** (who pays for it) and its **end users** (who will use it) need to be briefed and consulted at every stage of the system's development.
- With a DFD, users can **see**:
  - how the system will operate;
  - what it will accomplish;
  - how it will be implemented (built).
- You can draw the **old system's** DFDs and the **new system's** DFDs, then compare them, to build a more efficient system.
- DFDs give end users a concrete sense of where the data they enter ends up affecting the whole system, "from order to dispatch to recook." *(That's the article's phrase. It traces data from the first order, through sending it out, to redoing it, such as a dish sent back to the kitchen.)*
- **How any system is developed can be worked out from a DFD.**

*🍳 The waiter types "no onions." The DFD lets the waiter see that note travel: to the kitchen screen, to the cook, onto the bill, into the "complaints" store if it goes wrong, and back to "recook." Now the waiter understands why typing it correctly matters.*

**9. Structure charts: the program's family tree**

**🖼️ Figure: "A configuration system structure chart."** A tree of boxes. One box at the top stands for the whole system. Below it are branches of smaller boxes, down to the lowest pieces that can still be managed.

**What it is:** a **structure chart (SC)** shows how a system's configuration breaks down into its **lowest manageable levels**.

- It is used in **structured programming** to arrange the program's **modules** (self-contained pieces of a program) in a **tree** shape.
- Each module is a **box** with the module's name in it.
- The tree shows how the modules relate to each other.

**How it's used:**
- In structured analysis, structure charts lay out the **high-level design**, or **architecture**, of a computer program.
- As a design tool, they help the programmer **divide and conquer** a large software problem. That means repeatedly breaking it into parts **small enough for a human brain to understand**.
- This process is called **top-down design**, or **functional decomposition**.
- The article's own comparison: programmers use a structure chart the way an **architect uses a blueprint** to build a house.
- **During design**, the chart is drawn and used as a shared language between the **client** and the various **software designers**.
- **During building** (implementation), it is constantly referred to as the **master plan**.

**🔧 First principles: why "small enough for a human brain"?** People can only hold a few things in mind at once. Any problem bigger than that has to be cut into pieces that each fit in your head. The tree is the record of those cuts.

*🍳 Top box: "Restaurant System." Below it: "Ordering," "Kitchen," "Billing." Below "Billing": "Total the bill," "Add tip," "Take payment." Each box can be handed to one programmer, who knows exactly where their piece fits.*

**Structure chart vs. DFD.** A DFD shows how *data moves* between processes, like a river map. A structure chart shows which *program part is in charge of* which, like a family tree or a company org chart.

**10. Structured design: building with good modules**

**What it is:** **structured design (SD)** is about creating **modules** and putting them together into a "**module hierarchy**", a tree of modules where higher ones call on lower ones.

To design the best module structure and **interfaces** (the points where modules connect and pass things to each other), two principles are crucial.

**Principle 1: Cohesion**

Cohesion is "concerned with the grouping of functionally related processes into a particular module."

*Plain version:* put things that do related work **together** in the same module.

*🍳 The pastry station holds everything for desserts: the oven, the mixer, the sugar. High cohesion. A station that makes desserts, fixes the printer, and does payroll has low cohesion, and nobody knows what it's for.*

**Principle 2: Coupling**

Coupling relates to "the flow of information or parameters passed between modules. Optimal coupling reduces the interfaces of modules and the resulting complexity of the software."

*Plain version:* coupling is how much modules have to pass back and forth and depend on each other. Good design keeps these connections **few and simple**, which keeps the whole program simpler. (*Parameters are the pieces of information handed to a module when you ask it to do something.*)

*🍳 The grill cook needs only a ticket: "burger, medium." That's low coupling. If the grill cook had to check the bar's stock, the cashier's drawer, and the host's seating chart before cooking, that's high coupling. A change anywhere would break the grill.*

**🔧 First principles: why these two together?** Strong cohesion + loose coupling means each part makes sense on its own, and changing one part rarely breaks another. That's the goal of all good design.

**Where it came from, and Page-Jones's version**

- Structured design was developed by **Larry Constantine** in the **late 1960s**, then refined and published with collaborators in the **1970s**.
- **Page-Jones (1980)** proposed his own approach, made of three main objects:
  1. **structure charts**
  2. **module specifications**
  3. **data dictionary**

How they fit:
- The **structure chart** shows "the module hierarchy or calling sequence relationship of modules": which modules call (ask for help from) which, and in what order.
- Every module on the chart gets its own **module specification**, written in **pseudo-code** or a **program design language** (a semi-formal language for describing a program before writing real code).
- The **data dictionary** is like the one in structured analysis.
- **The payoff:** at this point in the software development lifecycle, once analysis and design are done, it becomes possible to **automatically generate**:
  - **data type declarations** (the code that defines what kind of data each item is);
  - **procedure or subroutine templates** (empty starter shells for each module's code).

*🍳 Once the menu, recipes, and station plan are fully written down, a machine can print every station's labeled, empty prep containers for you. The cooks just fill them in.*

**11. How it all fits together**

Context diagram. What it answers: who and what is outside, and what crosses the edge? Restaurant version: the restaurant as one box, with customers, suppliers, and the bank around it.

Data-flow diagram. What it answers: how does information move inside? Restaurant version: the order travels from waiter to cook to plate to bill.

Process spec, or mini-spec. What it answers: what exactly does the smallest step do? Restaurant version: "After 3 minutes, flip once."

Data dictionary. What it answers: what exactly is each piece of data? Restaurant version: "Order = table + items + time."

Structure chart. What it answers: how is the program split into modules, and who calls whom? Restaurant version: Restaurant System, then Ordering, Kitchen, and Billing.

Module spec. What it answers: what does each module do? Restaurant version: each station's written instructions.

Cohesion. What it answers: does each module hold related work only? Restaurant version: the pastry station does only desserts.

Coupling. What it answers: do modules depend on each other as little as possible? Restaurant version: the grill needs only the ticket.

**The whole story in one line:** start outside (context), follow the data inward (DFDs), break steps down until they're simple (functional primitives and mini-specs), define every piece of data (dictionary), then arrange the program as a tree of tidy, loosely connected modules (structure charts plus cohesion and coupling).
