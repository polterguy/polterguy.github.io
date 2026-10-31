---
title: "How to use [sql.delete]"
description: "How to use [sql.delete] - This slot is for deleting records."
generated: true
guide: true
---

This is the guide to [`sql.delete`](/reference/slots/sql/sql.delete/), whose reference page has its arguments, constraints and declaration.

This slot is for deleting records. Its **[where]** argument is applied in a similar fashion as the where
argument to **[sql.read]** and **[sql.update]**. You can find an example further down in this document of
how to use **[where]**.

```
sql.delete
   table:table1
   where
      and
         field1:value1
         field2:value2
```

The above will produce the following results.

```
sql.delete:delete from 'table1' where 'field1' = @0 and 'field2' = @1
   @0:value1
   @1:value2
```
