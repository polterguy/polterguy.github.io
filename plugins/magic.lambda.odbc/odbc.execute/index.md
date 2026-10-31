---
title: "How to use [odbc.execute]"
description: "How to use [odbc.execute] - This slot executes SQL you do not expect any result from, such as updates and deletes."
generated: true
guide: true
---

The reference page of [`odbc.execute`](/reference/slots/odbc/odbc.execute/) has its arguments, constraints and declaration.

This slot executes SQL you do not expect any result from, such as updates and deletes. It works like **[data.execute]**, except it always uses ODBC. Below is an example.

```
odbc.connect:sakila
   odbc.execute:update actor set last_name = 'Smith' where actor_id = 1
```
