---
title: "Magic Cloud"
description: "Magic Cloud is an AI-based Low-Code and No-Code software development automation framework, allowing for the machine to create most of your code"
header:
  image: /assets/images/wizard-large.webp
  image_description: Wizard standing in his library reading a book symbolizing the power of Magic Cloud
---

Magic Cloud, or Magic for short, is a backend software development platform that creates most of your code _"automagically"_, by leveraging meta programming, declarative programming, AI, low-code, and no-code. This allows you to focus on creative tasks, while having the machine create the boring parts.

> Where the Machine Creates the Code!

Magic is 100% open source, and you can find its [GitHub repo here](http://github.com/polterguy/magic). If you don't want to mess with hosting yourself, you can check out our professional or enterprise hosting plans [here](https://ainiro.io).

## AI Generated Code

With Magic you can sometimes accomplish in some few minutes what requires weeks of coding with a more
traditional platform. The following video illustrates how to create a full stack app using Magic Cloud.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-width: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/k6eSKxc6oM8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## The Magic Dashboard

Magic's purpose is to help you with your backend, and it comes with a dashboard allowing you to manage all aspects of your backend. The dashboard contains UI components for most things you'll need when creating and maintaining your API and backend code. Below you can find some general information about some of its most important components.

## Hyper IDE

Magic contains its own IDE or integrated development environment. [Hyper IDE](/dashboard/hyper-ide/) provides syntax highlighting 
and autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications, by executing your endpoint without ever having to leave your IDE. Magic even has its own backend _"vibe coding"_ prompting mechanisms, allowing you to generate Hyperlambda from natural language using generative AI.

![Screenshot of Magic's Hyper IDE with autocomplete open for Hyperlambda slots](/images/hyper-ide-actions.jpg)

Hyper IDE also integrates with our Machine Learning component, built on top of OpenAI, allowing you to write your requests in plain English, and have Hyper IDE and OpenAI automatically generate code for you solving your problem.

In addition its [workflows](/workflows/) feature allows you to dynamically orchestrate backend Hyperlambda code together, without needing to know Hyperlambda.

> With Hyper IDE manually writing code is optional

## The Endpoint Generator

The [Endpoint Generator](/dashboard/endpoint-generator/) allows you to wrap any database you have in CRUD API endpoints. It reads
meta data from your database, and automatically generates a web API for you. The generated API is
secured according to your instructions, and can be modified after it's created.

![Screenshot of Endpoint Generator allowing you to generate CRUD apps wrapping your database of choice](/images/backend-crud.jpg)

The Endpoint Generator takes care of left joins, referential integrity, validators, authentication, and authorisation -
While allowing you to declaratively tell it how to generate your API. It also allows you to publish
web socket messages as endpoints are invoked, in addition to having lots of additional features simplifying
your life as a software developer.

By combining the Endpoint Generator with [Hyperlambda Workflows](/workflows/), you can sometimes create your entire backend code exclusively by _"clicking buttons"_.

## The SQL Endpoint Generator

Magic allows you to create HTTP endpoints using SQL. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find this component in the Endpoint Generator,
in its _"SQL Endpoint Generator"_ tab. Choose your database, provide some SQL, add arguments that you
reference in your SQL, and click the _"Generate"_ button.

![Screenshot of the SQL Endpoint Generator allowing you to create HTTP endpoints with SQL](/images/sql-web-api.jpg)

The SQL endpoint generator allows you to secure your endpoints, declare what arguments your endpoints can handle,
use all 5 most common HTTP verbs for your endpoints, etc. You can use it with SQL Server, MySQL, MariaDB,
PostgreSQL, or SQLite - And if you don't know SQL, then SQL Studio even has integrated support for generating SQL from natural language. You can see an example below.

![Screenshot of the SQL Endpoint Generator allowing you to create HTTP endpoints with SQL](/images/sql-generator.png)

## SQL Studio

SQL Studio allows you to visually design your database using a graphical user interface. SQL Studio supports the following databases.

* Microsoft SQL Server
* PostgreSQL
* MySQL
* MariaDB
* SQLite

![Screenshot of SQL Studio's database designer while designing a database](/images/sql-designer.jpg)

SQL Studio also allows you to execute any SQL towards your database of choice, allowing you to administer your databases from anywhere. By combining SQL Studio with the Backend Generator, and especially the SQL API generator, you can compose some SQL, and rapidly wrap it into an API endpoint.

![Screenshot of SQL Studio while executing an arbitrary SQL statement](/images/sql-studio-2.jpg)

## Machine Learning and AI

Magic Cloud is scattered with AI and allows you to create your own Machine Learning models using OpenAI, by scraping any website, and generate training data (RAG data) that you can use to answer questions related to your domain. Use cases might be.

* Expert legal system, answering legal questions for clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chatbot for your enterprise, giving your clients support for whatever questions they might have related to your company
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand
* Etc, etc, etc

You can try out such a chatbot in the bottom/right corner of this page.

## User management

Magic Cloud allows you to create and administer users, by giving you a graphical user interface, allowing you to manage your application's users and roles, using a role based access control (RBAC) component. Provide access to modules and components according to what roles your users belongs to, and make sure only authorised users have access to private and secured data.

The user and role systemin Magic is based upon RBAC implying Role Based Access Control, allowing you to provide access to components and modules based upon roles, for then to associate roles with users.

## The task manager

Magic Cloud allows you to create and administer tasks. A task is a background job, that is persisted into your database as Hyperlambda, and it can either be executed by a _"trigger"_ occurring somewhere else in your system, or periodically scheduled to execute repeatedly, or at some specific date and time in the future. The task manager allows you to easily manage your tasks, edit them, and create new tasks as you see fit.

## Plugins

Magic Cloud also contains its own _"App Store"_, allowing you to rapidly install some plugin solving some particular need you might have in your own applications. Some example plugins are listed below;

* Stripe payment integrations
* Registration workflow actions
* Shopify AI chatbot integration
* WordPress AI chatbot integration
* Several example SQLite databases
* Etc, etc, etc

## The integrated log

Magic Cloud also comes with an integrated log component, allowing you to browse your server log, giving you control over events occurring that might somehow have consequences for your system.

When you create your own Hyperlambda applications, you can also create log entries as you see fit, to log important events, such as deleting records, executing tasks, registering users, etc.

## Custom AI chatbots

You can also use Magic to create your own custom AI chatbot, for then to embed it into your website. The Chatbot Wizard component in Magic will ask you for your OpenAI API key, for then to scrape your website generating a RAG database in the process. The end result allows your users to ask questions related to your website, and have the chatbot answer how you want it to answer questions.

It works by scraping your website, generating training data in the process, for then to end up with a custom _"machine learning model"_ (based upon RAG), that answers questions according to your training data. You can try out such a chatbot by clicking the button in the bottom / right corner of this page, and ask it any question about Magic Cloud. This chatbot was created by scraping this website. At AINIRO we also delivers such chatbots as one of our services. Read more about [our AI chatbots here](/dashboard/chatbot-wizard/).

## The goal of the project

The goal of the project is to make it easier to produce high quality and scalable code, much faster, without security holes, in an extremely scalable runtime. AKA ...

> Where the Machine Creates the Code!
