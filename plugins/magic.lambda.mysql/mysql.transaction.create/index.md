---
title: "How to use [mysql.transaction.create]"
description: "How to use [mysql.transaction.create] - This slot creates a database transaction, and evaluates its lambda object inside of it."
generated: true
guide: true
---

The reference page of [`mysql.transaction.create`](/reference/slots/mysql/mysql.transaction.create/) has its arguments, constraints and declaration.

This slot creates a database transaction, and evaluates its lambda object inside of it. It works like **[data.transaction.create]**. Unless the transaction is explicitly committed before it leaves scope, it is rolled back, which is what happens below.

```
mysql.connect:sakila
   mysql.transaction.create
      mysql.execute:update actor set last_name = 'Smith' where actor_id = 1
```
