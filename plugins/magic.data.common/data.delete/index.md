---
title: "How to use [data.delete]"
description: "How to use [data.delete] - This slot deletes rows in your database, using the current open connection created by [data.connect]."
generated: true
guide: true
---

The reference page of [`data.delete`](/reference/slots/data/data.delete/) has its arguments, constraints and declaration.

This slot deletes rows in your database, using the current open connection created by **[data.connect]**. It takes the same arguments as **[sql.delete]**, and its value resolves to the number of rows affected. The **[where]** argument is mandatory, to make it impossible to delete every row in a table by accident.

* __[table]__ - Name of the table to delete from. Mandatory, the slot throws if it is missing
* __[where]__ - Condition constraining which rows to delete, see the **[where]** documentation below
* __[database-type]__ - Database adapter to use instead of your default database type
* __[generate]__ - If true, only generates the SQL and its parameters instead of executing it, default is false

Below is an example.

```
data.connect:sakila
   data.delete
      table:actor
      where
         and
            first_name:John
            last_name:Doe
```
