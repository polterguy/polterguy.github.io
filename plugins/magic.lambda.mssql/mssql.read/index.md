---
title: "How to use [mssql.read]"
description: "How to use [mssql.read] - This slot reads records from a table, generating the SQL for Microsoft SQL Server, and returns them as a lambda object."
generated: true
guide: true
---

The reference page of [`mssql.read`](/reference/slots/mssql/mssql.read/) has its arguments, constraints and declaration.

This slot reads records from a table, generating the SQL for Microsoft SQL Server, and returns them as a lambda object. It works like **[data.read]**, and limits the result to 25 records unless you supply **[limit]**. Below is an example.

```
mssql.connect:sakila
   mssql.read
      table:actor
      columns
         first_name
         last_name
      order:last_name
      limit:5
```
