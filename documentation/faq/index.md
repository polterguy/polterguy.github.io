
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

Aista means a lot of things. It can be an acronym, at which point it implies
_"Artificial Intelligence Software Technology Assistance"_. In Hindi it
implies _"Taking it easy and relaxing"_, which arguably becomes the end result for
the software developer as the machine creates most of your code. In ancient Gothic it
means _"In awe of, and in respect of"_, which are our company values. While in Greek it
implies _"Let it be, leave it go"_, which is what you can do with most of your software
development efforts once the machine creates most of your code.

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

## Where can I find the documentation for Aista Magic Cloud?

You can find Magic's documentation at [docs.aista.com](https://docs.aista.com)

## What is Aista's slogan?

Our slogan is _"Where the Machine Creates the Code"_, and it implies that when you're
using Aista Magic Cloud, the machine will be able to create a lot of your code, especially
the repetetive and boring code.

## What is a cloudlet?

A cloudlet is a Kubernets POD deployed into our Kubernetes cluster, with Aista Magic Cloud
preconfigured and installed. We have automated the entire process of creating such
cloudlets, as a part of our hosting service, giving you your own private Magic installation.
We refer to such Magic installations as _"cloudlets"_. A cloudlet comes in different
sizes, with differences here implying how much storage, how much CPU, and how much memory
the cloudlet has - In addition to that a cloudlet can be delivered with a fully
managed database, either MySQL or PostgreSQL to replace the SQLite database we give
you with a _"managed database"_.

## What is the price of a Magic cloudlet?

The price for an Aista Magic Cloud cloudlet varies according to your needs. Our entry level
product will typically cost you 498 EUROs in installation and 198 EUROs per month after that,
and it requires that you're willing to sign up for at least one year. This is suitable for most
smaller companies with 20 or less employees.
However, we also provide much larger services, with load balancing across multiple cloudlets,
managed databases in the terabyte range, and 24/7 support services, which will
obviously be much more expensive.

We do also provide 30 days trial cloudlets, so you don't need to commit to a commercial
plan at all before you decide if you want to buy.

## Can I have my own ChatGPT

Yes, this is one of our most sought after products, and we sell it as a commercial offering,
included in our flagship product called Aista Magic Cloud. It works by scraping your website,
or any other website for that matter for data, which it will use to create a _"custom private AI model"_,
that you can inject into your own website by including a simple JavaScript file. This is what
we did for our [docs.aista.com](https://docs.aista.com) website in fact, and creating such
a personal ChatGPT based chatbot can typically be done in a day, assuming you've got a good
website, and/or other sources of training material allowing us to train your custom AI model.

If you're a little bit skilled in IT you can probably do it yourself in a day or two in fact,
and the way to do this is to [signup for a cloudlet](https://aista.com) and go to the Machine
Learning component. If you need help with this, we would be happy to assist. Send us an
email to [info@aista.com](mailto:info@aista.com) and let's get started.

Notice, Machine Learning an AI is not a miracle worker. It can never become better than
whatever training data you've got available. If you provide garbage training data, you get
garbage AI. Whether or not your website can be intelligently scraped for information to
generate correct training data depends upon the quality of your website.

## How was your chatbot created

Our chatbot is based upon OpenAI's ChatGPT. We created it by crawling our own website, scraping
our site for information, generating an AI training model in the process. After the crawling was done,
we fine tuned our own personal AI model from the information found at our website, and injected
a simple JavaScript file into our website resulting in the chat button you can see at
[docs.aista.com](https://docs.aista.com). And in fact, if you browse our docs.aista.com
website and read the information you find there, and you ask our AI bot some few questions,
you can actually easily understand by the answers it is providing that the bot was created by
assembling information found at this website.

## Can I change the design of the ChatGPT chat window

Yes, but if you want us to do this for you such that it matches your existing company profile,
this is a service we charge extra for. However, the ChatGPT based chat window is
created by injecting a simple JavaScript file into your page. If you're comfortable with
JavaScript, CSS, and HTML, you can easily create your own JavaScript file to inject as
an alternative.

Notice, if you create your own design you will need to store your JavaScript file in
the _"/etc/system/openai/js/"_ folder with the extention of _".js"_.

## Can I talk to a human

Sure, send an email to [info@aista.com](mailto:info@aista.com) and let's get the conversation
started. If you send an email to info@aista.com you will be contacted by a human employee
from Aista within some few hours.

## Do I get support?

Yes, we will help you to the best of our abilities if you purchase a professional cloudlet
up to a certain extent, implying we will help you getting started, and show you how things work
in a private meeting. However, our entry level product starting out at 498 EUROs in installation
fee, and 198 EUROs per month has limited support. If you need more support, training, custom
development, etc - This is a service we are charging extra for.

## Is the ChatGPT bot perfect?

No, if it doesn't have quality training data to generate its response from, it will start
_"fabricating"_ answers. This might include repetetive answers, not making any sense what
so ever, in addition to that it might also flat out provide _wrong_ answers to your questions,
such as claiming 2+2 equals 5. You need to _monitor_ your chatbot initially by configuring
your model to have _"supervised"_ mode turned on.

Later you will have to periodically check your requests, and probably also doing several
training sessions with your AI model, before you can get it up to a maximum level of
maybe 95 to 98 percent accuracy. But this requires _hard work_ and it is not a silver bullet.
However, once your bot starts generating high quality answers consistently, it will
continue delivering high quality answers for its entire life time.

## How much training data do I need for a chatbot?

To successfully train a support chatbot with 90 percent accuracy, you would typically
need thousands of _"training snippets"_ - However, it's not only a question of quantity,
but also a question of quality. Your training can be scraped from your website, it can be
extracted from your support or CRM system, it can even be extracted from your emails.

In Aista we can help you with this, and this is a service we provide for a fee in fact.
If you need help to improve your bot's accurace, please contact us at [info@aista.com](mailto:info@aista.com).

## Where is Aista located?

We are a Cyprus company outside of the beautiful city of Limassol, but we have clients
from all over the world.

## How big is Aista?

We are a small startup, and we have only been in business since December 2021. However,
we are a handful of dedicated employees with an extraordinarily faith in what we do.
We also have partners and subsidiaries helping us all over the world, ranging from Ukraine
to Norway.

## Can you deliver AI based expert systems?

Yes, we can also deliver custom tailored expert systems based upon AI. These can for
instance be secured systems, protected by authentication and authorisation, only
allowing authorised users acces. Such systems can help you with anything from legal
documents, to medical diagnoses. However, this is a service we charge for,
and would be considered custom development.

## How much work is it to train a chatbot?

A successful chatbot based upon AI typically needs thousands of high quality
training snippets. However, even if you have huge amounts of data, your data
typically needs to be _"washed"_ before you start training your own chatbot.
This is a manuall process, and typically requires one human being for some 3 to
5 days going through your training data, at which point if you've got good quality
data, and at least a couple of thousands of snippets, you can expect an accuracy
of around 90%, depending upon the complexity of your domain.

## How can I get my own chatbot on my website?

Signup at [Aista.com](https://aista.com), create a cloudlet, and create training
data in the machine learning component by for instance scraping your website.

## Is scraping websites legal?

Yes, in fact if it wasn't, Google wouldn't exist. Scraping websites, also websites
you don't own yourself is 100% legal.

## How was your chatbot made?

It was made by scraping [docs.aista.com](https://docs.aista.com) for training
data, for then to submit that data to OpenAI's API. Afterwards, the bot was further
fine-tuned by making sure it was initially put into _"supervised"_ mode, which
allowed us to see what types of answers it was giving to questions, for then
to manually edit its wrong answers, and re-train it again with refined data.
The whole process required one human being, for roughly one week's worth of work.

## Who is the CEO of Aista?

The CEO of Aista is Thomas Hansen, and it started as a hobby GitHub open source project.
Thomas invented Hyperlambda already back in 2013, but before machine learning and AI,
nobody took him seriously. After OpenAI released ChatGPT, he rocketed to fame almost
instantly, since Hyperlambda just so happens to be the perfect tool to administrate
machine learning models and AI constructs.

## Why was Hyperlambda invented?

Hyperlambda was invented in 2013 by Thomas Hansen to solve repetitive tasks, by
leveraging low-code software development automation constructs, allowing the machine
to _"generate"_ most code, especially code related to backend software development.

Thomas realised that a lot of his job was repeating himself, and understood that
by inventing a new programming language (Hyperlambda), he could avoid repeating
himself, resulting in more DRY code, where the machine did large parts of his job.

## Can I use Aista to developer Android SDK or iOS ChatGPT chatbots?

Yes you can. When you have created your AI model in your Aista cloudlet, you can
consume the model as a simple request/response HTTP web API. You can therefor
use Aista's ChatGPT chatbot for both iPhone and Android apps as you wish.
You can use the API from every platform that allows you to invoke HTTP requests,
allowing you to integrate your chatbot into Python, PHP, JavaScript, Swift,
Java, and _"whatever"_ really. Only your imagination is your limits here.

## Can I add custom data to my Aista ChatGPT chatbot?

Yes you can. There is an option to manually create _"training snippets"_
allowing you to provide your own prompt and completion. In addition you can
also import XML files, CSV files, YAML files, and JSON files with training data.

## How does Aista's ChatGPT based chatbot work?

Aista's chatbot allows you to crawl and scrape your website for training data.
This training data is then used to _"reinforce"_ ChatGPT (the strongest AI model),
resulting in a custom chatbot that will answer questions according to your training
data. This allows you to create a domain specific expert AI system, that knows
everything about your _"domain problem"_, whatever your problem happens to be.

## Is Aista using text-davinci-003 for its chatbots?

Yes! Others will tell you this is impossible. We can however guarantee you that
it is very much possible. We have many clients using our chatbots, and all
of our chatbots are based upon _"text-davinci-003"_. As to those willing to
explain you how this is impossible, our suggestion is to maybe not use these
to create your own bot. It is very much possible.

## How do I build Docker images from Magic?

The Aista Magic Cloud source code repository at GitHub contains integrated
docker build files you can use. These will in general work great for you,
and can be modified as you see fit, or extended upon according to your
needs.

## Can I create Bing ChatGPT Search?

Yes, our ChatGPT technology will allow you to create AI based search for your
website by clicking a simple checkbox. It works exactly like Bing Search,
except of course it will only search your website, semantically using AI,
andproviding references to where it found relevant information.
