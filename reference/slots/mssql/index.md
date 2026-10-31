---
title: "mssql.* slots"
description: "The 12 slots named mssql.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

12 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`mssql.connect`](/reference/slots/mssql/mssql.connect/) | Opens a SQL Server connection. |
| [`mssql.create`](/reference/slots/mssql/mssql.create/) | Inserts rows through the current SQL Server connection. |
| [`mssql.delete`](/reference/slots/mssql/mssql.delete/) | Deletes rows through the current SQL Server connection; include a [where] child unless intentionally deleting every row in the table. |
| [`mssql.execute`](/reference/slots/mssql/mssql.execute/) | Executes SQL on the current SQL Server connection. |
| [`mssql.execute-batch`](/reference/slots/mssql/mssql.execute-batch/) | Executes a batch SQL script on the current SQL Server connection. |
| [`mssql.read`](/reference/slots/mssql/mssql.read/) | Reads rows through the current SQL Server connection. |
| [`mssql.scalar`](/reference/slots/mssql/mssql.scalar/) | Executes SQL and returns a scalar value from the current SQL Server connection. |
| [`mssql.select`](/reference/slots/mssql/mssql.select/) | Executes a SELECT query on the current SQL Server connection. |
| [`mssql.transaction.commit`](/reference/slots/mssql/mssql.transaction.commit/) | Commits the current SQL Server transaction. |
| [`mssql.transaction.create`](/reference/slots/mssql/mssql.transaction.create/) | Creates a SQL Server transaction. |
| [`mssql.transaction.rollback`](/reference/slots/mssql/mssql.transaction.rollback/) | Rolls back the current SQL Server transaction. |
| [`mssql.update`](/reference/slots/mssql/mssql.update/) | Updates rows through the current SQL Server connection; use [where] to constrain affected rows. |

