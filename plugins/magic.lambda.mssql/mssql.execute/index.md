---
title: "How to use [mssql.execute]"
description: "How to use [mssql.execute] - This slot executes SQL you do not expect any result from, such as updates and deletes."
generated: true
guide: true
---

The reference page of [`mssql.execute`](/reference/slots/mssql/mssql.execute/) has its arguments, constraints and declaration.

This slot executes SQL you do not expect any result from, such as updates and deletes. It works like **[data.execute]**, except it always uses Microsoft SQL Server. Below is an example.

```
mssql.connect:sakila
   mssql.execute:update actor set last_name = 'Smith' where actor_id = 1
```
