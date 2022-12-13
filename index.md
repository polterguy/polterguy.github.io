---
title: Getting started with Aista and Hyperlambda
description: This is the primary Aista Magic Cloud and Hyperlambda documentation
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg
---

# Getting started with Aista and Hyperlambda

The CRUD generator reads meta data from your database, for then to generate Hyperlambda backend code for
you automatically, wrapping your database of choice. Below is a screenshot of the CRUD generator.

![CRUD API generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

## Generate CRUD endpoints for your database

First you need a database. You can connect to an existing database in the Create/Databases menu item. Click
the _"Connect to database"_ tab, and make sure you use `{database}` as your database selector such
that Magic can dynamically connect to all databases in your database server. If you don't have a database yourself,
and only want to play around with Magic, you can find some example SQLite plugin databases in the same place.

Then click Create/Endpoint Generator. Choose your database and click _"Generate endpoints"_. You can also select
individual tables and configure these as you wish. This allows you to for instance apply authorisation
requirements for your individual endpoints, add reCAPTCHA requirements for invoking endpoints, publish web
socket messages as endpoints are invoked, log invocations to endpoints, etc.

When you are done generating your CRUD API, you can go to Manage/Endpoints to test your endpoints.
This component is similar to Swagger, and allows you to see which arguments your endpoints can handle,
to easily implement some kind of frontend. Below is a video demonstrating the entire process.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/h4s0bwEC_a4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Generate SQL endpoints

Magic allows you to create HTTP endpoints using only SQL. This allows you to compose some SQL statement,
and rapidly wrap it inside an HTTP endpoint. You can find also this component in the Endpoint Generator.
Choose your database, provide some SQL, add arguments that you reference in your SQL, and click the
_"Generate"_ button. Below is a screenshot of the process.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

## SQL Studio

In addition to the above, Magic contains a web based SQL Studio, allowing you to design your database visually,
in addition to execute any SQL you want to execute. SQL Studio supports syntax highlightning, autocomplete, and
all the following database types

* Microsoft SQL Server
* PostgreSQL
* MySQL
* MariaDB
* SQLite

![Aista's SQL Studio](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

Below is another screenshot of SQL Studio, but this time in SQL view.

![Aista's SQL Studio](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-studio-2.jpg)

## Hyper IDE

Magic also contains its own IDE or integrated development environment.
Hyper IDE provides syntax highlighting for most popular programming languages, in addition
to autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately see the result
of your modifications by executing your endpoint.

![Magic's Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

The real power of the CRUD Generator is that it generates code you can edit, with a declarative programming language
called Hyperlambda. If you need to add business logic to your generated CRUD endpoints, this is easily achieved
using Hyper IDE. Below you can find more information about Magic, such as tutorials and its reference documentation.

* [Tutorials](/tutorials/)
* [Docs](/documentation/)
