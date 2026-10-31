---
title: "How to use [mssql.delete]"
description: "How to use [mssql.delete] - This slot deletes records from a table, generating the SQL for Microsoft SQL Server, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`mssql.delete`](/reference/slots/mssql/mssql.delete/) has its arguments, constraints and declaration.

This slot deletes records from a table, generating the SQL for Microsoft SQL Server, and resolves to the number of records affected. It works like **[data.delete]**. Always supply **[where]**. Below is an example.

```
mssql.connect:sakila
   mssql.delete
      table:actor
      where
         and
            first_name:John
            last_name:Doe
```
