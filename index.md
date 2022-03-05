---
title: Aista Magic Cloud, Open Source, Low-Code, and Hyperlambda
description: Aista Magic Cloud is an Open Source Low-Code web application generator allowing you to create your web apps by clicking a button.
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg
---

# Aista Magic Cloud, an open source low-code web application generator

Aista Magic Cloud is a low-code web application generator allowing you to generate your web apps
by clicking a button. It works by automatically wrapping your existing database into Hyperlambda HTTP CRUD web API
endpoints, for then to generate an Angular frontend for you based upon your web API.
[Magic Cloud is 100% open source](https://github.com/polterguy/magic) and you can freely use it in your
closed source projects.

![Hyperlambda HTTP CRUD generator screenshot](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

Magic supports MySQL, Microsoft SQL Server, and PostgreSQL, in addition to having basic NoSQL support. Magic
contains its own DSL called Hyperlambda, similar to YAML in structure, allowing you to _"declare"_ your logic with a
syntax resembling YAML. This makes it a perfect _"first programming"_ language due to that it's an extremely
high level abstraction eliminating most of the problems from traditional programming languages. You can easily
teach yourself Hyperlambda in a couple of hours.

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
you'd expect from an SQL Workbench type of component. The SQL Workbench works perfectly on any device you might
have allowing you to administrate your databases from your phone if required.

![Magic's web based SQL Workbench](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

You can also create your HTTP endpoints using nothing but SQL with Magic. Although it's obviously more convenient
to use a desktop computers as your primary development machine, you _can_ use all components in Magic from your phone
if required. Below is a video where we demonstrate how to use Hyper IDE from an iPhone.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/nP_4m8c_fT8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

* [Getting Started](/tutorials/getting-started/)
* [Tutorials](/tutorials/)
* [Docs](/documentation/)
