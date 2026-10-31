---
title: "How to use [mssql.update]"
description: "How to use [mssql.update] - This slot updates records in a table, generating the SQL for Microsoft SQL Server, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`mssql.update`](/reference/slots/mssql/mssql.update/) has its arguments, constraints and declaration.

This slot updates records in a table, generating the SQL for Microsoft SQL Server, and resolves to the number of records affected. It works like **[data.update]**. Always supply **[where]**, or every record in the table is updated. Below is an example.

```
mssql.connect:sakila
   mssql.update
      table:actor
      values
         last_name:Smith
      where
         and
            first_name:John
            last_name:Doe
```
