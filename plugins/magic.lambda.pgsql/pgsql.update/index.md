---
title: "How to use [pgsql.update]"
description: "How to use [pgsql.update] - This slot updates records in a table, generating the SQL for PostgreSQL, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`pgsql.update`](/reference/slots/pgsql/pgsql.update/) has its arguments, constraints and declaration.

This slot updates records in a table, generating the SQL for PostgreSQL, and resolves to the number of records affected. It works like **[data.update]**. Always supply **[where]**, or every record in the table is updated. Below is an example.

```
pgsql.connect:sakila
   pgsql.update
      table:actor
      values
         last_name:Smith
      where
         and
            first_name:John
            last_name:Doe
```
