---
title: Plugins
description: Extend your Magic cloudlet with plugins from the integrated App Store — Stripe payments, Shopify and WordPress chatbots, example databases, and more.
header:
  image: /assets/images/hero/plugins-dash.png
  og_image: /assets/images/hero/plugins-dash-og.png
  image_description: The Plugins component
faq:
  - q: "What is the Plugins component?"
    a: "Magic's own 'App Store', letting you rapidly install backend micro services and applications solving particular needs - Stripe payments, registration workflows, AI chatbot integrations, MCP, OAuth, example databases, and more."
  - q: "What types of plugins exist?"
    a: "Two types: modules and frontends. Modules are backend micro services installed into your modules folder, while frontends are complete applications served from your frontend domain."
  - q: "Why can't I install frontends?"
    a: "Frontends cannot be installed if your backend and frontend dashboard run on the same host or domain - which is the case for the all-in-one (aio) image and the DigitalOcean deployment - since installed frontends need their own domain to be served from."
  - q: "Can I see what a plugin contains before installing?"
    a: "Yes. Click Details on any plugin to read its complete description and see exactly what it contains - for instance which workflow actions a module gives you - before deciding to install."
  - q: "How do plugins work under the hood?"
    a: "Installing downloads a ZIP file and unzips it into your modules folder, after which all Hyperlambda files inside its magic.startup folder are executed, taking care of initialisation such as creating databases and slots."
  - q: "Can I modify an installed plugin?"
    a: "Yes, you can edit its files with Hyper IDE - but if you do, you can no longer update the plugin from the App Store."
---

The Plugins component is Magic's integrated _"AppStore"_, and allows you to install backend micro services on the fly, without interrupting normal usage. It resolves towards AINIRO's repository of plugins, that contains several pre-fabricated backend micro services, serving some generic requirement, such as for instance Stripe payments, OpenAI helpers, and registration helpers. Most plugins automatically take care of creating their databases, and other things required to initialise the plugin.

![Screenshot of the plugins component allowing you to extend your cloudlet](/images/bazaar.jpg)

There are two _types_ of plugins; _modules_ and _frontends_. Modules are backend micro services, installed into your cloudlet's modules folder. Frontends are complete applications served from your frontend domain. Notice, frontends can _not_ be installed if your backend and your frontend dashboard are running on the same host or domain - which is the case for the all-in-one (aio) image and the [DigitalOcean deployment](/deploy/) - since installed frontends need their own domain to be served from.

Before installing anything, click the _"Details"_ button on a plugin. This shows you the plugin's complete description - what it does, and exactly what it contains - for instance which workflow actions a module gives you, allowing you to read through everything the plugin provides and make an informed decision before you install it.

![Screenshot of the Details dialog for a plugin, showing its description and workflow actions](/assets/images/plugin-details.jpeg)

## How plugins work in Magic

When you install a plugin, a ZIP file is downloaded from our plugins repository, and unzipped into your modules folder. After unzipping the file, all Hyperlambda files inside the _"magic.startup"_ folder will be automatically executed, allowing for startup and installation logic. And in fact, if you create your own micro service module using Hyperlambda, you should create such startup folders yourself, where you initialise your plugin, by creating slots your module depends upon, creating its initial database if it's needing a database, etc.

After you have installed a plugin, you can see its code by using [Hyper IDE](/dashboard/hyper-ide/), and expand the modules folder, for then to expand the folder where your plugin was installed, and look at its files. You can even immediately edit any files this way too, but if you do, you can no longer update your plugin. If your plugin creates a database of some sort, you can also look at your database using [SQL Studio](/dashboard/sql-studio/).

## Available plugins

Below is the catalogue of plugins currently available from the AppStore. The list grows over time, so you may find additional plugins in your dashboard.

* __ai-expert-system__ - A chat frontend for password-protected AI models, with OpenID Connect login, Stripe subscriptions, and full white-labeling — an _"AI SaaS in a box"_.
* __auth__ - Workflow actions and a ready-made registration workflow for user management, authentication, and authorisation.
* __charts__ - HTTP endpoints that render grouped and stacked charts as PNG images from numerical data.
* __hubspot__ - Integrate your cloudlet with HubSpot, reading and writing contacts, notes, and more.
* __hugging-face__ - Use Hugging Face as your LLM provider.
* __mcp__ - A Model Context Protocol server that exposes your dynamic endpoints as MCP tools.
* __natural-language-api__ - Expose secure APIs that take natural language as input, generate Hyperlambda, execute it, and return the result.
* __netsuite__ - NetSuite integration with REST and SuiteQL workflows and endpoints for administering records.
* __oauth__ - An OAuth 2.1 authorization server that lets standards-compliant clients log in and receive a Magic JWT.
* __ollama__ - Run any Ollama-supported LLM as your model.
* __openai__ - OpenAI-based workflow actions — context retrieval, querying, image creation, and vectorizing — you can chain together.
* __robo-crm__ - A small, extensible starter CRM, and an example of building AI-assistant style apps.
* __scraper__ - Automate scraping of multiple sites and spice URLs to build machine-learning training data.
* __serp-api__ - SERP API integration with AI functions and workflows for searching and analysing patents and the web.
* __shopify__ - Integrate with Shopify to import products as training snippets, track orders, and more.
* __shopping-cart-demo__ - An example AI-based shopping cart with products, a cart, and a checkout process.
* __slack__ - Interact with Slack from your cloudlet, for example escalating AI support queries to human agents.
* __sqlite-chinook__ - Installs the Chinook example SQLite database to experiment with the generators.
* __sqlite-northwind__ - Installs the Northwind example SQLite database to experiment with the generators.
* __sqlite-sakila__ - Installs the Sakila example SQLite database to experiment with the generators and SQL Studio.
* __stripe__ - Stripe integration with workflow actions for customers, payments, subscriptions, refunds, and webhooks.
* __stripe-subscription-templates__ - Out-of-the-box Stripe subscription support with role-based plans (depends on the Stripe plugin).
* __sys__ - System actions such as compiling C# code and executing shell commands.
* __together-ai__ - Use Together AI as your LLM provider.
* __utilities__ - Helper slots and workflow actions for AI chatbot functionality, such as emailing chat logs.
* __vibe-coding__ - API functions and endpoints for automating software development — files, databases, Hyperlambda, modules, and plugins — with an AI agent.
* __woocommerce__ - Integrate with WooCommerce to import products as training snippets.
* __wordpress__ - Import WordPress pages and posts through the REST API to create semantic training content.
* __xpert-system__ - The React and TypeScript AI Expert System chat frontend, with streaming, OIDC, Stripe, white-labeling, and rich Markdown rendering.

{% include faq.html %}
