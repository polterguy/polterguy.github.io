---
title: "How to use [data.create]"
description: "How to use [data.create] - This slot inserts a new row into your database, using the current open connection created by [data.connect]."
generated: true
guide: true
---

This is the guide to [`data.create`](/reference/slots/data/data.create/), whose reference page has its arguments, constraints and declaration.

This slot inserts a new row into your database, using the current open connection created by **[data.connect]**.
It generates the SQL for your database type, and takes the same **[table]** and **[values]** arguments as
**[sql.create]**. Its value resolves to the ID of the created row if **[return-id]** is true, which is the default,
otherwise to null. It also accepts the following arguments.

* __[table]__ - Name of the table to insert into. Mandatory, the slot throws if it is missing
* __[values]__ - Column names and values to insert, as children nodes. Mandatory, the slot throws if it is missing
* __[database-type]__ - Database adapter to use instead of your default database type
* __[generate]__ - If true, only generates the SQL and its parameters instead of executing it, default is false
* __[return-id]__ - Whether or not to return the ID of the created row, default is true
