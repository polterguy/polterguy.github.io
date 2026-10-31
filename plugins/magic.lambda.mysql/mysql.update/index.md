---
title: "How to use [mysql.update]"
description: "How to use [mysql.update] - This slot updates records in a table, generating the SQL for MySQL, and resolves to the number of records affected."
generated: true
guide: true
---

The reference page of [`mysql.update`](/reference/slots/mysql/mysql.update/) has its arguments, constraints and declaration.

This slot updates records in a table, generating the SQL for MySQL, and resolves to the number of records affected. It works like **[data.update]**. Always supply **[where]**, or every record in the table is updated. Below is an example.

```
mysql.connect:sakila
   mysql.update
      table:actor
      values
         last_name:Smith
      where
         and
            first_name:John
            last_name:Doe
```
