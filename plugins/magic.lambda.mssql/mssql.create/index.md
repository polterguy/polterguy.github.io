---
title: "How to use [mssql.create]"
description: "How to use [mssql.create] - This slot inserts a record into a table, generating the SQL for Microsoft SQL Server."
generated: true
guide: true
---

The reference page of [`mssql.create`](/reference/slots/mssql/mssql.create/) has its arguments, constraints and declaration.

This slot inserts a record into a table, generating the SQL for Microsoft SQL Server. It works like **[data.create]**, and its value becomes the ID of the new record unless **[return-id]** is false. Below is an example.

```
mssql.connect:sakila
   mssql.create
      table:actor
      values
         first_name:John
         last_name:Doe
```
