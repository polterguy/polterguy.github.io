---
title: "How to use [mysql.read]"
description: "How to use [mysql.read] - This slot reads records from a table, generating the SQL for MySQL, and returns them as a lambda object."
generated: true
guide: true
---

The reference page of [`mysql.read`](/reference/slots/mysql/mysql.read/) has its arguments, constraints and declaration.

This slot reads records from a table, generating the SQL for MySQL, and returns them as a lambda object. It works like **[data.read]**, and limits the result to 25 records unless you supply **[limit]**. Below is an example.

```
mysql.connect:sakila
   mysql.read
      table:actor
      columns
         first_name
         last_name
      order:last_name
      limit:5
```
