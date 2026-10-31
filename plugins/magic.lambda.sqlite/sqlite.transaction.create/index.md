---
title: "How to use [sqlite.transaction.create]"
description: "How to use [sqlite.transaction.create] - This slot creates a database transaction, and evaluates its lambda object inside of it."
generated: true
guide: true
---

The reference page of [`sqlite.transaction.create`](/reference/slots/sqlite/sqlite.transaction.create/) has its arguments, constraints and declaration.

This slot creates a database transaction, and evaluates its lambda object inside of it. It works like **[data.transaction.create]**. Unless the transaction is explicitly committed before it leaves scope, it is rolled back, which is what happens below.

```
sqlite.connect:sakila
   sqlite.transaction.create
      sqlite.execute:update actor set last_name = 'Smith' where actor_id = 1
```
