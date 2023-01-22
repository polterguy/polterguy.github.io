---
title: Create an HTTP CRUD web API in 1 second
description: The backend CRUD generator allows you to create a CRUD API wrapping your database in seconds. Magic will read meta data from your database, and automatically create all required code for you.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg"
---

# The Endpoint Generator component

The endpoint generator component allows you to automatically generate an HTTP CRUD web API wrapping your database
of choice. This component is the corecomponent of the low-code and software development automation parts of Magic,
and allows you to generate a web API wrapping your database by clicking a button. The endpoint generator component
works by reading meta data from your database, which it then uses to generate Hyperlambda HTTP endpoints for you
automatically.

![Backend CRUD generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

If you use the generator on for instance the _"SQLite Sakila"_ database that you can find as a plugin,
Magic will create more than 3,000 lines of Hyperlambda code for you automatically, resulting in some
roughly 100 HTTP endpoints for you, providing you with all CRUD operations towards all
tables in your database - However, Magic can also generate an API wrapping your existing databases. If you
want to use your existing databases as input, you'll have to provide Magic with a connection strings
that allows it to connect to your database. You can do this through the _"Databases"_ component.

## How to use the endpoint generator

To use the endpoint generator component you must first select a database. Then you can optionally configure the
CRUD process for individual tables, such as configuring what URL your CRUD API should use, whether or
not to turn on caching of HTTP GET endpoints, what authorisation requirements each endpoint should have,
etc. If you deselect all tables and select only one table, you get a lot more options
to choose from. This is useful if you need additional control over how your API endpoints are generated,
and what results the endpoint generator should give you.

![Configuring CRUD endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/configuring-crud.jpg)

The backend CRUD generator creates 5 HTTP endpoints by default for each table. One endpoint
for all CRUD operations, and a 5th endpoint to count items. If your table does not have a primary key,
it will not be able to generate delete or update endpoints. If your primary key has a default value,
it will not generate endpoint code requiring a primary key value for its create endpoints. In general,
the endpoint generator tries to intelligently choose defaults for your tables as it generates your backend.
However, it is not always able to choose correctly for you, so you might want to sanity check its result
after you've generated your backend.

## Backend generator settings

Once you have selected a database and a table, you can override individual settings for how Magic should
create CRUD endpoints wrapping your table. Below is a screenshot where we have chosen to publish SignalR socket
messages upon write invocations to our table, implying create, update, and delete invocations. You can also turn
on or off specific columns, preventing Magic from accepting values for these columns, for individual CRUD verbs.
If you have a read only type of column for instance, that should only be set during _"create"_ invocations, you
can easily remove that field from your _"update"_ endpoint, making sure Magic does not accept new values to that
column when its update endpoint is invoked.

![CRUD backend settings](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crud-settings.jpg)

You can also override what URLs your endpoints should use, what authorisation requirements
your endpoints should have, in addition to a lot of other settings, such as turning on logging, caching, etc.

## Backend generator settings

Below is a complete list of what settings you can apply when generating your endpoints. Notice, some of these
settings are only possible to apply if you've selected only _one_ table.

* What fields each CRUD endpoint accepts
* Display as which is only relevant for foreign keys, and only used when generating a frontend later, allowing you to declare one string field in the referenced table that you can do lookups from later when generating a frontend
* Template being for instance email, url, phone, etc, which changes the way the field is displayed later as you generate a frontend
* Authorisation requirements for each CRUD endpoint, allowing you to declare which role a user must have to be able to invoke your endpoints
* Primary and secondary URL, allowing you to tell the backend generator what URLs to generate for a particular table
* Paging and sorting, allowing you to turn on or off paging of data and sorting of data
* Turning on or off logging when your create, update and delete endpoints are invoked
* reCAPTCHA value, and what endpoint to apply reCAPTCHA for, allowing you to tell the backend generator that you want to apply reCAPTCHA for the create, read, update or delete endpoint. Notice, Magic is using reCAPTCHA version 3 from Google
* Caching, implying HTTP cache, or the _"Cache-Control"_ HTTP header, and whether or not to turn on public cache or not, where public caching allows proxies to cache your endpoint's result
* Whether or not _"write"_ endpoints should publish socket messages, where write endpoints implies create, update and delete. If you turn on publishing of socket messages here, a socket message with the name of the database, table, and HTTP verb will be published as the endpoint is invoked. If you turn on publishing of socket messages, you can optionally declare what type of authorisation the socket message will require in order to deliver the message to connected users
* Left joins, allowing you to declare whether or not you want to join on referenced tables or not, implying if a field is a foreign key, it will in addition to giving you all columns from your specific table, also pull in one string field from the referenced table as it's returning data from your read endpoint
* Verbose filtering, which if turned on, will create a lot more arguments, providibng you with much more filtering capabilities for your generated endpoints
* Overwrite, which if true, will overwrite an existing endpoint. Byt default, the backend generator will _not_ overwrite existing files unless you explicitly tell it to do so

In addition to the above settings, the backend generator also allows you to declare Hyperlambda code that is added to
your endpoint. This is typically useful if you want to add validators, to for instance validate an email field being a
valid email address, etc.

## Backend generator internals

The backend generator will actually create 5 files for you, one file for each CRUD verb, and one file to count items.
These files will be Hyperlambda files, and you can see these after the process is done by
using [Hyper IDE](/documentation/magic/components/hyper-ide) and expand your _"modules"_ folder. The generated Hyperlambda
will basically be wrappers around the **[data.connect]** slot, in addition to one of the following slots, depending
upon which CRUD verb the file you're looking at is wrapping.

* __[data.create]__ - The Hyperlambda slot for creating new items in your database
* __[data.read]__ - The Hyperlambda slot for reading items from your database
* __[data.update]__ - The Hyperlambda slot for updating items in your database
* __[data.delete]__ - The Hyperlambda slot for deleting items from your database
