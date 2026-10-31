---
title: "How to use [odbc.scalar]"
description: "How to use [odbc.scalar] - This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result."
generated: true
guide: true
---

The reference page of [`odbc.scalar`](/reference/slots/odbc/odbc.scalar/) has its arguments, constraints and declaration.

This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result. It works like **[data.scalar]**, except it always uses ODBC. Below is an example, counting the records of a table.

```
odbc.connect:sakila
   odbc.scalar:select count(*) from actor
```
