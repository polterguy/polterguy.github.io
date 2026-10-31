---
title: "How to use [odbc.transaction.rollback]"
description: "How to use [odbc.transaction.rollback] - This slot explicitly rolls back the open transaction, discarding everything done since it was created."
generated: true
guide: true
---

The reference page of [`odbc.transaction.rollback`](/reference/slots/odbc/odbc.transaction.rollback/) has its arguments, constraints and declaration.

This slot explicitly rolls back the open transaction, discarding everything done since it was created. It works like **[data.transaction.rollback]**. Below is an example.

```
odbc.connect:sakila
   odbc.transaction.create
      odbc.execute:update actor set last_name = 'Smith' where actor_id = 1
      odbc.transaction.rollback
```
