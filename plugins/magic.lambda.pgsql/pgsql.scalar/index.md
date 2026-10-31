---
title: "How to use [pgsql.scalar]"
description: "How to use [pgsql.scalar] - This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result."
generated: true
guide: true
---

The reference page of [`pgsql.scalar`](/reference/slots/pgsql/pgsql.scalar/) has its arguments, constraints and declaration.

This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result. It works like **[data.scalar]**, except it always uses PostgreSQL. Below is an example, counting the records of a table.

```
pgsql.connect:sakila
   pgsql.scalar:select count(*) from actor
```
