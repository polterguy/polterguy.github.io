---
title: "How to use [mssql.transaction.rollback]"
description: "How to use [mssql.transaction.rollback] - This slot explicitly rolls back the open transaction, discarding everything done since it was created."
generated: true
guide: true
---

The reference page of [`mssql.transaction.rollback`](/reference/slots/mssql/mssql.transaction.rollback/) has its arguments, constraints and declaration.

This slot explicitly rolls back the open transaction, discarding everything done since it was created. It works like **[data.transaction.rollback]**. Below is an example.

```
mssql.connect:sakila
   mssql.transaction.create
      mssql.execute:update actor set last_name = 'Smith' where actor_id = 1
      mssql.transaction.rollback
```
