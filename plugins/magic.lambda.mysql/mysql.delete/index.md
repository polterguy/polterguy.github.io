---
title: "How to use [mysql.delete]"
description: "How to use [mysql.delete] - This slot deletes records from a table, generating the SQL for MySQL, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`mysql.delete`](/reference/slots/mysql/mysql.delete/) has its arguments, constraints and declaration.

This slot deletes records from a table, generating the SQL for MySQL, and resolves to the number of records affected. It works like **[data.delete]**. Always supply **[where]**. Below is an example.

```
mysql.connect:sakila
   mysql.delete
      table:actor
      where
         and
            first_name:John
            last_name:Doe
```
