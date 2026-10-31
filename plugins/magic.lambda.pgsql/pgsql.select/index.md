---
title: "How to use [pgsql.select]"
description: "How to use [pgsql.select] - This slot executes any SQL you give it against the open connection, and returns every record as a lambda object."
generated: true
guide: true
---

The reference page of [`pgsql.select`](/reference/slots/pgsql/pgsql.select/) has its arguments, constraints and declaration.

This slot executes any SQL you give it against the open connection, and returns every record as a lambda object. It works like **[data.select]**, except it always uses PostgreSQL. Below is an example.

```
pgsql.connect:sakila
   pgsql.select:select first_name, last_name from actor limit 2

// The result of the above looks like the following.
pgsql.connect
   pgsql.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
```
