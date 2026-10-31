---
title: "How to use [pgsql.read]"
description: "How to use [pgsql.read] - This slot reads records from a table, generating the SQL for PostgreSQL, and returns them as a lambda object."
generated: true
guide: true
---

The reference page of [`pgsql.read`](/reference/slots/pgsql/pgsql.read/) has its arguments, constraints and declaration.

This slot reads records from a table, generating the SQL for PostgreSQL, and returns them as a lambda object. It works like **[data.read]**, and limits the result to 25 records unless you supply **[limit]**. Below is an example.

```
pgsql.connect:sakila
   pgsql.read
      table:actor
      columns
         first_name
         last_name
      order:last_name
      limit:5
```
