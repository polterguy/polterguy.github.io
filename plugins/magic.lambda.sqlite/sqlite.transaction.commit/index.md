---
title: "How to use [sqlite.transaction.commit]"
description: "How to use [sqlite.transaction.commit] - This slot commits the open transaction."
generated: true
guide: true
---

The reference page of [`sqlite.transaction.commit`](/reference/slots/sqlite/sqlite.transaction.commit/) has its arguments, constraints and declaration.

This slot commits the open transaction. It works like **[data.transaction.commit]**. Without it a transaction is rolled back when it leaves scope. Below is an example.

```
sqlite.connect:sakila
   sqlite.transaction.create
      sqlite.execute:update actor set last_name = 'Smith' where actor_id = 1
      sqlite.transaction.commit
```
