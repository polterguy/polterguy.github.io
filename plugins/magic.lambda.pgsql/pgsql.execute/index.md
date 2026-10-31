---
title: "How to use [pgsql.execute]"
description: "How to use [pgsql.execute] - This slot executes SQL you do not expect any result from, such as updates and deletes."
generated: true
guide: true
---

The reference page of [`pgsql.execute`](/reference/slots/pgsql/pgsql.execute/) has its arguments, constraints and declaration.

This slot executes SQL you do not expect any result from, such as updates and deletes. It works like **[data.execute]**, except it always uses PostgreSQL. Below is an example.

```
pgsql.connect:sakila
   pgsql.execute:update actor set last_name = 'Smith' where actor_id = 1
```
