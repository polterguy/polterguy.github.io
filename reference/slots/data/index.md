---
title: "data.* slots"
description: "The 12 slots named data.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

12 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`data.connect`](/reference/slots/data/data.connect/) | Opens a database connection using the configured provider. |
| [`data.create`](/reference/slots/data/data.create/) | Inserts a new row into the current open database connection. |
| [`data.delete`](/reference/slots/data/data.delete/) | Deletes rows in the current open database connection; include a [where] child unless intentionally deleting every row in the table. |
| [`data.execute`](/reference/slots/data/data.execute/) | Executes SQL against the current database connection. |
| [`data.read`](/reference/slots/data/data.read/) | Selects rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied. |
| [`data.scalar`](/reference/slots/data/data.scalar/) | Executes SQL and returns a scalar value from the current database connection. |
| [`data.scan`](/reference/slots/data/data.scan/) | Scans rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied. |
| [`data.select`](/reference/slots/data/data.select/) | Executes a query and returns rows from the current database connection. |
| [`data.transaction.commit`](/reference/slots/data/data.transaction.commit/) | Commits the current database transaction using the configured provider. |
| [`data.transaction.create`](/reference/slots/data/data.transaction.create/) | Creates a database transaction using the configured provider. |
| [`data.transaction.rollback`](/reference/slots/data/data.transaction.rollback/) | Rolls back the current database transaction using the configured provider. |
| [`data.update`](/reference/slots/data/data.update/) | Updates rows in the current open database connection; use [where] to constrain affected rows. |

