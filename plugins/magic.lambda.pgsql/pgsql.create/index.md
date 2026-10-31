---
title: "How to use [pgsql.create]"
description: "How to use [pgsql.create] - This slot inserts a record into a table, generating the SQL for PostgreSQL."
generated: true
guide: true
---

The reference page of [`pgsql.create`](/reference/slots/pgsql/pgsql.create/) has its arguments, constraints and declaration.

This slot inserts a record into a table, generating the SQL for PostgreSQL. It works like **[data.create]**, and its value becomes the ID of the new record unless **[return-id]** is false. Below is an example.

```
pgsql.connect:sakila
   pgsql.create
      table:actor
      values
         first_name:John
         last_name:Doe
```
