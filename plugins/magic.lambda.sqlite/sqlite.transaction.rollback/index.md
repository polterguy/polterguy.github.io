---
title: "How to use [sqlite.transaction.rollback]"
description: "How to use [sqlite.transaction.rollback] - This slot explicitly rolls back the open transaction, discarding everything done since it was created."
generated: true
guide: true
---

The reference page of [`sqlite.transaction.rollback`](/reference/slots/sqlite/sqlite.transaction.rollback/) has its arguments, constraints and declaration.

This slot explicitly rolls back the open transaction, discarding everything done since it was created. It works like **[data.transaction.rollback]**. Below is an example.

```
sqlite.connect:sakila
   sqlite.transaction.create
      sqlite.execute:update actor set last_name = 'Smith' where actor_id = 1
      sqlite.transaction.rollback
```
