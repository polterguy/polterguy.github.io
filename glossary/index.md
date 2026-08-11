---
title: Glossary
description: The canonical name for every concept in Magic Cloud - what each term means, which synonyms are deprecated, and what things are called in the API where history differs from the docs.
---

This page is the single source of truth for terminology in Magic. Every concept has exactly one canonical name, used consistently across the dashboard and the documentation. Where the API, database, or file system uses a different name for historical reasons, the entry says so - those internal names are frozen forever, since renaming them would break existing systems.

If you find documentation or dashboard copy contradicting this page, that's a bug.

## Platform

* **Magic Cloud** (or just **Magic**) - The product as a whole; the backend, the dashboard, and Hyperlambda.
* **Cloudlet** - *Your* instance of Magic, wherever it runs - an AINIRO-hosted container, a Docker installation, or localhost during development. Everything in one cloudlet is yours: its database, its users, its endpoints, its files. *Deprecated synonyms: "your server", "your backend", "your Magic server".* Use "server" only when referring to the actual process, such as "the server log" or "the server returns 409".
* **Dashboard** - The web frontend you manage your cloudlet through.
* **Hyperlambda** - Magic's programming language; the code your cloudlet executes.
* **Slot** - A single Hyperlambda instruction, such as **[data.read]** or **[log.info]**. Slots are implemented in C# and invoked from Hyperlambda.
* **Endpoint** - An HTTP URL your cloudlet serves, implemented by a Hyperlambda file whose filename declares its verb, such as `customers.get.hl`.

## Modules and plugins

* **Plugin** - An installable package, added to your cloudlet with a single click from the Plugins component. *Internal name: the API calls the plugin repository the "Bazar".*
* **Module** - A folder inside `/modules/` containing a backend application - its endpoints, and optionally its frontend and database scripts. Installing a plugin gives you a module; the Endpoint Generator creates one; you can also write one by hand. In short: a plugin is how a module arrives, a module is what you have once it's there.
* **Core plugins** - Something different from the above: the open source C# projects making up Magic itself, such as `magic.lambda.logging`. These are documented under [Plugins](/plugins/) and are only relevant if you're extending Magic with C#.

## Machine learning

* **Model** - Your trained collection of training snippets, queried with RAG and VSS - what a chatbot answers from. *Internal name: the API and database call this a "type"* (`ml_types`), *for historical reasons.*
* **OpenAI model** - The language model doing the actual inference, such as gpt-5.6-luna. Never call this just "model" - that word is reserved for the entry above.
* **Training snippet** - One prompt/completion pair inside a model; the unit of RAG training data. Always written with its qualifier - never bare "snippet".
* **Chatbot Wizard** - The dashboard flow crawling a website and turning it into a working chatbot, backed by a model.
* **AI function** - A declared operation a chatbot or AI agent can invoke - Magic's equivalent of function calling / tools.
* **Frank** - AINIRO's AI support agent, trained on the Magic and Hyperlambda documentation, available from the dashboard.

## Creating things

* **Endpoint Generator** - The component generating a secured CRUD web API from your database's metadata, including its guided flow started from the *API Wizard* card on the dashboard's landing page. *Deprecated synonyms: "Generator", "Backend Generator", "CRUD generator". Internal name: the backend calls the process "crudify"* (`/system/crudifier/`).
* **SQL endpoint** - An endpoint wrapping a single SQL statement you provide, created from the Endpoint Generator's SQL tab.
* **Hyperlambda Generator** - The AI that writes Hyperlambda from natural language - powering the *"Where the Machine Creates the Code"* prompt bars throughout the dashboard.
* **Saved snippet** - A Hyperlambda or SQL snippet you save for later from the Hyperlambda Playground or SQL Studio. Always written with its qualifier, to keep it apart from training snippets.
* **Task** - A named piece of Hyperlambda your cloudlet stores and executes on demand or on schedule, managed in the Task Manager. The dashboard landing page's *Tasks* section executes them; the Task Manager component creates and schedules them.
* **Workflow** - A Hyperlambda file composed from reusable actions, typically assembled visually in Hyper IDE.
