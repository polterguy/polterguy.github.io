---
title: "How to use [sqlite.update]"
description: "How to use [sqlite.update] - This slot updates records in a table, generating the SQL for SQLite, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`sqlite.update`](/reference/slots/sqlite/sqlite.update/) has its arguments, constraints and declaration.

This slot updates records in a table, generating the SQL for SQLite, and resolves to the number of records affected. It works like **[data.update]**. Always supply **[where]**, or every record in the table is updated. Below is an example.

```
sqlite.connect:sakila
   sqlite.update
      table:actor
      values
         last_name:Smith
      where
         and
            first_name:John
            last_name:Doe
```
