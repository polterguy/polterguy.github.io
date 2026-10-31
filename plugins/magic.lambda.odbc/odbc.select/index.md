---
title: "How to use [odbc.select]"
description: "How to use [odbc.select] - This slot executes any SQL you give it against the open connection, and returns every record as a lambda object."
generated: true
guide: true
---

The reference page of [`odbc.select`](/reference/slots/odbc/odbc.select/) has its arguments, constraints and declaration.

This slot executes any SQL you give it against the open connection, and returns every record as a lambda object. It works like **[data.select]**, except it always uses ODBC. Below is an example.

```
odbc.connect:sakila
   odbc.select:select first_name, last_name from actor limit 2

// The result of the above looks like the following.
odbc.connect
   odbc.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
```
