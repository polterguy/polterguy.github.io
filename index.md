---
title: Magic Cloud
description: Magic Cloud is an AI, Low-Code and No-Code platform that builds and hosts your entire backend, and powers database-driven AI agents over MCP.
header:
  image: /assets/images/hero/home.png
  og_image: /assets/images/hero/home-og.png
  image_description: Magic Cloud
faq:
  - q: "What is Magic Cloud?"
    a: "An open source AI, Low-Code and No-Code platform that builds and hosts your entire backend - database, API, business logic, background jobs, and authentication - and powers database-driven AI agents over MCP."
  - q: "What can I build with Magic?"
    a: "Full stack apps such as CRM systems, secure web APIs wrapping new or legacy databases, custom AI chatbots trained on your own content, database-driven AI agents, scheduled background jobs, and static websites - most of it generated from natural language."
  - q: "Can I create an AI agent with Magic?"
    a: "Yes. Create a machine learning model, give it AI functions - endpoints the AI can invoke, added from Hyper IDE or straight into the model's system instruction - and the chatbot becomes an agent that can query your database, trigger workflows, and act on the user's behalf. Alternatively, connect an orchestrator such as Claude over MCP, and your entire cloudlet becomes the agent's toolbox, behind your own RBAC."
  - q: "Can I create full stack apps with Magic?"
    a: "Yes. Describe your app to an MCP-connected orchestrator LLM, and it creates the database, generates a secured CRUD API with the Endpoint Generator, and builds the frontend - served straight from your cloudlet's /etc/www/ folder. A working CRM has been built this way 100% autonomously in 7 minutes, for roughly $0.50 in inference."
  - q: "Do I need to know how to code?"
    a: "No. The Hyperlambda Generator transforms plain English into working code, the Endpoint Generator creates complete CRUD APIs from your database without a single line of code, and AI prompt bars throughout the dashboard write SQL and Hyperlambda for you."
  - q: "What is Hyperlambda?"
    a: "Magic's declarative orchestration language - technically a relational file format for execution trees. Machines can generate it reliably, which is what makes Magic's AI code generation possible. You don't need to master it to use Magic."
  - q: "What is the Hyperlambda Generator?"
    a: "Magic's proprietary SLM, fine-tuned with more than 600,000 training snippets, turning natural language into working Hyperlambda in seconds - and it cannot hallucinate function invocations, since every generated slot is verified against your cloudlet."
  - q: "How does Magic work with AI agents such as Claude?"
    a: "Magic has an integrated MCP server with OAuth. Connect Claude, Claude Code, Cursor, Codex or any MCP client, and every endpoint in your cloudlet becomes a tool the agent can invoke - obeying your RBAC - while the agent can also create new endpoints for itself on demand."
  - q: "Can I create an AI chatbot from my website?"
    a: "Yes. The Chatbot Wizard crawls your website, turns your content into RAG training data, and gives you an embeddable chatbot in minutes - which you can then refine with training data, widgets, and AI functions."
  - q: "Can Magic wrap my existing database?"
    a: "Yes. Point the Endpoint Generator at any MySQL, PostgreSQL, SQL Server, MariaDB or SQLite database, and it generates a complete, secured CRUD API from your existing schema in seconds."
  - q: "Is Magic secure?"
    a: "Magic is built on JWT authentication and role based access control, with every endpoint declaring which roles may invoke it. It also acts as an OAuth server, and supports OIDC for federated sign-in through providers such as Google and Microsoft."
  - q: "Is Magic open source, and where can I run it?"
    a: "Yes, Magic is 100% open source. Run it locally with one Docker command, deploy it to any VPS, or use AINIRO.IO's professional hosting - a managed cloudlet with backups and HTTPS out of the box."
---

Magic Cloud, or Magic for short, is a backend software development platform that creates most of your code _"automagically"_, by leveraging meta programming, declarative programming, AI, low-code, and no-code. This allows you to focus on creative tasks, while having the machine create the boring parts.

> Where the Machine Creates the Code!

Magic gives you everything you need to build your entire backend — your database, your API, your business logic, your background jobs, and your authentication and authorisation — and to host it, all in one place. And when you connect it to an AI-based [MCP](/tutorials/how-to-connect-the-mcp-server/) client such as Claude, or point it at OpenAI, the machine can generate your frontend too — turning a plain-English description into a working full stack application.

This also makes Magic exceptionally well suited for building AI agents, and _especially database-driven agents_. Because your entire backend and its data become secured tools the AI can invoke over MCP, an agent can query and update your database, call your endpoints, and even create brand new endpoints on demand — all behind your own authentication and role based access control, with your data never leaving your database.

Magic is 100% open source, and you can find its [GitHub repo here](http://github.com/polterguy/magic). If you don't want to mess with hosting yourself, you can check out our professional or enterprise hosting plans [here](https://ainiro.io).

## What can you use Magic for?

Magic is a general purpose backend platform, but some things it is _particularly_ good at. Below are the most important use cases.

* **Full stack apps** - CRM systems, admin panels, booking systems, internal tools - a database, a secure API, and a frontend, generated from natural language in minutes
* **Database-driven AI agents** - AI agents that query and update _your_ database, invoke _your_ endpoints, and even create new tools for themselves on demand - all behind your own RBAC
* **A kick-ass MCP server** - connect Claude, Cursor, Codex, or any MCP client to your cloudlet, and every endpoint becomes a tool the agent can invoke
* **Custom AI chatbots** - crawl your website, and get an embeddable chatbot trained on your own content, with widgets and AI functions
* **Wrapping legacy databases** - point Magic at an existing MySQL, PostgreSQL, SQL Server or MariaDB database, and get a secured, modern web API in seconds
* **Managing your databases** - design schemas visually, execute SQL from the browser, or let an AI agent administer your database through natural language
* **Web APIs without code** - CRUD endpoints, custom SQL endpoints, aggregations and keyword search - generated, not written
* **Background jobs and automation** - scheduled tasks written in Hyperlambda, or generated from plain English descriptions
* **Hosting static websites and SPAs** - your cloudlet serves files from /etc/www/, turning it into a web server for landing pages and single-page apps, right next to the APIs powering them
* **Email, workflows and integrations** - SMTP, Stripe, Shopify, WordPress, HubSpot, NetSuite and more, through installable plugins

## AI Generated Code - "Vibe Coding"

With Magic you can sometimes accomplish in some few minutes what requires weeks of coding with a more
traditional platform. The CRM app below was created with Qoder in **7 minutes** over Magic's [MCP server](/tutorials/how-to-connect-the-mcp-server/), using Kimi K3, costing a grand total of **$0.50** in inference. It's a full stack app; A SQLite database with 3 tables, a secure API wrapping it, and authentication and authorisation - All generated from natural language.

![A home grown CRM app with clients, notes and emails, vibe coded in 7 minutes for 50 cents](/assets/images/home-grown-app.png)

Notice, the AI doesn't need to create your database from scratch - Legacy databases can be just as easily wrapped, turning your existing MySQL, PostgreSQL, SQL Server, or SQLite database into a secure API and a working app in minutes.

## MCP Support

Magic contains an integrated MCP server, with OAuth, allowing you to connect it to.

* Claude Code
* Codex
* Cursor
* Qoder
* Grok

The above is just some of what I've tried it with, but it should work with everything having MCP support. To get started, check out [how to connect the MCP server](/tutorials/how-to-connect-the-mcp-server/).

![The dashboard's MCP card with the URL an AI agent needs to connect to your cloudlet](/assets/images/mcp-dashboard-copy-url.png)

## The Hyperlambda Generator

At the heart of Magic you'll find the [Hyperlambda Generator](/dashboard/hyperlambda-generator/) — our own proprietary SLM (Small Language Model), fine-tuned with more than 600,000 training snippets, transforming natural language into working Hyperlambda code in typically 1.5 to 5 seconds. Unlike general purpose LLMs, it cannot hallucinate function invocations — every slot the generated code invokes is verified against the slots that actually exist in your cloudlet before the code is returned to you.

Combined with the [MCP server](/tutorials/how-to-connect-the-mcp-server/), this allows an AI agent such as Claude to create new tools for itself on demand — describing the endpoint it needs in plain English, and having the generator create it in seconds.

![The Hyperlambda Generator transforming an English description into a working HTTP endpoint](/assets/images/hyperlambda-generator.png)

## The Magic Dashboard

Magic's purpose is to help you with your backend, and it comes with a dashboard allowing you to manage all aspects of your backend. The dashboard contains UI components for most things you'll need when creating and maintaining your API and backend code. Below you can find some general information about some of its most important components.

![Screenshot of the Magic dashboard with key numbers, the MCP card, and the Chatbot Wizard](/images/dashboard.jpeg)

## Hyper IDE

Magic contains its own IDE or integrated development environment. [Hyper IDE](/dashboard/hyper-ide/) provides syntax highlighting 
and autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications, by executing your endpoint without ever having to leave your IDE. Magic even has its own backend _"vibe coding"_ prompting mechanisms, allowing you to generate Hyperlambda from natural language using generative AI.

![Screenshot of Magic's Hyper IDE with autocomplete open for Hyperlambda slots](/images/hyper-ide-actions.jpg)

Hyper IDE also integrates with our Machine Learning component, built on top of OpenAI, allowing you to write your requests in plain English, and have Hyper IDE and OpenAI automatically generate code for you solving your problem.

> With Hyper IDE manually writing code is optional

## The Endpoint Generator

The [Endpoint Generator](/dashboard/endpoint-generator/) allows you to wrap any database you have in CRUD API endpoints. It reads
meta data from your database, and automatically generates a web API for you. The generated API is
secured according to your instructions, and can be modified after it's created.

![Screenshot of Endpoint Generator allowing you to generate CRUD apps wrapping your database of choice](/images/backend-crud.jpg)

The Endpoint Generator takes care of referential integrity, validators, authentication, and authorisation -
While allowing you to declaratively tell it how to generate your API, in addition to having lots of
additional features simplifying your life as a software developer.

By combining the Endpoint Generator with the [Hyperlambda Generator](/dashboard/hyperlambda-generator/) and an AI agent connected over MCP, you can create entire backends straight from natural language.

## The SQL Endpoint Generator

Magic allows you to create HTTP endpoints using SQL. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find this component in the Endpoint Generator,
in its _"SQL Endpoint Generator"_ tab. Choose your database, provide some SQL, add arguments that you
reference in your SQL, and click the _"Generate"_ button.

![Screenshot of the SQL Endpoint Generator allowing you to create HTTP endpoints with SQL](/images/sql-web-api.jpg)

The SQL endpoint generator allows you to secure your endpoints, declare what arguments your endpoints can handle,
use all 5 most common HTTP verbs for your endpoints, etc. You can use it with SQL Server, MySQL, MariaDB,
PostgreSQL, or SQLite - And if you don't know SQL, then SQL Studio even has integrated support for generating SQL from natural language.

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

![Screenshot of the Machine Learning component listing your AI models](/assets/images/machine-learning-types.jpeg)

## Create an AI chatbot

Creating your own AI chatbot with Magic takes minutes. Provide the Chatbot Wizard with your website's URL, and it crawls your site, scrapes each page, and turns your content into training data - reporting its progress in real time as it works its way through the site. A few minutes later you have a chatbot trained on your own content, ready to embed on your website.

![Screenshot of the dashboard crawling and scraping a website to create an AI chatbot](/assets/images/scraping-website-for-chatbot-data.png)

## User management

Magic Cloud allows you to create and administer users, by giving you a graphical user interface, allowing you to manage your application's users and roles, using a role based access control (RBAC) component. Provide access to modules and components according to what roles your users belong to, and make sure only authorised users have access to private and secured data.

![Screenshot of the Users & roles component managing users and their access rights](/images/auth.jpg)

## The task manager

Magic Cloud allows you to create and administer tasks. A task is a background job, that is persisted into your database as Hyperlambda, and it can either be executed by a _"trigger"_ occurring somewhere else in your system, or periodically scheduled to execute repeatedly, or at some specific date and time in the future. The task manager allows you to easily manage your tasks, edit them, and create new tasks as you see fit.

![Screenshot of creating a Hyperlambda task in the Task Manager](/images/scheduling-task.jpg)

## Plugins

Magic Cloud also contains its own _"App Store"_, allowing you to rapidly install some plugin solving some particular need you might have in your own applications. Some example plugins are listed below;

* Stripe payment integrations
* Registration workflow actions
* Shopify AI chatbot integration
* WordPress AI chatbot integration
* Several example SQLite databases
* Etc, etc, etc

![Screenshot of the Plugins component, Magic's integrated App Store](/images/bazaar.jpg)

## The integrated log

Magic Cloud also comes with an integrated log component, allowing you to browse your server log, giving you control over events occurring that might somehow have consequences for your system.

When you create your own Hyperlambda applications, you can also create log entries as you see fit, to log important events, such as deleting records, executing tasks, registering users, etc.

![Screenshot of the Log component while browsing server log items](/images/log.jpg)

## Custom AI chatbots

You can also use Magic to create your own custom AI chatbot, for then to embed it into your website. The Chatbot Wizard component in Magic will ask you for your OpenAI API key, for then to scrape your website generating a RAG database in the process. The end result allows your users to ask questions related to your website, and have the chatbot answer how you want it to answer questions.

It works by scraping your website, generating training data in the process, for then to end up with a custom _"machine learning model"_ (based upon RAG), that answers questions according to your training data. You can try out such a chatbot by clicking the button in the bottom / right corner of this page, and ask it any question about Magic Cloud. This chatbot was created by scraping this website. At AINIRO we also deliver such chatbots as one of our services. Read more about [our AI chatbots here](/dashboard/chatbot-wizard/).

![Screenshot of an AI chatbot answering questions about Hyperlambda and Magic](/assets/images/integrated-chatbot.jpeg)

{% include faq.html %}

## The goal of the project

The goal of the project is to make it easier to produce high quality and scalable code, much faster, without security holes, in an extremely scalable runtime. AKA ...

> Where the Machine Creates the Code!
