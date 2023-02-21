---
title: Documentation for Aista Magic Cloud and Hyperlambda
description: Where the Machine Creates your Code, using Artificial Intelligence, Machine Learning, meta programming, and software development automation
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg
---

# What is Aista Magic Cloud?

Aista Magic Cloud, or Magic for short, is a software development platform that creates most of your code _"automagically"_,
by leveraging meta programming, declarative programming, artificial intelligence, and low-code software development
automation. This allows you to focus on creative tasks, while having the machine implement the
boring parts. Aista Magic Cloud is [open source](https://github.com/polterguy/magic), but Aista also
offers [hosting of Magic](https://aista.com) for a monthly fee.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/n8Y4sTrprqk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Why use Aista Magic Cloud?

As a software developer typically 80% of your job is literally so simple that it can be replaced
with artificial intelligence and software development automation, based upon meta programming constructs.
This results in more secure and robust solutions, with less bugs, better scaling, and more freedom
for you to pursue more creative tasks. In general Aista Magic Cloud makes you at least 5 times as productive,
sometimes hundreds of times more productive.

## What can I create with Magic?

Aista Magic Cloud is not suitable for all tasks. Its
primary strength is for generating backend code, that is database heavy in nature, and/or integrates with
other web APIs. However, when you can use Magic, it easily saves you 80% of your time, and sometimes it will
save you 95% of your time and resources, depending upon your requirements. Below are some examples of
apps where it makes sense to use Magic.

* Custom ChatGPT website chatbots
* CRM systems
* Headless CMS systems
* EPJ systems tracking patients and journals of patients
* Inventory systems
* Task management systems, such as ClickUp, Monday.com, or similar types of systems
* Logistic systems
* Basically, anything that requires collecting and managing data, where CRUD operations are important

As an example of how useful Magic is, realise that at Aista we built our [entire hub](https://hub.aista.com) using
nothing but Magic and Hyperlambda. This saved us roughly 90% of the resource requirements we would have needed if
we were to create the same system using for instance GoLang, Python or PHP.

## Custom ChatGPT website chatbots

You can use Magic to create your own custom ChatGPT chatbot in minutes, for then to embed it into your
website in some few seconds. The Chatbot Wizard component in Magic will ask you for your OpenAI API key,
your Google reCAPTCHA settings, for then to allow you to scrape your website generating a custom machine
learning model in the process. This model allows your users to ask questions related to _your website_,
and have the chatbot answer how you _want it to answer questions_. Want to have a chatbot that tells your
users you're the President of China? No problem, it's a 5 minute job for Magic.

![Custom ChatGPT website chatbot](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/custom-chatgpt-chatbot.jpg)

It works by scraping your website, generating training data in the process, for then to end up with a
custom machine learning model that answers questions according to your training data. You can try out such
a chatbot by clicking the button on the bottom right corner of this page, and ask it any question related to
AISTA, Magic Cloud or Hyperlambda. This chatbot was created by scraping this website.

## The backend generator

The backend generator allows you to wrap any database you have in CRUD API endpoints in some few seconds. It reads
meta data from your database, and automatically generates a web API for you, producing thousands
of lines of code for you in the process. The generated API is secured according to your instructions, and
can be used as the foundation for your own frontend.

![Backend generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

The web API generator takes care of left joins, referential integrity, validators, authentication and authorisation,
while allowing you to declaratively tell it how to generate your API. It also allows you to publish
web socket messages as endpoints are invoked, in addition to having tons of additional features simplifying
your life as a software developer. If your endpoints are simple wrappers around your database, the endpoint
generator can do 100% of your job automagically.

## The SQL endpoint generator

Magic allows you to create HTTP endpoints using SQL. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find this component in the Endpoint Generator,
in its _"SQL Endpoint Generator"_ tab. Choose your database, provide some SQL, add arguments that you
reference in your SQL, and click the _"Generate"_ button.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The SQL API generator allows you to secure your endpoints, declare what arguments your endpoint can handle,
use all 5 most common HTTP verbs for your endpoints, etc. You can use it with SQL Server, MySQL, MariaDB,
PostgreSQL or SQLite - However, you need to write SQL that is valid for your particular database type as
you create your endpoints. Some use cases can be found below.

* Statistics
* Reports
* Endpoints for charts
* Etc, etc, etc

## SQL Studio

Magic allows you to visually design your database using a graphical user interface. No need to mess with complex
SQL DDL. Use SQL Studio to visually design your database and save hours of searching the web for the correct
syntax to use when creating foreign keys or needing other constructs rarely if ever remembered by the human brain.
SQL Studio supports the following databases.

* Microsoft SQL Server
* PostgreSQL
* MySQL
* MariaDB
* SQLite

![Aista's SQL Studio database designer](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-designer.jpg)

SQL Studio also allows you to execute any SQL towards your database of choice, giving you superior database
management tools, allowing you to administer your databases from anywhere in the world. By combining SQL Studio
with the backend generator, and especially the SQL API generator, you can compose some SQL, and wrap
it into a web API endpoint in seconds.

![SQL Studio](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-studio-2.jpg)

Are you an expert DB admin, but have no knowledge of backend programming? No problem, wrap your SQL into
a web API endpoint 100% automagically with zero coding besides providing the SQL generator with some SQL
you want it to execute as your endpoint is invoked.

## Hyper IDE

Magic also contains its own IDE or integrated development environment.
Hyper IDE provides syntax highlighting for most popular programming languages, in addition
to autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications by executing your endpoint without ever having to leave your IDE.

![Magic's Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

The real power of the backend generator is that it generates code you can edit, with a declarative programming language
called Hyperlambda. If you need to add business logic to your generated CRUD endpoints, this is easily achieved
using Hyper IDE.

Hyper IDE also integrates perfectly with our Machine Learning component, built on top of OpenAI's
ChatGPT, allowing you to write your requests in plain English, and have Hyper IDE and ChatGPT automatically
generate code for you solving your problem.

## Machine Learning and AI

Aista Magic Cloud is scattered with AI and allows you to generate your own Machine Learning models in seconds,
by scraping any website, and generating training data for you that you can use to create your own ChatGPT model,
answering questions related to your domain. Need a chat bot for your company answering questions about your company
or domain? That's a 5 seconds job for Aista Magic Cloud as long as you have an existing website, and/or structured
training data you can upload to your cloudlet. Use cases might be.

* Expert legal system, answering legal questions for clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chat bot for your enterprise, giving your clients support for whatever questions they might have related to your company
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand
* Etc, etc, etc

![Magic's Machine Learning parts](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg)

Creating a Machine Learning training model is incredibly difficult unless you know what you're doing.
With Aista Magic Cloud it becomes 1,000 times easier, and you can literally do it by pointing Aista
to your existing website, have our web scraper crawl your website, resulting in a custom AI expert
system model in some few seconds.

## The frontend generator

In addition to the backend web API generator, Aista also contains a frontend generator, that creates
a fully functional frontend web application for you in seconds. The generated code is perfect Angular code,
and can be modified according to your needs after the generator is done.

![Frontend generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sakila.jpg)

The generated frontend will be secured with authentication and authorisation, and wrap all your database
tables with UI components required to create, read, update and delete records from your database. The frontend
generator will also create autocomplete components with searching and filtering capabilities for referenced
tables with foreign keys, take care of types for you automatically, and basically provide you with a
starter kit solving 80% of your frontend software development problems before you have to write a single
line of code.

## User management

Aista Magic Cloud allows you to administer your users easily, by giving you a graphical user interface,
allowing you to manage your application's users and roles, using a role based access control (RBAC)
component. Import users from your existing system, provide access to modules and components according
to what roles your users belongs to, and make sure only authorised users have access to private and secured
data.

![Users and roles administration in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

The user and role systemin Magic is based upon RBAC implying Role Based Access Control, allowing you to
provide access to components and modules based upon roles, for then to associate roles with users.

## The task scheduler

Aista Magic Cloud allows you to create and administer tasks. A task is a background job, that is persisted
into your database as Hyperlambda, and it can either be executed by a _"trigger"_ occurring somewhere
else in your system, or periodically scheduled to execute repeatedly, or at some specific date and time in
the future. The task scheduler allows you to easily manage your tasks, edit them, and create new tasks
as you see fit.

![Hyperlambda task scheduler](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg)

Due to its dynamic nature, the task scheduler is also a perfect foundation for your own business process
workflows, where functionality is dynamically built and executed by _"triggers"_ occurring in your
own code.

## Plugins

Aista Magic Cloud also contains its own _"marketplace"_ allowing you to rapidly install some plugin
solving some particular need you might have in your own applications. Some example plugins are listed
below;

* Stripe payment integrations
* Translation micro service
* Ticket backend administration system
* Etc, etc, etc - [Contact us](mailto:info@aista.com) if you need something specific we still haven't built

![Magic's plugins](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/bazaar.jpg)

## The integrated log

Aista Magic Cloud also comes with an integrated log component, allowing you to browse your server log,
giving you control over events occurring that might somehow have consequences for your system.

![Magic log](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/log.jpg)

When you create your own Hyperlambda applications, you can also create log entries as you see fit,
to log important events, such as deleting records, executing tasks, registering users, etc.

## Aista Magic Cloud is Open Source

Aista Magic Cloud is 100% open source, and you can use it free of charge in proprietary projects
as you see fit. You can find its code at [GitHub](https://github.com/polterguy/magic), and
we accept pull requests for it if your code is high quality. We also provide docker images
for Magic, allowing you to install it locally in seconds without having to mess with dependencies,
such as the .Net CLI and NodeJS. However, the fastest way to get started with Magic is to
create a free 30 day trial cloudlet at [Aista.com](https://aista.com).

## How to get started

You can of course download the open source code from GitHub, but the easiest way to get started
immediately is to simply register at [Aista.com](https://aista.com), at which point you'll
get a free 30 days trial cloudlet, with security, CDN, automatically configured with
all best practices applied out of the box. We do charge a fee for such cloudlets, but we
also provide 30 days trial cloudlets for free, without asking you for anything else but
your email address.

* [Signup at Aista.com for your free 90 days cloudlet](https://aista.com)

## Primary features of Aista Magic Cloud

Below is a more or less complete list of Aista Magic Cloud's frontend UI components and features,
allowing you to graphically administrate your Magic installation.

* [Endpoint generator component](/documentation/magic/components/crudifier/backend/)
* [Frontend generator component](/documentation/magic/components/crudifier/frontend/)
* [SQL endpoint generator component](/documentation/magic/components/crudifier/sql/)
* [The database component](/documentation/magic/components/databases/)
* [SQL Studio](/documentation/magic/components/sql/)
* [Machine Learning and AI](/documentation/magic/components/machine-learning/)
* [Hyper IDE](/documentation/magic/components/hyper-ide/)
* [Hyperlambda Playground](/documentation/magic/components/evaluator/)
* [Endpoints](/documentation/magic/components/endpoints/)
* [Plugins component](/documentation/magic/components/bazar/)
* [Tasks component](/documentation/magic/components/tasks/)
* [Users and roles component](/documentation/magic/components/auth/)
* [Cryptography component](/documentation/magic/components/crypto/)
* [Health check](/documentation/magic/components/assumptions/)
* [Custom ChatGPT website chatbots](/documentation/magic/components/chatbot-wizard/)
* [Sockets](/documentation/magic/components/sockets/)
* [Configuration component](/documentation/magic/components/config/)
* [Profile component](/documentation/magic/components/profile/)
* [Log](/documentation/magic/components/log/)
* [HTTP endpoints in Magic](/documentation/magic/endpoints/)
* [Dynamic Hyperlambda slots in Magic](/documentation/magic/slots/)
