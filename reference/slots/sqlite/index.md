---
title: "sqlite.* slots"
description: "The 14 slots named sqlite.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

14 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`sqlite.backup`](/reference/slots/sqlite/sqlite.backup/) | Creates a backup of the current SQLite connection. |
| [`sqlite.connect`](/reference/slots/sqlite/sqlite.connect/) | Opens a SQLite connection. |
| [`sqlite.connections.flush`](/reference/slots/sqlite/sqlite.connections.flush/) | Flushes cached SQLite connections. |
| [`sqlite.create`](/reference/slots/sqlite/sqlite.create/) | Inserts rows through the current SQLite connection. |
| [`sqlite.delete`](/reference/slots/sqlite/sqlite.delete/) | Deletes rows through the current SQLite connection; include a [where] child unless intentionally deleting every row in the table. |
| [`sqlite.execute`](/reference/slots/sqlite/sqlite.execute/) | Executes SQL on the current SQLite connection. |
| [`sqlite.load-extension`](/reference/slots/sqlite/sqlite.load-extension/) | Loads a SQLite extension into the current connection from child-node arguments. |
| [`sqlite.read`](/reference/slots/sqlite/sqlite.read/) | Reads rows through the current SQLite connection. |
| [`sqlite.scalar`](/reference/slots/sqlite/sqlite.scalar/) | Executes SQL and returns a scalar value from the current SQLite connection. |
| [`sqlite.select`](/reference/slots/sqlite/sqlite.select/) | Executes a SELECT query on the current SQLite connection. |
| [`sqlite.transaction.commit`](/reference/slots/sqlite/sqlite.transaction.commit/) | Commits the current SQLite transaction. |
| [`sqlite.transaction.create`](/reference/slots/sqlite/sqlite.transaction.create/) | Creates a SQLite transaction. |
| [`sqlite.transaction.rollback`](/reference/slots/sqlite/sqlite.transaction.rollback/) | Rolls back the current SQLite transaction. |
| [`sqlite.update`](/reference/slots/sqlite/sqlite.update/) | Updates rows through the current SQLite connection; use [where] to constrain affected rows. |

