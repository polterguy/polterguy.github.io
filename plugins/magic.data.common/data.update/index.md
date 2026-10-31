---
title: "How to use [data.update]"
description: "How to use [data.update] - This slot updates rows in your database, using the current open connection created by [data.connect]."
generated: true
guide: true
---

The reference page of [`data.update`](/reference/slots/data/data.update/) has its arguments, constraints and declaration.

This slot updates rows in your database, using the current open connection created by **[data.connect]**.
It takes the same arguments as **[sql.update]**, and its value resolves to the number of rows affected.
Always supply a **[where]** argument to constrain which rows are updated, since the SQL generated does not
constrain the update to any specific row if you leave it out.

* __[table]__ - Name of the table to update. Mandatory, the slot throws if it is missing
* __[values]__ - Column names and their new values, as children nodes. Mandatory, the slot throws if it is missing
* __[where]__ - Condition constraining which rows to update, see the **[where]** documentation below
* __[database-type]__ - Database adapter to use instead of your default database type
* __[generate]__ - If true, only generates the SQL and its parameters instead of executing it, default is false
