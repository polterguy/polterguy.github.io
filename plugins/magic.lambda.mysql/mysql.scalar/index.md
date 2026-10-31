---
title: "How to use [mysql.scalar]"
description: "How to use [mysql.scalar] - This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result."
generated: true
guide: true
---

The reference page of [`mysql.scalar`](/reference/slots/mysql/mysql.scalar/) has its arguments, constraints and declaration.

This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result. It works like **[data.scalar]**, except it always uses MySQL. Below is an example, counting the records of a table.

```
mysql.connect:sakila
   mysql.scalar:select count(*) from actor
```
