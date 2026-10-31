---
title: "How to use [mssql.select]"
description: "How to use [mssql.select] - This slot executes any SQL you give it against the open connection, and returns every record as a lambda object."
generated: true
guide: true
---

The reference page of [`mssql.select`](/reference/slots/mssql/mssql.select/) has its arguments, constraints and declaration.

This slot executes any SQL you give it against the open connection, and returns every record as a lambda object. It works like **[data.select]**, except it always uses Microsoft SQL Server. Below is an example.

```
mssql.connect:sakila
   mssql.select:select first_name, last_name from actor limit 2

// The result of the above looks like the following.
mssql.connect
   mssql.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
```
