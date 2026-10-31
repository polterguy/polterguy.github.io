---
title: "How to use [sqlite.execute]"
description: "How to use [sqlite.execute] - This slot executes SQL you do not expect any result from, such as updates and deletes."
generated: true
guide: true
---

The reference page of [`sqlite.execute`](/reference/slots/sqlite/sqlite.execute/) has its arguments, constraints and declaration.

This slot executes SQL you do not expect any result from, such as updates and deletes. It works like **[data.execute]**, except it always uses SQLite. Below is an example.

```
sqlite.connect:sakila
   sqlite.execute:update actor set last_name = 'Smith' where actor_id = 1
```
