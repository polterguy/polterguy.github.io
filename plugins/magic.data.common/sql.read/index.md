---
title: "How to use [sql.read]"
description: "How to use [sql.read] - This slot requires only one mandatory argument, being your table name."
generated: true
guide: true
---

This is the guide to [`sql.read`](/reference/slots/sql/sql.read/), whose reference page has its arguments, constraints and declaration.

This slot requires only one mandatory argument, being your table name. The slot creates a select
SQL statement for you. An example can be found below.

```
sql.read
   table:foo
```

The above will result in the following SQL returned to you. If you're using the special implementations,
such as e.g. **[data.read]**, and/or **[mssql.read]** - The returned SQL might vary according to your dialect.
But the results of executing the SQL will be the same.

```
select * from 'foo' limit 25
```

To avoid accidentally exhausting your database, this slot will by default limit your result set
to 25 records unless explicitly overridden by your code with a **[limit]** argument. You can optionally
supply the following arguments to this slot.

* __[columns]__ - Columns to select
* __[order]__ - Which column(s) to order the results by. You can supply multiple **[order]** arguments
* __[direction]__ - Which direction to order your columns
* __[limit]__ - How many records to return, default is 25. Set this value to -1 to avoid having the parser inject its default value
* __[offset]__ - Offset of where to start returning records
* __[where]__ - Where condition
* __[join]__ - Join condition
* __[group]__ - Group by declaration

For instance, to select only the _"field1"_ column and the _"field2"_ column from _"table1"_,
and ordering descendingly by _"field3"_ - You can use something resembling the following.

```
sql.read
   table:table1
   columns
      field1
      field2
   order:field3
   direction:desc
```

This will result in the following SQL returned.

```
select 'field1','field2' from 'table1' order by 'field3' desc limit 25
```

The **[direction]** argument can _only_ be either _"asc"_ or _"desc"_, implying ascending or descending.
You can also supply multiple ordering columns, by separating them by _","_. See an example below, which also specifies
what table to use while ordering your results.

```
sql.read
   table:table1
   order:table1.field1, table1.field2
```

The above will result in the following SQL.

```sql
select * from 'table1' order by 'table1'.'field1' asc,'table1'.'field2' asc limit 25
```

And finally you can provide the **[direction]** argument on separate **[order]** arguments, such as the
following illustrates.

```
sql.read
   table:table1

   order:field1
      direction:asc

   order:field2
      direction:desc
```

If you do, the ordering is sequentially applied.
