---
title: "Aggregate results"
description: "Aggregate results - You can also create aggregate results, by simply adding your aggregate as your column, such as the following illustrates."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

You can also create aggregate results, by simply adding your aggregate as your column, such as the
following illustrates.

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
select count(*) as 'count' from 'table1'
```

A column, **[group]** or **[order]** entry containing a parenthesis is parsed as an expression, and every
identifier in it is escaped. An expression can call the functions every database has, being `count`, `sum`,
`avg`, `min`, `max`, `group_concat`, `string_agg`, `round`, `abs`, `coalesce`, `lower`, `upper`, `length` and
`cast`, plus the functions of the database's own dialect.

* SQLite - `total`, `strftime`, `date`, `datetime`, `julianday`, `ifnull`, `random`, `substr` and `trim`
* MySQL - `date_format`, `year`, `month`, `day`, `ifnull`, `rand`, `concat`, `substring` and `trim`
* PostgreSQL - `to_char`, `date_trunc`, `random`, `concat`, `substring` and `trim`
* SQL Server - `year`, `month`, `day`, `format`, `isnull`, `newid`, `concat`, `substring` and `trim`

Functions can be nested, and combined with `+`, `-`, `*` and `/`, numbers, and string literals in single quotes
holding letters, digits, spaces and the characters `%-_:/.,`. A column can declare its alias inline, as in
`count(*) as total`, instead of with an **[as]** argument. The following groups SQLite rows by month.

```
sql.read
   table:sales
   limit:-1
   columns
      strftime('%Y-%m', sold)
         as:month
      round(sum(amount), 2) as total
   group
      strftime('%Y-%m', sold)
   order:"strftime('%Y-%m', sold)"
```

Anything else, such as sub-selects, `case` expressions, functions not listed above, or a string literal holding
a quote, is rejected with an exception, to avoid SQL injection attacks. Use **[data.select]** with plain SQL for
those.

By setting **[limit]** to _"-1"_, like we do above, we avoid adding the limit parts to our SQL. Unless
you explicitly specify a limit, the default value will always be 25 to avoid accidentally exhausting your database,
and/or web server, by selecting all records from a table with millions of records.

---

[&larr; How to use [data.*]](/plugins/magic.data.common/how-to-use-data/) | [all of magic.data.common](/plugins/magic.data.common/) | [Paging &rarr;](/plugins/magic.data.common/paging/)
