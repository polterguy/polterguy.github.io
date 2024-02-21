---
title: "Magic Cloud"
description: "Magic Cloud is an AI-based Low-Code and No-Code software development automation framework, allowing for the machine to create most of your code"
header:
  image: /assets/images/wizard-large.webp
  image_description: Wizard standing in his library reading a book symbolizing the power of Magic Cloud
---

Magic Cloud, or Magic for short, is a backend software development platform that creates most of your code _"automagically"_, by leveraging meta programming, declarative programming, artificial intelligence, low-code, and no-code software development automation. This allows you to focus on creative tasks, while having the machine create the boring parts. Magic comes in two flavors.

* Enterprise Version
* Open Source Community Edition

The open source community edition is no longer actively maintained, and should be considered legacy. It's still available, but it will not have bug fixes, security patches, or any future changes, and I doubt you can make it worksince it relies upon 42 projects that have been made private.

The Enterprise Version is closed source and contains everything the community edition contains, in addition to a lot of additional things. The Enterprise Version comes with professional support and comes in two prices.

* Single Server License at $5,000 per month
* Kubernetes Cluster License for $20,000 per month

If you're interested in purchasing a professional license you can [contact us here](mailto:thomas@ainiro.io). If you're only looking for a hosted cloudlet allowing you to use all plugins, create workflows, and AI chatbots - You can purchase a cloudlet from AINIRO.IO [here](https://ainiro.io/buy).

Notice, AINIRO.IO also provides cloudlets, which are basically Kubernetes PODs, with the complete Magic installation, starting out at some few hundred bucks per month, if you don't have the budget to pay $5,000 or $20,000 per month for access to an on-premise solution. You can find more information about our cloudlets [here](https://ainiro.io).

## Workflows

With Magic you can sometimes accomplish in some few minutes what requires weeks of coding with a more
traditional platform. The following YouTube video illustrates how to create a [workflow](/workflows/), and wrap
it into an API. It's a fairly complex workflow too, handling Stripe payments - Something even
experienced software developers often struggle with. In the video I wire up Stripe payments in some
few minutes using declarative programming and workflows.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/ITz1ASqsWoM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## The Magic Dashboard

Although Magic's purpose is to help you with backend code, it comes with a dashboard allowing you to manage your Magic backend. The dashboard contains UI components for most things you'll need when creating and maintaining your backend code.

* [Hyper IDE](/dashboard/hyper-ide/)
* [Endpoint Generator](/dashboard/endpoint-generator/)
* [SQL Studio](/dashboard/sql-studio/)
* Plus many more ...

## Hyper IDE

Magic also contains its own IDE or integrated development environment. [Hyper IDE](/dashboard/hyper-ide/) provides syntax highlighting 
and autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications, by executing your endpoint without ever having to leave your IDE.

![Magic's Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

Hyper IDE also integrates perfectly with our Machine Learning component, built on top of OpenAI, allowing you to write your requests in plain English, and have Hyper IDE and OpenAI automatically
generate code for you solving your problem.

However, the most powerful parts of Hyper IDE is its _"workflows"_ feature, allowing you to dynamically orchestrate
backend Hyperlambda code together, without needing to know Hyperlambda.

> With Hyper IDE manually writing code is __optional__

## The Endpoint Generator

The [Endpoint Generator](/dashboard/endpoint-generator/) allows you to wrap any database you have in CRUD API endpoints. It reads
meta data from your database, and automatically generates a web API for you. The generated API is
secured according to your instructions, and can be modified after it's created.

![Endpoint Generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

The web API generator takes care of left joins, referential integrity, validators, authentication, and authorisation -
While allowing you to declaratively tell it how to generate your API. It also allows you to publish
web socket messages as endpoints are invoked, in addition to having lots of additional features simplifying
your life as a software developer.

By combining the Endpoint Generator with Hyperlambda [Workflows](/workflows/), you can sometimes create your entire backend code exclusively by _"clicking buttons"_.

## The SQL endpoint generator

Magic allows you to create HTTP endpoints using SQL. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find this component in the Endpoint Generator,
in its _"SQL Endpoint Generator"_ tab. Choose your database, provide some SQL, add arguments that you
reference in your SQL, and click the _"Generate"_ button.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The SQL endpoint generator allows you to secure your endpoints, declare what arguments your endpoint can handle,
use all 5 most common HTTP verbs for your endpoints, etc. You can use it with SQL Server, MySQL, MariaDB,
PostgreSQL or SQLite - However, you need to write SQL that is valid for your particular database type as
you create your endpoints.

## SQL Studio

Magic allows you to visually design your database using a graphical user interface. SQL Studio supports
the following databases.

* Microsoft SQL Server
* PostgreSQL
* MySQL
* MariaDB
* SQLite

![AINIRO's SQL Studio database designer](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-designer.jpg)

SQL Studio also allows you to execute any SQL towards your database of choice, allowing you to administer
your databases from anywhere. By combining SQL Studio with the backend generator, and especially
the SQL API generator, you can compose some SQL, and rapidly wrap it into a web API endpoint.

![SQL Studio](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-studio-2.jpg)

## Machine Learning and AI

Magic Cloud is scattered with AI and allows you to create your own Machine Learning models using OpenAI,
by scraping any website, and generating training data for you that you can use to create your own OpenAI model,
answering questions related to your domain. Use cases might be.

* Expert legal system, answering legal questions for clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chatbot for your enterprise, giving your clients support for whatever questions they might have related to your company
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand
* Etc, etc, etc

You can try out such a chatbot in the bottom/right corner of this page.

## User management

Magic Cloud allows you to administer your users, by giving you a graphical user interface,
allowing you to manage your application's users and roles, using a role based access control (RBAC)
component. Provide access to modules and components according to what roles your users belongs to,
and make sure only authorised users have access to private and secured data.

The user and role systemin Magic is based upon RBAC implying Role Based Access Control, allowing you to
provide access to components and modules based upon roles, for then to associate roles with users.

## The task manager

Magic Cloud allows you to create and administer tasks. A task is a background job, that is persisted
into your database as Hyperlambda, and it can either be executed by a _"trigger"_ occurring somewhere
else in your system, or periodically scheduled to execute repeatedly, or at some specific date and time in
the future. The task manager allows you to easily manage your tasks, edit them, and create new tasks
as you see fit.

## Plugins

Magic Cloud also contains its own _"App Store"_, allowing you to rapidly install some plugin
solving some particular need you might have in your own applications. Some example plugins are listed
below;

* Stripe payment integrations
* Registration workflow actions
* Several example SQLite databases
* Etc, etc, etc

## The integrated log

Magic Cloud also comes with an integrated log component, allowing you to browse your server log,
giving you control over events occurring that might somehow have consequences for your system.

When you create your own Hyperlambda applications, you can also create log entries as you see fit,
to log important events, such as deleting records, executing tasks, registering users, etc.

## Custom AI chatbots

You can also use Magic to create your own custom AI chatbot, for then to embed it into your
website. The Chatbot Wizard component in Magic will ask you for your OpenAI API key,
your Google reCAPTCHA settings, for then to scrape your website generating a VSS database in the process.
The end result allows your users to ask questions related to your website, and have the chatbot answer
how you want it to answer questions.

It works by scraping your website, generating training data in the process, for then to end up with a
custom _"machine learning model"_ (based upon RAG), that answers questions according to your training data.
You can try out such a chatbot by clicking the button in the bottom right corner of this page, and ask it
any question related to AINIRO.IO, or concepts from this website. This chatbot was created by scraping this
website. At AINIRO.IO we also delivers such chatbots as one of our services. Read more about
[our AI chatbots here](/dashboard/chatbot-wizard/).

## Magic Cloud is NOT Open Source

Magic Cloud started as open source. However, the project had 10 million downloads of its NuGet packages, zero contributions, and zero donations, so we could no longer justify maintaining it as an open source project. If you're interested in accessing its source code, we do provide the source with a server license and kubernetes license, which has a cost of $5,000 per month, and $20,000 per month, which gives you access to its source code.

## The goal of the project

The goal of the project is to make it possible for everybody to produce high quality code,
much faster, without security holes, in an extremely scalable runtime. AKA ...

> Where the Machine Creates the Code!
