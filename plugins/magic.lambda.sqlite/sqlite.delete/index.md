---
title: "How to use [sqlite.delete]"
description: "How to use [sqlite.delete] - This slot deletes records from a table, generating the SQL for SQLite, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`sqlite.delete`](/reference/slots/sqlite/sqlite.delete/) has its arguments, constraints and declaration.

This slot deletes records from a table, generating the SQL for SQLite, and resolves to the number of records affected. It works like **[data.delete]**. Always supply **[where]**. Below is an example.

```
sqlite.connect:sakila
   sqlite.delete
      table:actor
      where
         and
            first_name:John
            last_name:Doe
```
