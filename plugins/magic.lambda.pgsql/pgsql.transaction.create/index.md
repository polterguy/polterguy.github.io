---
title: "How to use [pgsql.transaction.create]"
description: "How to use [pgsql.transaction.create] - This slot creates a database transaction, and evaluates its lambda object inside of it."
generated: true
guide: true
---

The reference page of [`pgsql.transaction.create`](/reference/slots/pgsql/pgsql.transaction.create/) has its arguments, constraints and declaration.

This slot creates a database transaction, and evaluates its lambda object inside of it. It works like **[data.transaction.create]**. Unless the transaction is explicitly committed before it leaves scope, it is rolled back, which is what happens below.

```
pgsql.connect:sakila
   pgsql.transaction.create
      pgsql.execute:update actor set last_name = 'Smith' where actor_id = 1
```
