---
title: "How to use [pgsql.transaction.rollback]"
description: "How to use [pgsql.transaction.rollback] - This slot explicitly rolls back the open transaction, discarding everything done since it was created."
generated: true
guide: true
---

The reference page of [`pgsql.transaction.rollback`](/reference/slots/pgsql/pgsql.transaction.rollback/) has its arguments, constraints and declaration.

This slot explicitly rolls back the open transaction, discarding everything done since it was created. It works like **[data.transaction.rollback]**. Below is an example.

```
pgsql.connect:sakila
   pgsql.transaction.create
      pgsql.execute:update actor set last_name = 'Smith' where actor_id = 1
      pgsql.transaction.rollback
```
