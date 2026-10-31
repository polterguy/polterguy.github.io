---
title: "How to use [pgsql.transaction.commit]"
description: "How to use [pgsql.transaction.commit] - This slot commits the open transaction."
generated: true
guide: true
---

The reference page of [`pgsql.transaction.commit`](/reference/slots/pgsql/pgsql.transaction.commit/) has its arguments, constraints and declaration.

This slot commits the open transaction. It works like **[data.transaction.commit]**. Without it a transaction is rolled back when it leaves scope. Below is an example.

```
pgsql.connect:sakila
   pgsql.transaction.create
      pgsql.execute:update actor set last_name = 'Smith' where actor_id = 1
      pgsql.transaction.commit
```
