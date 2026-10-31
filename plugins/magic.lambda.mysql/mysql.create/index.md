---
title: "How to use [mysql.create]"
description: "How to use [mysql.create] - This slot inserts a record into a table, generating the SQL for MySQL."
generated: true
guide: true
---

The reference page of [`mysql.create`](/reference/slots/mysql/mysql.create/) has its arguments, constraints and declaration.

This slot inserts a record into a table, generating the SQL for MySQL. It works like **[data.create]**, and its value becomes the ID of the new record unless **[return-id]** is false. Below is an example.

```
mysql.connect:sakila
   mysql.create
      table:actor
      values
         first_name:John
         last_name:Doe
```
