
# FAQ

These are frequently asked questions related to Magic and Hyperlambda, and serves as an FAQ for
anything related to Aista, Magic and Hyperlambda. If your question is not answered, you can
send your question to [info@aista.com](mailto:info@aista.com), and we will try to answer you at the best of our abilities.

## What is Aista Magic Cloud?

Aista Magic Cloud, or simply Magic for short, is an open source cloud based software development platform, based upon
artificial intelligence, machine learning, and software development automation. At its core
it is built on top of Hyperlambda, which is a declarative meta programming language, allowing
for the computer to for the most parts automagically assemble your code, in particular backend
code.

This frees up the human software developer to focus on more interesting and demanding tasks,
while the machine can do most of the boring parts automagically.

## What is Aista?

Aista is a privately held company in Cyprus, delivering cloud services and automated software
development services, on top of its own internally developed software development platform
called Aista Magic Cloud. Aista Magic Cloud again is open source, and hosted at GitHub
for those wanting to host it for themselves. Aista's slogan is _"Where the Machine Creates the Code"_,
and also encapsulates our vision and goal.

## What does Aista mean?

Aista means a lot of things. It can be an acronym, at which point it implies _"Artificial
Intelligence Software Technology Assistance"_. In Hindi it implies _"Taking it easy and relaxing"_,
which arguably becomes the end result for the software developer as the machine creates most of your
code. In ancient Gothic it means _"In awe of, and in respect of"_, which are our company values.
While in Greek it implies _"Let it be, leave it go"_, which is what you can do with most of
your software development efforts once the machine creates most of your code.

## What is Hyperlambda?

Hyperlambda is a declarative meta programming language and hence lending itself heavily to
artificial intelligence and machine learning for obvious reasons, with the purpose of
automagically generating most (backend) code, freeing up the (human) software developer
to focus on more interesting tasks. Hyperlambda is at the core of Aista Magic Cloud, and
is open source in its entirety, and the project is publicly available at GitHub.

## Who invented Hyperlambda and Magic?

Thomas Hansen invented Magic and Hyperlambda in 2013, and continued working on it,
realising it was simply a superior tool for managing and administrating machine learning,
due to its meta programming capabilities.

## Can I generate frontend code with Aista?

Kind of. We have scaffolders that allows you to automagically generate Angular frontends,
and alsoother types of frontends - However, Aista Magic Cloud is definitely best suited
for generating backend code, due to Hyperlambda and its meta programming capabilities.

## Can I create an API with Aista?

Yes. You can literally point Aista Magic Cloud at any database you might have, and click
a button, for then to have Magic automagically generate a complete web API for you in seconds.
The resulting API is super scalable, async to the core, and easily understood due to
Hyperlambda's declarative syntax, making it much more easily understood than a traditional
programming language.

## Can I visually design my database with Aista?

Yes. Aista Magic Cloud contains a graphical database designer, allowing you to visually
design your database, similarly to how you would use a drag and drop user interface.
SQL Studio, our database designer, also allows you to execute SQL and manage your
databases, and works transparently towards SQL Server, MySQL, PostgreSQL, MariaDB
and SQLite.

## What databases does Aista support?

At the time of this writing we are supporting the following database systems.

- MySQL and MariaDB
- PostgreSQL
- Microsoft SQL Server
- SQLite

We have some basic support for Cassandra, ScyllaDB and CQL, but nothing that's officially
supported.

## Can I visually design my app with Aista?

No, besides SQL Studio there are no _"visual designers"_ in Magic. Magic is based upon
software development automation, and machine learning and AI, and not graphical user
interfaces allowing you to visually design neither backends nor frontends.

## How was Magic created?

Aista Magic Cloud is created on top of .Net Core and Active Events, or Super Signals.
Super Signals again is a simple design pattern invented by Thomas Hansen in 2009, facilitating
for extremely loosely coupled components of C# and .Net classes, resulting in Hyperlambda
ending up as an _"orchestration programming language"_, giving Aista Magic Cloud its
software development automation features.

## Is Magic Open Source?

Aista Magic Cloud is 100% Open Source and free of charge to use. The main backend is licensed as MIT,
the dashboard is GPL, and the plugins are LGPL. This allows you to use Magic to create closed source
applications, while also ensuring improvements to the project itself *stays* Open Source.

## What is meta programming?

Meta programming is when the human software developer does _not_ create software directly, but rather
relies upon other software systems automagically generating software. Meta programming is typically
based upon access to meta information about the task at hand, such as DDL information for some SQL based
relational database, and OpenAPI Swagger files, etc. Once the computer has access to meta information,
it can automatically generate a large part of your software, resulting in much faster iterations,
and much less resource usage. Meta programming is often associated with declarative programming.

## What is declarative programming?

Declarative programming is an extremely high abstraction level in software development, where you
do not focus on _"how"_ but exclusively focus on _"what"_. An example can be illustrated with
sending an email, which requires to create a socket connection, transmit handshake messages to
the SMTP server, establish a TLS channel for securely transmitting bytes, etc. The required steps
to send an email in traditional programming is mind baffling, and makes the process very difficult.
In declarative programming sending an email would simply imple invoking a function called for
instance _"sendEmail"_ passing in recipient, body and subject of your email, at which point the
task becomes much easier, since it requires much less thinking, and fewer things can go wrong.

## How is Machine Learning and AI implemented in Magic?

Magic internally is using OpenAI's ChatGPT Machine Learning API. However, instead of relying
upon the _"generic"_ and publicly available API, Magic allows you to create your own model,
by simplifying training, allowing you to for instance upload XML files or scrape your existing
website for training data, resulting in your own _"private"_ AI model, that you control access
to. This results in an AI model that is much _"sharper"_ for your particular domain than
the generally available ChatGPT model everybody can access at OpenAI's website.

## How is the task scheduler created?

The task scheduler in Magic allows you to create Hyperlambda code, and save your code into
your magic database. Each task can optionally be given one or more schedules, allowing your
tasks to execute at some deterministic date and time in the future, either once, or repeatedly
according to some sort of repetition pattern or schedule. When a task is due for execution,
it is executed on a background thread, to make sure the backend is still as reponsive as
possible. The task scheduler also takes care of thread pooling, to prevent multiple
tasks running at the same time resulting in that your backend becomes unresponsive.

## Can I extend Magic with C#?

Yes, but we don't currently allow hosting of modified Magic installations. However,
extending Hyperlambda and Aista Magic Cloud with C# is very easy. Start out by
cloning the _"magic.clone"_ project, look at its code, refer to the _"magic.signals"_
project's documentation, at which point you can easily create your own Hyperlambda
keywords probably in a couple of hours. If you do, and you open source license your
code, please [let us know](mailto:info@aista.com) since we love to hear about community
driven extentions, and we might be interested in promoting your work if it's good.

## How can I learn Hyperlambda?

The easiest way to learn Hyperlambda is to follow our hands on YouTube course that lasts
for roughly 5 hours.

- [www.youtube.com/watch?v=v1D3DtrmhS8&list=PLgyI389Eb9HNlhKpF9EHXO7D1EE7_dklg](https://www.youtube.com/watch?v=v1D3DtrmhS8&list=PLgyI389Eb9HNlhKpF9EHXO7D1EE7_dklg)

When you have watched the above videos, you can find the reference documentation
for each project and slot in the navbar section of the primary documentation for Magic.

## What is a cloudlet?

A cloudlet is a Kubernets POD deployed into our Kubernetes cluster, with Aista Magic Cloud
preconfigured and installed. We have automated the entire process of creating such
cloudlets, as a part of our hosting service, giving you your own private Magic installation.
We refer to such Magic installations as _"cloudlets"_. A cloudlet comes in different
sizes, with differences here implying how much storage, how much CPU, and how much memory
the cloudlet has - In addition to that a cloudlet can be delivered with a fully
managed database, either MySQL or PostgreSQL to replace the SQLite database we give
you with a _"managed database"_.
