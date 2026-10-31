---
title: "How to use [mssql.transaction.commit]"
description: "How to use [mssql.transaction.commit] - This slot commits the open transaction."
generated: true
guide: true
---

The reference page of [`mssql.transaction.commit`](/reference/slots/mssql/mssql.transaction.commit/) has its arguments, constraints and declaration.

This slot commits the open transaction. It works like **[data.transaction.commit]**. Without it a transaction is rolled back when it leaves scope. Below is an example.

```
mssql.connect:sakila
   mssql.transaction.create
      mssql.execute:update actor set last_name = 'Smith' where actor_id = 1
      mssql.transaction.commit
```
