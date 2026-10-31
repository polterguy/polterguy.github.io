---
title: "How to use [mysql.execute]"
description: "How to use [mysql.execute] - This slot executes SQL you do not expect any result from, such as updates and deletes."
generated: true
guide: true
---

The reference page of [`mysql.execute`](/reference/slots/mysql/mysql.execute/) has its arguments, constraints and declaration.

This slot executes SQL you do not expect any result from, such as updates and deletes. It works like **[data.execute]**, except it always uses MySQL. Below is an example.

```
mysql.connect:sakila
   mysql.execute:update actor set last_name = 'Smith' where actor_id = 1
```
