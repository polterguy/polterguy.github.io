---
title: "pgsql.* slots"
description: "The 11 slots named pgsql.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

11 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`pgsql.connect`](/reference/slots/pgsql/pgsql.connect/) | Opens a PostgreSQL connection. |
| [`pgsql.create`](/reference/slots/pgsql/pgsql.create/) | Inserts rows through the current PostgreSQL connection. |
| [`pgsql.delete`](/reference/slots/pgsql/pgsql.delete/) | Deletes rows through the current PostgreSQL connection; include a [where] child unless intentionally deleting every row in the table. |
| [`pgsql.execute`](/reference/slots/pgsql/pgsql.execute/) | Executes SQL on the current PostgreSQL connection. |
| [`pgsql.read`](/reference/slots/pgsql/pgsql.read/) | Reads rows through the current PostgreSQL connection. |
| [`pgsql.scalar`](/reference/slots/pgsql/pgsql.scalar/) | Executes SQL and returns a scalar value from the current PostgreSQL connection. |
| [`pgsql.select`](/reference/slots/pgsql/pgsql.select/) | Executes a SELECT query on the current PostgreSQL connection. |
| [`pgsql.transaction.commit`](/reference/slots/pgsql/pgsql.transaction.commit/) | Commits the current PostgreSQL transaction. |
| [`pgsql.transaction.create`](/reference/slots/pgsql/pgsql.transaction.create/) | Creates a PostgreSQL transaction. |
| [`pgsql.transaction.rollback`](/reference/slots/pgsql/pgsql.transaction.rollback/) | Rolls back the current PostgreSQL transaction. |
| [`pgsql.update`](/reference/slots/pgsql/pgsql.update/) | Updates rows through the current PostgreSQL connection; use [where] to constrain affected rows. |

