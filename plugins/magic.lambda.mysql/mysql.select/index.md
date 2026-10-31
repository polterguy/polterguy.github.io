---
title: "How to use [mysql.select]"
description: "How to use [mysql.select] - This slot executes any SQL you give it against the open connection, and returns every record as a lambda object."
generated: true
guide: true
---

The reference page of [`mysql.select`](/reference/slots/mysql/mysql.select/) has its arguments, constraints and declaration.

This slot executes any SQL you give it against the open connection, and returns every record as a lambda object. It works like **[data.select]**, except it always uses MySQL. Below is an example.

```
mysql.connect:sakila
   mysql.select:select first_name, last_name from actor limit 2

// The result of the above looks like the following.
mysql.connect
   mysql.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
```
