---
title: "How to use [odbc.transaction.commit]"
description: "How to use [odbc.transaction.commit] - This slot commits the open transaction."
generated: true
guide: true
---

The reference page of [`odbc.transaction.commit`](/reference/slots/odbc/odbc.transaction.commit/) has its arguments, constraints and declaration.

This slot commits the open transaction. It works like **[data.transaction.commit]**. Without it a transaction is rolled back when it leaves scope. Below is an example.

```
odbc.connect:sakila
   odbc.transaction.create
      odbc.execute:update actor set last_name = 'Smith' where actor_id = 1
      odbc.transaction.commit
```
