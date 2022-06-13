---
title: Getting started with Aista Magic Cloud in 4 minutes
description: This is the getting started guide for Aista Magic Cloud for those in a hurry. In 4 minutes we guide you through everything.
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg
---

# Getting started with Aista Magic Cloud in 4 minutes

Aista Magic Cloud is a low-code CRUD generator allowing you to generate CRUD apps in one second
by clicking a button. It works by wrapping your database into Hyperlambda HTTP API endpoints. Below is the CRUD
generator that automatically creates your web API.

![CRUD API generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

## Generate CRUD endpoints for your database

First you need a database. You can connect to an existing database in the Management/Config menu item. Click
the button that says _"Add connection string"_ and make sure you use `{database}` as your database selector such
that Magic can dynamically connect to all databases in your database server. If you don't have a database yourself,
and only want to play around with Magic, you can find example databases in the Management/Plugins section.
Choose any plugin that starts with _"SQLite"_ and ends with _"DB"_, and click _"Install"_.

Then go to Tools/CRUD Generator. Choose your database and click _"Crudify all tables"_. You can also select
individual tables and configure these as you wish. This allows you to for instance apply authorisation
requirements for your individual endpoints, add reCAPTCHA requirements for invoking endpoints, publish web
socket messages as endpoints are invoked, log invocations to endpoints, etc.

When you are done generating your CRUD API, you can go to Analytics/Endpoints to play with your endpoints.
This component is similar to Swagger, and allows you to see which arguments your endpoints can handle,
to easily implement some kind of frontend. Below is a video demonstrating the entire process.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/h4s0bwEC_a4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Generate SQL endpoints

Magic allows you to create HTTP endpoints with SQL only. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find this component in the Tools/CRUD Generator/SQL section
of your dashboard. Choose your database, provide some SQL, add arguments that you reference in your SQL, and click
the _"Generate"_ button. Below is a screenshot of the process.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

## SQL Studio

In addition to the above, Magic contains a web based SQL Studio, allowing you to execute SQL towards
your database of choice. This component works transparently towards SQL Server, MySQL, SQLite, and PostgreSQL, and allows
you to save frequently used SQL snippets, and do basic administration of your databases.
The SQL component in Magic supports syntax highlighting on your tables, autocomplete, and most other features
you would expect from an SQL Workbench type of component. To trigger the autocompletion feature use CTRL+SPACE on Windows
or FN+CONTROL+SPACE on your mac. When you have created some SQL statement and saved it, you can load this SQL
from the SQL endpoint CRUD Generator to wrap it inside an HTTP SQL endpoint.

![Magic's web based SQL Workbench](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

## Hyper IDE

Magic also contains its own IDE or integrated development environment, a fully fledged web based IDE.
Hyper IDE provides syntax highlighting for most popular programming languages, in addition
to autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications by executing your endpoint using the menu dropdown button.

![Magic's Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

## Use Magic from anywhere!

Notice, although it's obviously more convenient to use a desktop computer as your primary development machine, you _can_
use all components in Magic from your phone if required. Below is a video where we demonstrate the Crudifier and Hyper IDE
from an iPhone.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/nP_4m8c_fT8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Below you can find more information about Magic, such as tutorials and its reference documentation.

* [Tutorials](/tutorials/)
* [Docs](/documentation/)
