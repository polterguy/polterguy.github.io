---
title: Aista Magic Cloud, a low-code CRUD generator
description: Aista Magic Cloud is an open source low-code CRUD generator allowing you to create your CRUD apps by clicking a button.
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg
---

# A low-code CRUD generator

Aista Magic Cloud is a low-code CRUD generator allowing you to generate your CRUD apps
by clicking a button. It works by automatically wrapping your existing database into Hyperlambda HTTP CRUD web API
endpoints. [Magic Cloud is 100% open source](https://github.com/polterguy/magic) and you can freely use it in your
closed source projects. Magic supports MySQL, Microsoft SQL Server, and PostgreSQL, in addition to having basic NoSQL
support.

![CRUD API generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

## Getting started

First you need a database. You can connect to your existing database in the Management/Config menu item. Click
the button that says _"Add connection string"_ and make sure you use `{database}` as your database selector such
that Magic can dynamically connect to all databases in your database server. If you don't have a database yourself,
and only want to play around with Magic, you can find example databases in the Management/Plugins section.
Choose any plugin that starts with _"SQLite"_ and ends with _"DB"_, and click _"Install"_.

Then go to Tools/CRUD Generator. Choose your database and click _"Crudify all tables"_. You can also select
individual tables and configure these as you need. This allows you to for instance apply authorisation
requirements for your individual endpoints, add reCAPTCHA requirements for invoking endpoints, publish web
socket messages as endpoints are invoked, etc.

When you are done generating your CRUD API, you can go to Analytics/Endpoints to play with your endpoints.
This component is similar to Swagger, and allows you to see which arguments your endpoints can handle,
to easily implement some kind of frontend. Below is a video demonstrating the entire process.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/h4s0bwEC_a4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Hyper IDE, a web based IDE

Magic also contains its own IDE or integrated development environment, a fully fledged web based IDE accessible
from your phone if required. Hyper IDE provides syntax highlighting for most popular programming languages, in addition
to autocomplete for Hyperlambda. With Hyper IDE you can edit your code, save it, and immediately execute your
endpoints - And even automatically generate unit tests afterwards.

![Magic's Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

## Web based SQL "Workbench"

In addition to the above, Magic contains a web based SQL _"workbench"_, allowing you to execute SQL towards
your database of choice. This component works transparently towards SQL Server, MySQL, and PostgreSQL, and allows
you to save frequently used SQL snippets, and do basic administration of your databases.
The SQL component in Magic supports syntax highlighting on your tables, autocomplete, and most other features
you would expect from an SQL Workbench type of component. The SQL Workbench works perfectly on any device you might
have allowing you to administrate your databases from your phone if required.

![Magic's web based SQL Workbench](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

You can also create your HTTP endpoints using nothing but SQL with Magic. Although it's obviously more convenient
to use a desktop computers as your primary development machine, you _can_ use all components in Magic from your phone
if required. Below is a video where we demonstrate the Crudifier and Hyper IDE from an iPhone.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/nP_4m8c_fT8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

* [Getting Started](/tutorials/getting-started/)
* [Tutorials](/tutorials/)
* [Docs](/documentation/)
