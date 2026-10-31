---
title: "How to use [sqlite.connections.flush]"
description: "How to use [sqlite.connections.flush] - This slot clears all of SQLite's pooled connections, which you typically need to do after you have replaced or deleted a database file on disc, since a pooled connection would o..."
generated: true
guide: true
---

The reference page of [`sqlite.connections.flush`](/reference/slots/sqlite/sqlite.connections.flush/) has its arguments, constraints and declaration.

This slot clears all of SQLite's pooled connections, which you typically need to do after you have replaced or deleted a database file on disc, since a pooled connection would otherwise keep pointing at the old file. Below is an example.

```
sqlite.connections.flush
```
