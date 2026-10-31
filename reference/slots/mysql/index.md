---
title: "mysql.* slots"
description: "The 11 slots named mysql.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

11 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`mysql.connect`](/reference/slots/mysql/mysql.connect/) | Opens a MySQL connection. |
| [`mysql.create`](/reference/slots/mysql/mysql.create/) | Inserts rows through the current MySQL connection. |
| [`mysql.delete`](/reference/slots/mysql/mysql.delete/) | Deletes rows through the current MySQL connection; include a [where] child unless intentionally deleting every row in the table. |
| [`mysql.execute`](/reference/slots/mysql/mysql.execute/) | Executes SQL on the current MySQL connection. |
| [`mysql.read`](/reference/slots/mysql/mysql.read/) | Reads rows through the current MySQL connection. |
| [`mysql.scalar`](/reference/slots/mysql/mysql.scalar/) | Executes SQL and returns a scalar value from the current MySQL connection. |
| [`mysql.select`](/reference/slots/mysql/mysql.select/) | Executes a SELECT query on the current MySQL connection. |
| [`mysql.transaction.commit`](/reference/slots/mysql/mysql.transaction.commit/) | Commits the current MySQL transaction. |
| [`mysql.transaction.create`](/reference/slots/mysql/mysql.transaction.create/) | Creates a MySQL transaction. |
| [`mysql.transaction.rollback`](/reference/slots/mysql/mysql.transaction.rollback/) | Rolls back the current MySQL transaction. |
| [`mysql.update`](/reference/slots/mysql/mysql.update/) | Updates rows through the current MySQL connection; use [where] to constrain affected rows. |

