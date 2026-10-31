---
title: "'Namespacing' columns"
description: "'Namespacing' columns - When you're joining results from multiple tables, it's often required that you specify which table you want some resulting column to be fetched from, to avoid confusing your database as to whic..."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

## 'Namespacing' columns

When you're joining results from multiple tables, it's often required that you specify which table you want some resulting
column to be fetched from, to avoid confusing your database as to which column you want to extract, in cases where the
same column exists in multiple tables. For such cases, you can simply refer to your table first, and then the column
from that table, and separate your entities by a `.`. You can see an example of this below.

```
data.connect:sakila
   data.read
      columns

         /*
          * Prefixing result columns with table names.
          */
         film.title
         film.description
         actor.last_name
         actor.first_name

      table:film

         join:film_actor
            type:inner
            on
               and
                  film.film_id:film_actor.film_id

            join:actor
               type:inner
               on
                  and
                     film_actor.actor_id:actor.actor_id
```

The above will result in the following SQL, if you append the **[generate]** argument, and set its value to _"true"_.

```sql
select
   `film`.`title`,
   `film`.`description`,
   `actor`.`last_name`,
   `actor`.`first_name`
   from `film`
      inner join `film_actor` on `film`.`film_id` = `film_actor`.`film_id`
         inner join `actor` on `film_actor`.`actor_id` = `actor`.`actor_id`
   limit 25
```

Spacing is not applied to the actual generated SQL result, but have been applied to some of the SQL
examples in this documentation to make the SQL more readable.
If you supply **[as]** arguments to your tables, you can also use your alias to reference tables inside of
your invocation.


## Group by

You can also provide a **[group]** argument to your lambda, resulting in a _"group by"_ statement injected
into the resulting SQL. Below is an example.

```
sql.read
   table:table1
   limit:-1
   columns
      col1
      count(*)
         as:count
   group
      col1
```

The above will result in the following SQL.

```
select col1, count(*) as count from 'table1' group by 'col1'
```

You can supply multiple group by columns, in addition to _"namespacing"_ your columns with your table names,
such as we illustrate below.

```
sql.read
   table:table1
   limit:-1
   columns
      count(*)
   group
      table1.foo1
      table1.foo2
```

The above of course results in the following SQL.

```sql
select count(*) from 'table1' group by 'table1'.'foo1','table1'.'foo2'
```

You can of course combine your **[group]** arguments with **[where]** arguments, and **[\[join\]](/reference/slots/core/join/)** arguments,
allowing you to create complex aggregate results, statistics, joining multiple tables, etc.

---

[&larr; Differences between [join] and [where]](/plugins/magic.data.common/differences-between-join-and-where/) | [all of magic.data.common](/plugins/magic.data.common/) | [The [where] argument &rarr;](/plugins/magic.data.common/the-where-argument/)
