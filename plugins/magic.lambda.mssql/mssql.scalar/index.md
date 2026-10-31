---
title: "How to use [mssql.scalar]"
description: "How to use [mssql.scalar] - This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result."
generated: true
guide: true
---

The reference page of [`mssql.scalar`](/reference/slots/mssql/mssql.scalar/) has its arguments, constraints and declaration.

This slot executes SQL returning a single value, such as an aggregate, and sets the value of its own node to the result. It works like **[data.scalar]**, except it always uses Microsoft SQL Server. Below is an example, counting the records of a table.

```
mssql.connect:sakila
   mssql.scalar:select count(*) from actor
```
