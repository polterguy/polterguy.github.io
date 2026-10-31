---
title: "How to use [mysql.transaction.rollback]"
description: "How to use [mysql.transaction.rollback] - This slot explicitly rolls back the open transaction, discarding everything done since it was created."
generated: true
guide: true
---

The reference page of [`mysql.transaction.rollback`](/reference/slots/mysql/mysql.transaction.rollback/) has its arguments, constraints and declaration.

This slot explicitly rolls back the open transaction, discarding everything done since it was created. It works like **[data.transaction.rollback]**. Below is an example.

```
mysql.connect:sakila
   mysql.transaction.create
      mysql.execute:update actor set last_name = 'Smith' where actor_id = 1
      mysql.transaction.rollback
```
