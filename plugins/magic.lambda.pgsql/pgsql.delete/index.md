---
title: "How to use [pgsql.delete]"
description: "How to use [pgsql.delete] - This slot deletes records from a table, generating the SQL for PostgreSQL, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`pgsql.delete`](/reference/slots/pgsql/pgsql.delete/) has its arguments, constraints and declaration.

This slot deletes records from a table, generating the SQL for PostgreSQL, and resolves to the number of records affected. It works like **[data.delete]**. Always supply **[where]**. Below is an example.

```
pgsql.connect:sakila
   pgsql.delete
      table:actor
      where
         and
            first_name:John
            last_name:Doe
```
