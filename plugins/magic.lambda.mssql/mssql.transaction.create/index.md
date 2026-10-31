---
title: "How to use [mssql.transaction.create]"
description: "How to use [mssql.transaction.create] - This slot creates a database transaction, and evaluates its lambda object inside of it."
generated: true
guide: true
---

The reference page of [`mssql.transaction.create`](/reference/slots/mssql/mssql.transaction.create/) has its arguments, constraints and declaration.

This slot creates a database transaction, and evaluates its lambda object inside of it. It works like **[data.transaction.create]**. Unless the transaction is explicitly committed before it leaves scope, it is rolled back, which is what happens below.

```
mssql.connect:sakila
   mssql.transaction.create
      mssql.execute:update actor set last_name = 'Smith' where actor_id = 1
```
