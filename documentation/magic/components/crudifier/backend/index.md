---
title: Create an HTTP CRUD web API in 1 second
description: The backend CRUD generator allows you to create a CRUD API wrapping your database in seconds. Magic will read meta data from your database, and automatically create all required code for you.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-backend-crud.jpg"
---

# The Endpoint Generator component

The endpoint generator component allows you to automatically generate an HTTP CRUD web API wrapping your database
of choice. This component is the heart of the Low-Code and Automation parts of Magic, and allows you to generate
an HTTP web API wrapping your database by clicking a button.

![Backend CRUD generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

If you use the generator on for instance the _"SQLite Sakila"_ database that you can find as a plugin,
Magic will create more than 3,000 lines of Hyperlambda code for you automatically, resulting in some
roughly 100 HTTP endpoints for you, providing you with all CRUD operations towards all
tables in your database - However, Magic can also generate an API wrapping your existing databases. If you
want to use your existing databases as input, you'll have to provide Magic with a connection strings
that allows it to connect to your database. You can do this through the _"Databases"_ component.

To use the endpoint generator component you must first select a database. Then you can optionally configure the
CRUD process for individual tables, such as configuring what URL your CRUD API should use, whether or
not to turn on caching of HTTP GET endpoints, what authorisation requirements each endpoint should have,
etc.

![Configuring CRUD endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/configuring-crud.jpg)

The backend CRUD generator creates 5 HTTP endpoints by default for each table, if it can. One endpoint
for all CRUD operations, and a 5th endpoint to count items.

## Backend generator settings

Once you have selected a database and a table, you can override individual settings for how Magic should
create CRUD endpoints wrapping your table. Below is a screenshot where we have chosen to publish SignalR socket
messages upon write invocations to our table, implying create, update, and delete invocations. You can also turn
on or off specific columns, preventing Magic from accepting values for these columns, for individual CRUD verbs.
If you have a read only type of column for instance, that should only be set during _"create"_ invocations, you
can easily remove that field from your _"update"_ endpoint by expanding the column, and making sure Magic does
not accept new values to that column upon update invocations.

![CRUD backend settings](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crud-settings.jpg)

You can also override what URLs your endpoints should use, what authorisation requirements
your endpoints should have, in addition to a lot of other settings, such as turning on logging, caching, etc.
