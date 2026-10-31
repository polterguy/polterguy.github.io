---
title: Endpoint Generator
description: The Endpoint Generator reads your database's metadata and automatically generates a secured CRUD API wrapping it, wraps your own SQL into endpoints, safely executes caller-supplied code inside a role-based sandbox, searches a machine learning type, and imports third party APIs from their OpenAPI specifications - with no manual coding required.
header:
  image: /assets/images/hero/endpoint-generator.webp
  og_image: /assets/images/hero/endpoint-generator-og.png
  image_description: The Endpoint Generator
faq:
  - q: "What does the Endpoint Generator do?"
    a: "It reads metadata from your database and automatically generates a complete CRUD web API wrapping it, secured according to your instructions. What would normally take weeks of coding is done in seconds."
  - q: "Which databases can it wrap?"
    a: "Any MySQL, PostgreSQL, SQL Server, MariaDB, or SQLite database - including existing legacy databases, which makes it a fast way to put a modern, secure API on top of an old system."
  - q: "Which endpoint types can it generate?"
    a: "POST, GET, PUT and DELETE endpoints for each table, plus additional GET endpoints such as count, aggregate, distinct, and a keyword density search endpoint."
  - q: "What is keyword density search?"
    a: "A search endpoint that ranks each row by how many of your keywords it matches, sorting by most matches first. It is a good substitute for RAG and VSS - no embeddings, no vector database, no AI inference - yet often yields surprisingly relevant results."
  - q: "Is the generated API secure?"
    a: "Yes. You declare which roles can invoke each verb, and the generator takes care of authentication, authorisation, validators, and referential integrity - plus optional logging of create, update and delete invocations."
  - q: "Does caching apply to all generated endpoints?"
    a: "No. Caching, implying the Cache-Control HTTP header, is only applied to GET endpoints in this component."
  - q: "What is the fastest way to create an API?"
    a: "The dashboard's landing page has an 'API Wizard' card starting a guided version of the Endpoint Generator - it preselects every table in your database, and when generation is done it links you directly to your new endpoints and to user management."
  - q: "Can I wrap somebody else's API instead of a database?"
    a: "Yes. The Import API tab reads an OpenAPI specification - OpenAPI 3.x or Swagger 2.0, JSON or YAML - and generates Hyperlambda endpoints wrapping whichever operations you select, complete with arguments, validators and documentation taken from the specification."
  - q: "Where is the credential for an imported API stored?"
    a: "In your configuration, never in the generated files. You nominate a configuration key, and the generated endpoints read the credential from it at invocation time, which keeps your files safe to check into source control."
  - q: "Do imported endpoints work as MCP tools?"
    a: "Yes. The importer writes the operation's summary as the file level comment and each argument's documentation as a comment above that argument, which is what Magic exposes as the tool's description and its arguments' descriptions - so an imported API becomes a set of self describing tools for an AI agent."
  - q: "Can I wrap my own SQL in an endpoint?"
    a: "Yes. The SQL endpoint tab lets you provide any SQL statement, declare arguments you reference as @name in the SQL, choose an HTTP verb and authorisation, and generate a secure endpoint wrapping it. The AI prompt bar can even write the SQL for you, and you can load saved snippets or import .sql files."
  - q: "What is the Sandbox API tab?"
    a: "It generates one endpoint that safely executes code its own callers supply - Hyperlambda, or plain English turned into Hyperlambda - inside a whitelist you define per role. Callers can only reach the functions you granted, a function you did not grant does not exist as far as their code is concerned, and a hallucinated function is refused before anything runs."
  - q: "How do I limit what a Sandbox API caller can do?"
    a: "You build a policy from an 'everybody' base vocabulary plus per-role rules that add functions on top. A caller runs with the union of the functions their roles grant, so you can, for example, give one role access to a specific database while another role cannot reach it. The rate limit and the execution timeout are set per role too, and root is trusted completely - never sandboxed, throttled, or timed out."
  - q: "How can a role run complex business logic without access to the raw resources behind it?"
    a: "Put the logic in a Hyperlambda file, and grant the role that one file with the Execute files wizard instead of the functions the file uses. The file runs fully trusted, so it can read a database or call an API the role itself can never touch - the caller can only run exactly what the file does, with the arguments it accepts. You review the file once, and the role never gets raw access."
  - q: "Can the Sandbox API run a natural-language instruction?"
    a: "Yes. Choose the natural-language or 'both' input mode, and the endpoint sends the instruction to the Hyperlambda Generator, verifies every function the generated code references actually exists, and runs it inside the same whitelist. The response says whether it executed, and why not when it was refused."
  - q: "Does the Sandbox API endpoint work as an MCP tool?"
    a: "Yes. The generator writes the endpoint's file level comment to match its input mode, which Magic exposes as the tool's description, and the comment even tells the calling model how to discover its own capability surface - by calling the tool with describe set to true. Each role's one-line description is added to the comment too. An AI agent can therefore learn exactly which functions a given sandbox permits before it calls it."
  - q: "How does a caller find out what a Sandbox API permits?"
    a: "It calls the endpoint with describe set to true instead of sending code. The endpoint answers with the functions that particular caller may use - each with its pinned value, if it has one - plus the rate limit and timeout that apply to it. Nothing is executed, and the call does not count against the rate limit."
  - q: "Can I discover Sandbox API endpoints without MCP?"
    a: "Yes. Every time the generator saves a Sandbox API endpoint, it lists the endpoint in /.well-known/hyperlambda-agent on your cloudlet - a JSON document an agent can fetch without any prior setup, then call each listed endpoint with describe set to true."
  - q: "How do I check what a particular role can really do?"
    a: "Open the endpoint in the Endpoints component, pick the role in the Run as dropdown, and invoke it with describe set to true. Magic mints a short lived token for that role and calls the endpoint with it, so you see exactly what a caller in that role would see."
  - q: "What is the Search endpoint tab?"
    a: "It generates one endpoint that searches the training snippets of a single machine learning type, by keyword (BM25), by meaning (vectors), or both. The type, the search mode and what comes back are fixed in the endpoint, so callers send only a query. It is retrieval only - no AI model is invoked."
  - q: "Does a search endpoint cost anything per call?"
    a: "Not when it searches by keyword - that needs no OpenAI key and no vectors. Searching by meaning, or by both, spends one OpenAI embedding on every call, which is why the tab applies a rate limit by default and can let the caller cache answers."
moved_anchors: {"additional-endpoint-types": "/dashboard/endpoint-generator/crud-generator/#additional-endpoint-types", "arguments-and-documentation": "/dashboard/endpoint-generator/import-api/#arguments-and-documentation", "as-an-mcp-tool-and-discovery-without-mcp": "/dashboard/endpoint-generator/sandbox-callers-and-discovery/#as-an-mcp-tool-and-discovery-without-mcp", "asking-what-is-permitted---describe": "/dashboard/endpoint-generator/sandbox-callers-and-discovery/#asking-what-is-permitted---describe", "authentication-towards-the-upstream-api": "/dashboard/endpoint-generator/import-api/#authentication-towards-the-upstream-api", "business-logic-without-raw-access": "/dashboard/endpoint-generator/sandbox-business-logic/#business-logic-without-raw-access", "capability-wizards": "/dashboard/endpoint-generator/sandbox-api/#capability-wizards", "endpoint-generator-internals": "/dashboard/endpoint-generator/crud-generator/#endpoint-generator-internals", "endpoint-generator-settings": "/dashboard/endpoint-generator/crud-generator/#endpoint-generator-settings", "endpoint-generator-settings-complete-list": "/dashboard/endpoint-generator/crud-generator/#endpoint-generator-settings-complete-list", "how-the-code-is-checked-and-run": "/dashboard/endpoint-generator/sandbox-api/#how-the-code-is-checked-and-run", "how-to-use-the-endpoint-generator": "/dashboard/endpoint-generator/crud-generator/#how-to-use-the-endpoint-generator", "how-to-use-the-sql-endpoint-generator": "/dashboard/endpoint-generator/sql-endpoints/#how-to-use-the-sql-endpoint-generator", "http-verbs": "/dashboard/endpoint-generator/crud-generator/#http-verbs", "import-api---wrapping-a-third-party-api": "/dashboard/endpoint-generator/import-api/", "input---hyperlambda-natural-language-or-both": "/dashboard/endpoint-generator/sandbox-api/#input---hyperlambda-natural-language-or-both", "request-bodies": "/dashboard/endpoint-generator/import-api/#request-bodies", "root-throttling-and-the-timeout": "/dashboard/endpoint-generator/sandbox-callers-and-discovery/#root-throttling-and-the-timeout", "search-endpoint---searching-a-machine-learning-type": "/dashboard/endpoint-generator/search-endpoint/", "settings-for-the-sql-generator": "/dashboard/endpoint-generator/sql-endpoints/#settings-for-the-sql-generator", "testing-an-endpoint-as-a-role": "/dashboard/endpoint-generator/sandbox-callers-and-discovery/#testing-an-endpoint-as-a-role", "the-api-wizard---the-guided-flow": "/dashboard/endpoint-generator/crud-generator/", "the-policy---base-vocabulary-plus-per-role-grants": "/dashboard/endpoint-generator/sandbox-api/#the-policy---base-vocabulary-plus-per-role-grants", "the-sandbox-api-generator": "/dashboard/endpoint-generator/sandbox-api/", "the-sql-endpoint-generator": "/dashboard/endpoint-generator/sql-endpoints/", "who-may-call": "/dashboard/endpoint-generator/sandbox-callers-and-discovery/#who-may-call"}
---

The Endpoint Generator component allows you to automatically generate an HTTP CRUD web API wrapping your database of choice. The endpoint generator component works by reading meta data from your database, which it then uses to generate Hyperlambda HTTP endpoints for you automatically.

<img src="/images/backend-crud.webp" alt="Screenshot of the Endpoint Generator generating CRUD HTTP endpoints wrapping an SQL database" loading="lazy" width="2400" height="1500">

If you use the generator on for instance the _"SQLite Sakila"_ database that you can find as a [plugin](/dashboard/plugins/), Magic will create more than 3,000 lines of Hyperlambda code for you automatically, resulting in some roughly 100 HTTP endpoints for you, providing you with all CRUD operations towards all tables in your database.

Magic can also generate an API wrapping your existing databases. If you want to use your existing databases as input, you'll have to provide Magic with a connection string that allows it to connect to your database. You can do this through the [databases](/dashboard/databases/) component.

## In this section

* [CRUD Endpoint Generator](/dashboard/endpoint-generator/crud-generator/): The fastest way to use the generator is through the "API Wizard" card on the dashboard's landing page.
* [SQL Endpoint Generator](/dashboard/endpoint-generator/sql-endpoints/): The SQL endpoint generator component allows you to generate an API endpoint wrapping an SQL statement.
* [Sandbox API Generator](/dashboard/endpoint-generator/sandbox-api/): The "Sandbox API" tab generates a single endpoint that safely executes code its own callers supply.
* [Sandbox API - Business Logic Without Raw Access](/dashboard/endpoint-generator/sandbox-business-logic/): A whitelist answers "which functions may this role call?" Often the better question is "which results may this role get?" A role that should be able to see your top customers does not need [data.conne
* [Sandbox API - Callers, Throttling and Discovery](/dashboard/endpoint-generator/sandbox-callers-and-discovery/): Two settings sit above the policy.
* [Search Endpoint](/dashboard/endpoint-generator/search-endpoint/): The "Search endpoint" tab generates a single HTTP endpoint that searches the training snippets of one machine learning type and returns the best matches.
* [Import API](/dashboard/endpoint-generator/import-api/): The fifth tab in the Endpoint Generator, "Import API", works the other way around from the other four.

{% include faq.html %}
