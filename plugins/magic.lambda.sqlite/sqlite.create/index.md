---
title: "How to use [sqlite.create]"
description: "How to use [sqlite.create] - This slot inserts a record into a table, generating the SQL for SQLite."
generated: true
guide: true
---

The reference page of [`sqlite.create`](/reference/slots/sqlite/sqlite.create/) has its arguments, constraints and declaration.

This slot inserts a record into a table, generating the SQL for SQLite. It works like **[data.create]**, and its value becomes the ID of the new record unless **[return-id]** is false. Below is an example.

```
sqlite.connect:sakila
   sqlite.create
      table:actor
      values
         first_name:John
         last_name:Doe
```
