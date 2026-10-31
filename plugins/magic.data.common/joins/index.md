---
title: "Joins"
description: "Joins - The project supports joins by parametrizing your [sql.read] invocation with [join] arguments, beneath your If you have created the Sakila example database from Oracle, and you're using MySQL as your d"
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

The project supports joins by parametrizing your **[sql.read]** invocation with **[join]** arguments, beneath your
**[table]** argument(s). You can _only_ add **[join]** beneath **[table]** for **[sql.read]** invocations though.
If you have created the Sakila example database from Oracle, and you're using MySQL as your default database type,
you can execute the following MySQL join SQL statement to see a fairly complex recursive join.

```
data.connect:sakila
   data.read

      columns
         title
         description
         last_name
         first_name

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

The above lambda assumes you've got Oracle's Sakila database in your MySQL instance. If you only wish to see
its resulting SQL, add a **[generate]** argument to the above root invocation, and set its value to _"true"_.
All specialised slots, dynamically building and executing some SQL towards your database, supports
the **[generate]** argument, allowing you to easily _"debug"_ your SQL statements, and see what they actually do.
Below is an example of the SQL created by the above invocation if you add a **[generate]** argument to it
and set its value to boolean `true`.

```sql
select `film`.`title`, `film`.`description`, `actor`.`last_name`, `actor`.`first_name` from `film`
   inner join `film_actor` on `film`.`film_id` = `film_actor`.`film_id`
      inner join `actor` on `film_actor`.`actor_id` = `actor`.`actor_id`
   limit 25
```

You can recursively join as many levels as you wish, in addition to also supplying multiple join conditions for
the same join. An example of the latter can be found below.

```
sql.read
   generate:true
   limit:-1
   table:table1

      join:table2
         on
            and
               fk1:pk1
               fk2:pk2
```

The above lambda will result in the following SQL being generated.

```sql
select * from 'table1'
   inner join 'table2' on 'table1'.'fk1' = 'table2'.'pk1' and
      'table1'.'fk2' = 'table2'.'pk2'
```

Joining tables works _almost_ the exact same way as using a **[where]** argument, allowing you
to supply an operator for your join, such as we illustrate below, where we're using the `!=` operator,
instead of the (default) equality comparison. However, when you create your **[join]** segments
you can _only_ have columns from tables reference columns from tables, and not add static arguments
to your join. If you need static arguments you have to add these into your **[where]** parts.
See the **[where]** criteria for details about comparison operators.
You can also explicitly choose a **[type]** of join, such as we illustrate below.

```
sql.read
   limit:-1
   table:table1

      join:table2
         type:inner
         on
            and
               fk1.neq:pk1
```

The above results in the following SQL.

```sql
select * from 'table1' inner join 'table2' on 'table1'.'fk1' != 'table2'.'pk1'
```

The **[type]** argument to your **[join]** arguments, can be _"inner"_, _"full"_, _"left"_ or _"right"_,
resulting in the equivalent type of join for your SQL.

---

[&larr; Aggregate results](/plugins/magic.data.common/aggregate-results/) | [all of magic.data.common](/plugins/magic.data.common/) | [Differences between [join] and [where] &rarr;](/plugins/magic.data.common/differences-between-join-and-where/)
