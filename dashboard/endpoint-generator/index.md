---
title: Endpoint Generator
description: The Endpoint Generator reads your database's metadata and automatically generates a secured CRUD API wrapping it, with no manual coding required.
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
    a: "The dashboard's landing page has a 'Create an API from your data' card starting a guided version of the Endpoint Generator - it preselects every table in your database, and when generation is done it links you directly to your new endpoints and to user management."
  - q: "Can I wrap my own SQL in an endpoint?"
    a: "Yes. The SQL endpoint tab lets you provide any SQL statement, declare arguments you reference as @name in the SQL, choose an HTTP verb and authorisation, and generate a secure endpoint wrapping it. The AI prompt bar can even write the SQL for you, and you can load saved snippets or import .sql files."
---

The Endpoint Generator component allows you to automatically generate an HTTP CRUD web API wrapping your database of choice. This component is one of the core components of the Low-Code and software development automation parts of Magic, and allows you to generate a web API wrapping your database automatically. The endpoint generator component works by reading meta data from your database, which it then uses to generate Hyperlambda HTTP endpoints for you automatically.

<img src="/images/backend-crud.webp" alt="Screenshot of the backend Generator generating CRUD HTTP endpoints wrapping an SQL database" loading="lazy" width="2400" height="1500">

If you use the generator on for instance the _"SQLite Sakila"_ database that you can find as a [plugin](/dashboard/plugins/), Magic will create more than 3,000 lines of Hyperlambda code for you automatically, resulting in some roughly 100 HTTP endpoints for you, providing you with all CRUD operations towards all tables in your database.

Magic can also generate an API wrapping your existing databases. If you want to use your existing databases as input, you'll have to provide Magic with a connection string that allows it to connect to your database. You can do this through the [databases](/dashboard/databases/) component.

## API from your data - the guided flow

The fastest way to use the generator is through the _"Create an API from your data"_ card on the dashboard's landing page. This starts a guided version of the Endpoint Generator, walking you through three steps - _choose data_, _generate_, and _done_. The guided flow preselects every table in your database, since that is almost always what you want when creating an API from scratch, and if you haven't got a database of your own yet, it points you to the [databases](/dashboard/databases/) component to create or connect one first.

When generation is done, the guided flow tells you how many endpoints it created and where they live, and links you directly to the [endpoints](/dashboard/endpoints/) component - filtered to your new module such that you can try your API immediately - and to [users and roles](/dashboard/users-roles/), where you control who is allowed to invoke it.

## How to use the endpoint generator

To use the endpoint generator component you must first select a database. Then you can optionally configure the CRUD process for individual tables, such as configuring what URL your CRUD API should use, whether or not to turn on caching of HTTP GET endpoints, what authorisation requirements each endpoint should have, etc.

Notice, if you deselect all tables and select only one table, you get a lot more options to choose from. This is useful if you need additional control over how your API endpoints are generated, and what results the endpoint generator should give you.

<img src="/images/configuring-crud.webp" alt="Screenshot of configuring one individual table in the CRUD Backend Generator" loading="lazy" width="2400" height="1500">

The Backend Generator creates 5 HTTP endpoints by default for each table. One endpoint for each CRUD operation, and a 5th endpoint to count items. If your table does not have a primary key, it will not be able to generate delete or update endpoints. If your primary key has a default value, it will not generate endpoint code requiring a primary key value for its create endpoints. In general, the endpoint generator tries to intelligently choose defaults for your tables as it generates your backend. However, it is not always able to choose correctly for you, so you might want to sanity check its result after you've generated your backend.

## Additional endpoint types

In addition to the standard CRUD endpoints, the generator can optionally create a few extra query endpoints for a table. You enable these per table before you generate your backend.

* **Aggregate** - Creates an endpoint that returns the minimum, maximum, average, sum, or count for a column you specify, grouped by another column. The grouping column is mandatory, so the endpoint always returns your aggregate value per group. This lets you produce totals and statistics directly from your database, without writing any SQL yourself.
* **Distinct** - Creates an endpoint that returns the unique, distinct values from a column, allowing you to list every value that occurs in a column without duplicates.
* **Search** - Creates an endpoint that performs a _"keyword density search"_ across your table, ranking each row by how many of your keywords it matches, and sorting the result by _"most matches"_ first. This gives you a simple relevance-ranked, full-text style search endpoint out of the box. Keyword density search is actually a good substitute for RAG and VSS - it requires no embeddings, no vector database, and no AI inference, yet often yields surprisingly relevant results, making it a great low-cost alternative when you need search but don't need semantic understanding.

Below is how the result looks like in [Hyper IDE](/dashboard/hyper-ide/) after having generated all endpoint types for a table - one Hyperlambda file per endpoint, including the count, distinct, aggregate, group, and search endpoints.

<img src="/assets/images/generated-endpoints-tree.webp" alt="Screenshot of the generated endpoint files in Hyper IDE, one file per endpoint type" loading="lazy" width="2400" height="1500">

## Endpoint generator settings

Once you have selected a database and a table, you can override individual settings for how Magic should create CRUD endpoints wrapping your specified table. You can also turn on or off specific columns, preventing Magic from accepting values for these columns, also for individual CRUD verbs. If you have a read only type of column for instance, that should only be set during _"create"_ invocations, you can easily remove that field from your _"update"_ endpoint, making sure Magic does not accept new values to that column when its update endpoint is invoked.

<img src="/images/crud-settings.webp" alt="Screenshot of how to modify the authorisation settings for the Backend Generator" loading="lazy" width="2400" height="1500">

You can also override what URLs your endpoints should use, what authorisation requirements your endpoints should have, in addition to a lot of other settings, such as turning on logging, caching, etc.

## Endpoint generator settings complete list

Below is a complete list of what settings you can apply when generating your endpoints. Notice, some of these settings are only possible to apply if you've selected only _one_ table.

* What fields each CRUD endpoint accepts
* Authorisation requirements for each CRUD endpoint, allowing you to declare which role a user must have to be able to invoke your endpoints
* Primary and secondary URL, allowing you to tell the backend generator what URLs to generate for a particular table
* Paging and sorting, allowing you to turn on or off paging of data and sorting of data
* Additional GET endpoints, such as aggregate, distinct, and search endpoints, giving you more ways to query your table
* Turning on or off logging when your create, update and delete endpoints are invoked
* Caching, implying HTTP cache, or the _"Cache-Control"_ HTTP header, and whether or not to turn on public cache or not, where public caching allows proxies to cache your endpoint's result. Notice, caching is _only_ applied to GET endpoints in this component
* Overwrite, which if true, will overwrite an existing endpoint. By default, the endpoint generator will _not_ overwrite existing files unless you explicitly tell it to do so

## Endpoint generator internals

The endpoint generator will actually create 5 files for you, one file for each CRUD verb, and one file to count items. These files will be Hyperlambda files, and you can see these after the process is done by using [Hyper IDE](/dashboard/hyper-ide/) and expand your _"modules"_ folder. The generated Hyperlambda will basically be wrappers around the **[data.connect]** slot, in addition to one of the following slots, depending upon which CRUD verb the file you're looking at is wrapping.

* __[data.create]__ - The Hyperlambda slot for creating new items in your database
* __[data.read]__ - The Hyperlambda slot for reading items from your database
* __[data.update]__ - The Hyperlambda slot for updating items in your database
* __[data.delete]__ - The Hyperlambda slot for deleting items from your database

## The SQL endpoint generator

The SQL endpoint generator component allows you to generate an API endpoint wrapping an SQL statement. It is similar to the endpoint generator, but instead of automatically creating your SQL, it allows you to provide your own custom SQL, and then securely wrap your SQL into an HTTP endpoint. It allows you to create endpoints wrapping any of the 5 most popular HTTP verbs, takes care of authentication and authorisation, in addition to that it allows you to declare arguments to your endpoints.

<img src="/images/sql-web-api.webp" alt="Screenshot of how to create an HTTP endpoint using SQL in the Backend Generator" loading="lazy" width="2400" height="1500">

Notice, you don't have to write the SQL yourself. Below the SQL editor you'll find an input textbox that says _"Where the Machine Creates the Code"_ - describe the query you want in plain English, click _"Ask"_, and the AI generates the SQL for you, aware of your selected database and its schema. If the editor already contains SQL, your prompt is treated as a change instruction, allowing you to iterate until the query does exactly what you want, before wrapping it into an HTTP endpoint.

## How to use the SQL endpoint generator

You can find the SQL endpoint generator as an additional tab inside your endpoint generator. The SQL generator is much simpler to understand than the endpoint generator, since it has much less settings you can apply. However, the SQL endpoint generator obviously requires that you've got a solid understanding of SQL. The process to use the SQL endpoint generator to create an endpoint is as follows.

1. Choose your database
2. Choose an HTTP verb
3. Choose URL(s) for your endpoint
4. Select which roles are authorised to invoke your endpoint (optional)
5. Provide arguments to your endpoint (optional)
6. Write your SQL referencing arguments if you provided arguments in the above step

When you're done with the above, simply click the _"Generate"_ button, and you've got an HTTP endpoint wrapping your SQL.

## Settings for the SQL generator

The SQL generator allows you to override authorisation requirements, the URL of your endpoint, and which arguments your endpoint requires. The last part is important since it allows you to add arguments to your endpoint that you can reference in your SQL somehow. To reference an argument in your SQL, prefix your argument's name with an at character (@), implying if your argument is named _"foo"_, you'll have to reference your argument in your SQL as _"@foo"_.

Notice, arguments supplied to your SQL endpoint are obviously mandatory, since once you've generated your endpoint, there are no known mechanisms for removing the argument from your SQL. However, your arguments could be supplied as null values, at which point the resulting SQL would use the value null as a substitute for your argument.

<img src="/images/sql-arguments.webp" alt="Screenshot of how to declare an argument to your SQL endpoint in the Backend Generator" loading="lazy" width="2400" height="1500">

## HTTP verbs

The CRUD endpoint generator creates endpoints wrapping the POST, GET, PUT, and DELETE verbs, while the SQL endpoint generator can additionally wrap PATCH.

* POST - Typically used for creating or inserting new items
* GET - Typically used for retrieving or counting records
* PUT - Typically used for updating values in your database
* PATCH - Alternative to PUT with similar semantics, typically when adding new fields (SQL endpoint generator only)
* DELETE - Typically used when deleting records in your database.

{% include faq.html %}
