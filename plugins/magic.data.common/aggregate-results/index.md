---
title: "Aggregate results"
description: "Aggregate results - You can also create aggregate results, by simply adding your aggregate as your column, such as the following illustrates."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

## Aggregate results

You can also create aggregate results, by simply adding your aggregate as your column, such as the
following illustrates. The reasons why this works, is because if the SQL generator finds a parenthesis in your
column declaration, it will simply ignore parsing that column altogether, and directly inject it into the
resulting SQL's columns declaration.

```
sql.read
   table:table1
   limit:-1
   columns
      count(*)
        as:count
```

The above will result in the following SQL.

```
select count(*) as count from 'table1'
```

By setting **[limit]** to _"-1"_, like we do above, we avoid adding the limit parts to our SQL. Unless
you explicitly specify a limit, the default value will always be 25 to avoid accidentally exhausting your database,
and/or web server, by selecting all records from a table with millions of records.


## Paging

To page your **[sql.read]** results, use **[limit]** and **[offset]**, such as the following illustrates.
Even though we use _"limit"_ and _"offset"_, the correct syntax will be applied for your database type,
depending upon which database type you're using - Implying for Microsoft SQL Server, it will inject MS SQL dialect,
and not MySQL dialect. But the syntax for your lambda object still remains the same, making it simpler to create
SQL dialect valid for your specific database type 100% transparently.

```
sql.read
   table:table1
   offset:5
   limit:10
```

The above will return the following SQL `select * from 'table1' limit 10 offset 5`. If you run the above lambda
towards Microsoft SQL server, SQL syntax specific for MS SQL will be generated.


## Aliasing column results

You can also extract columns with an alias, _"renaming"_ the column in its result, such as the following illustrates.

```
sql.read
   table:table1
   columns

      table1.foo1
         as:howdy

      table1.foo2
         as:world
```

The above Hyperlambda will result in the following SQL.

```sql
select 'table1'.'foo1' as 'howdy','table1'.'foo2' as 'world'
   from 'table1' limit 25
```

Effectively resulting in that you'll have two columns returned after executing the above SQL, which
are `howdy` and `world`. Combining this with the join features from this project, allows you to create
any type of _"projections"_ you wish.

---

[&larr; How to use [data.*]](/plugins/magic.data.common/how-to-use-data/) | [all of magic.data.common](/plugins/magic.data.common/) | [Joins &rarr;](/plugins/magic.data.common/joins/)
