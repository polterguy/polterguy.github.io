---
title: Create an HTTP CRUD web API in 1 second
description: The backend CRUD generator allows you to create a CRUD API wrapping your database in seconds. Magic will read meta data from your database, and automatically create all required code for you.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-backend-crud.jpg"
---

# Create an HTTP CRUD web API in 1 second

This component allows you to automatically generate an HTTP CRUD web API wrapping your database. This
component is the heart of the Low-Code and Automation parts of Magic, and allows you to generate
an HTTP web API wrapping your database by literally clicking a button. Below is a screenshot of
the component.

![Backend CRUD generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

If you use the crudifier on for instance the _"Sakila"_ database that comes with Magic out of the box,
Magic will create more than 3,000 lines of Hyperlambda code for you automatically, resulting in some
roughly 100 HTTP endpoints for you, providing you with every single CRUD operation towards every
single table in your database - However, Magic can also crudify your existing databases. If you
want to crudify your existing databases, you'll have to provide Magic with a connection strings
that allows it to connect to your database. The latter is done through
the [config](/documentation/magic/components/config/) component.

To use the component you must first select a database. Then you can optionally configure the
CRUD process for individual tables, such as configuring what URL your CRUD API should use, whether or
not to turn on caching of HTTP GET endpoints, what authorisation requirements each endpoint should have,
etc. Below is a screenshot of how this would look like.

![Configuring CRUD endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/configuring-crud.jpg)

The backend CRUD generator creates 5 HTTP endpoints by default for each table, if it can. To understand
how it works, you can check out [this article](/tutorials/database-crud/).

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
