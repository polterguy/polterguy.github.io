---
title: "How to use [sqlite.read]"
description: "How to use [sqlite.read] - This slot reads records from a table, generating the SQL for SQLite, and returns them as a lambda object."
generated: true
guide: true
---

The reference page of [`sqlite.read`](/reference/slots/sqlite/sqlite.read/) has its arguments, constraints and declaration.

This slot reads records from a table, generating the SQL for SQLite, and returns them as a lambda object. It works like **[data.read]**, and limits the result to 25 records unless you supply **[limit]**. Below is an example.

```
sqlite.connect:sakila
   sqlite.read
      table:actor
      columns
         first_name
         last_name
      order:last_name
      limit:5
```
