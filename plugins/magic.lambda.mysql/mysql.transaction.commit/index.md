---
title: "How to use [mysql.transaction.commit]"
description: "How to use [mysql.transaction.commit] - This slot commits the open transaction."
generated: true
guide: true
---

The reference page of [`mysql.transaction.commit`](/reference/slots/mysql/mysql.transaction.commit/) has its arguments, constraints and declaration.

This slot commits the open transaction. It works like **[data.transaction.commit]**. Without it a transaction is rolled back when it leaves scope. Below is an example.

```
mysql.connect:sakila
   mysql.transaction.create
      mysql.execute:update actor set last_name = 'Smith' where actor_id = 1
      mysql.transaction.commit
```
