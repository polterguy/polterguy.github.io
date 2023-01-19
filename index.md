---
title: Getting started with Aista Magic Cloud
description: Where the Machine Creates your Code, using Artificial Intelligence, Machine Learning, meta programming, and software development automation
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/Aista-Magic-Cloud.jpeg
---

# Aista Magic Cloud

Aista Magic Cloud is a software development platform that creates most of your code 100% automatically,
by leveraging meta programming, declarative programming, artificial intelligence, and software development
automation. This allows you to focus on the creative tasks while having the computer take care of the
boring parts.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/n8Y4sTrprqk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As a software developer typically 80% of your job is literally so simple that it can be replaced
with artificial intelligence and software development automation, based upon meta programming constructs.
This results in more secure applications and robust solutions, with less bugs, better scaling, and more freedom
for you to pursue more creative tasks. In general Aista Magic Cloud makes you at least 5 times as productive,
sometimes hundreds of times more productive. Aista Magic Cloud is not suitable for all tasks though. It's
primary strength is for generating backend code, that is database centric in nature, and/or integrates with
other web APIs.

## CRUD generator

The CRUD generator allows you to wrap any database you have in CRUD API endpoints in seconds. It reads
meta data from your database, and automatically generates a web API for you, producing thousands
of lines of code for you in the process. The generated API is secured according to your instructions, and
can be used as the foundation for your own frontend.

![CRUD API generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

The web API generator takes care of left joins, referential integrity, validators, authentication and authorisation,
while allowing you to declaratively inform it how to generate your web API. It also allows you to publish
web socket messages as endpoints are invoked.

## SQL API generator

Magic allows you to create HTTP endpoints using SQL. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find this component in the Endpoint Generator.
Choose your database, provide some SQL, add arguments that you reference in your SQL, and click the
_"Generate"_ button.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The SQL API generator allows you to secure your endpoints, declare arguments, use all 5 most common HTTP
verbs, etc. You can use it with SQL Server, MySQL, MariaDB, PostgreSQL or SQLite.

## SQL Studio

Magic allows you to visually design your database using a graphical user interface. No need to mess with complex
SQL DDL. Use SQL Studio to visually design your database and save hours of searching the web for the correct
syntax to use when creating foreign keys. SQL Studio supports the following databases.

* Microsoft SQL Server
* PostgreSQL
* MySQL
* MariaDB
* SQLite

![Aista's SQL Studio](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

SQL Studio also allows you to execute any SQL towards your database of choice, giving you superior database
management tools, allowing you to administer your databases from anywhere in the world. By combining SQL Studio
with the CRUD API generator and more specifically the SQL API generator, you can compose some SQL, and wrap
it into a web API endpoint in seconds.

![SQL Studio](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-studio-2.jpg)

Are you an expert DB admin, but have no knowledge of backend programming? No problem. Wrap your SQL into
a web API endpoint 100% automagically with zero coding besides providing the SQL generator with some SQL
you want it to execute as your endpoint is invoked.

## Hyper IDE

Magic also contains its own IDE or integrated development environment.
Hyper IDE provides syntax highlighting for most popular programming languages, in addition
to autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications by executing your endpoint without ever having to leave your IDE.

![Magic's Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

The real power of the CRUD Generator is that it generates code you can edit, with a declarative programming language
called Hyperlambda. If you need to add business logic to your generated CRUD endpoints, this is easily achieved
using Hyper IDE. Hyper IDE integrates perfectly with our Machine Learning component, built on top of OpenAI's
ChatGPT, allowing you to write your requests in plain English, and have Hyper IDE and ChatGPT automatically
generate code for you solving your problem.

## Create your own AI expert system

Aista Magic Cloud allows you to generate your own Machine Learning models in seconds, by scraping any website,
and generating training data for you that you can use to create your own ChatGPT model, answering questions
related to your domain. Need a chat bot for your company answering questions about your company or domain?
That's a 5 seconds job for Aista Magic Cloud as long as you have an existing website, and/or structured
training data you can upload to your cloudlet. Use cases might be;

* Expert law system, answering legal questions for your clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chat bot for your enterprise, giving your client support for whatever questions they might have
* Etc, etc, etc

Creating a Machine Learning training model is incredibly difficult unless you know what you're doing.
With Aista Magic Cloud it becomes 1,000 times easier, and you can literally do it by pointing Aista
to your existing website, have our website scraper crawl your website, resulting in a custom AI expert
system in some few seconds.

## Frontend generator

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
component. Import users from your existing database, provide access to modules and components according
to what roles your users belongs to, and make sure only authorised users have access to private and secured
data.

## Task scheduler

Aista Magic Cloud allows you to create and administer tasks. A task is a background job, that is persisted
into your database as Hyperlambda, and it can either be executed by a _"trigger"_ occurring somewhere
else in your system, or periodically schedlued to execute repeatedly, or at some specific date and time in
the future. The task scheduler allows you to easily manage your tasks, edit them, and create new tasks
as you see fit.

## Plugins

Aista Magic Cloud also contains its own _"marketplace"_ allowing you to rapidly install some plugin
solving some particular need you might have in your own applications. Some example plugins are listed
below;

* Stripe payment integrations
* Translation micro service
* Ticket backend administration system
* Etc, etc, etc - Contact us if you need something specific we still haven't built

## Integrated log

Aista Magic Cloud also comes with an integrated log component, allowing you to browse your server log,
easily giving you control over events occurring that might somehow have consequences for your system.

## Open Source

Aista Magic Cloud is 100% open source, and you can use it free of charge in proprietary projects
as you see fit. You can find its code at [GitHub](https://github.com/polterguy/magic), and
we accept pull requests for itif your code is high quality. We also provide docker images
for Magic, allowing you to install it locally in seconds without having to mess with dependencies,
such as the .Net CLI and NodeJS. However, the fastest way to get started with Magic is to
create a free 90 day trial cloudlet at [Aista.com](https://aista.com).

* [Get started with Magic](https://aista.com)

## Features

Aista Magic Cloud contains the following features;

* Hyper IDE, and integrated IDE allowing you to create and maintain your code directly on your server
* SQL Studio, allowing you to visuall design your database, and execute any SQL towards it, getting instant feedback on the result
* Machine Learning, allowing you to write in plain English your request to the machine, resulting in OpenAI generating functioning code for you that you can immediately use in your own solutions
* Machine Learning automation, allowing you to create your own Machine Learning model by scraping your website
* Database management tools to administer your databases in one place with a uniform UI
* User administration allowing you to control who's got access to what with a role based access control (RBAC) UI component
* Task scheduler allowing you to manage and schedule tasks
* Plugins for installing backend micro service components solving your particular needs
* Log component giving you easy access to see what occurs in your system over time
* Cryptography features for managing super sensitive data
* Health check component allowing you to automatically test integrity of your particular system
* Configuration component allowing you to manage your server's configuration settings
* Endpoints component giving you a _"Swagger like UI"_ for testing your endpoints
* Hyperlambda playground allowing you to execute some Hyperlambda snippet
* Web Sockets component allowing you to debug and test your web socket integrations
* Etc, etc, etc

Aista Magic Cloud is basically your _"one stop shop"_ for most of your software development requirements,
with its edge of course being that it generates most of your code 100% automagically.

## More

* [Tutorials](/tutorials/) - Tutorials about how to get started with Aista Magic Cloud
* [Docs](/documentation/) - Reference documentation for Aista Magic Cloud
