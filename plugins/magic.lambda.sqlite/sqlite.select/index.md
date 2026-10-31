---
title: "How to use [sqlite.select]"
description: "How to use [sqlite.select] - This slot executes any SQL you give it against the open connection, and returns every record as a lambda object."
generated: true
guide: true
---

The reference page of [`sqlite.select`](/reference/slots/sqlite/sqlite.select/) has its arguments, constraints and declaration.

This slot executes any SQL you give it against the open connection, and returns every record as a lambda object. It works like **[data.select]**, except it always uses SQLite. Below is an example.

```
sqlite.connect:sakila
   sqlite.select:select first_name, last_name from actor limit 2

// The result of the above looks like the following.
sqlite.connect
   sqlite.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
```
