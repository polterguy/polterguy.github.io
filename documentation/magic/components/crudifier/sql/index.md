---
title: Create an HTTP endpoint with SQL
description: Magic allows you to create HTTP endpoints using only SQL. You provide the SQL, and Magic automatically wires up everything else required to execute your SQL (securely) through HTTP.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg"
---

# Create an HTTP endpoint with SQL

The SQL component allows you to automatically generate an HTTP web API endpoint wrapping some arbitrary SQL statement.
It is similar to the [backend CRUD generator](/documentation/magic/components/crudifier/backend/), but instead of
automatically creating your SQL, it allows you to provide your own custom SQL, and then securely wrap your SQL into
an HTTP endpoint. Below is a screenshot of the component.

![SQL web API](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The process works as follows.

1. Choose your database
2. Choose an HTTP verb and a URL for your endpoint
3. Select which roles should be allowed to invoke your endpoint (optional)
4. Provide arguments to your endpoint (optional)
5. Write your SQL referencing arguments if you provided arguments in the above step

When you've done with the above, simply click the _"Generate"_ button, and you've got an HTTP endpoint
wrapping your SQL. Read [this article](/tutorials/sql-web-api/) for a hands on tutorial about the component.

## Settings

The SQL generator allows you to override authorisation requirements, the URL of your endpoint, and which arguments
your endpoint requires. The last parts is important since it allows you to add arguments to your endpoint that
you can reference in your SQL somehow. In the above screenshot we have created a _"filter"_ argument, that we're
referencing inside our SQL using `@filter`. Above we're using this argument to make sure we're only returning
items having either a _"first\_name"_, _"title"_, or _"description"_ that contains the specified filter value - But you
can also reference arguments for insert, update, or delete SQL statements. If you generate an SQL endpoint using the
PUT, PATCH or POST verb, the caller will have to supply his or her arguments as a JSON payload. If you generate a GET or
DELETE endpoint, the endpoint requires your arguments as query parameters instead. When you add arguments to your
endpoint's declaration, you'll have to choose a _"type"_. This ensures that Magic is automagically converting
the incoming argument's value to the type of your choice. Below is a screenshot of this process.

![SQL arguments](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-arguments.jpg)

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
