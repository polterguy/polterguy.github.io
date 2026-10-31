---
title: "How to use [sqlite.scalar]"
description: "How to use [sqlite.scalar] - This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result."
generated: true
guide: true
---

The reference page of [`sqlite.scalar`](/reference/slots/sqlite/sqlite.scalar/) has its arguments, constraints and declaration.

This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result. It works like **[data.scalar]**, except it always uses SQLite. Below is an example, counting the records of a table.

```
sqlite.connect:sakila
   sqlite.scalar:select count(*) from actor
```
