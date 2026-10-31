---
title: magic.lambda.pgsql slot reference
description: Every slot in magic.lambda.pgsql with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.pgsql](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.pgsql). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.pgsql](/plugins/magic.lambda.pgsql/)._

## [.db-factory.connection.pgsql]

Creates a PostgreSQL connection factory.

* **Returns**: Resolves to a new PostgreSQL connection instance

## [pgsql.connect]

Opens a PostgreSQL connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override

## [pgsql.create]

Inserts rows through the current PostgreSQL connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null

## [pgsql.delete]

Deletes rows through the current PostgreSQL connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected

## [pgsql.execute]

Executes SQL on the current PostgreSQL connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement

## [pgsql.read]

Reads rows through the current PostgreSQL connection.

* **Returns**: Returns one child node per row read from the current PostgreSQL connection

## [pgsql.scalar]

Executes SQL and returns a scalar value from the current PostgreSQL connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement

## [pgsql.select]

Executes a SELECT query on the current PostgreSQL connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query

## [pgsql.transaction.commit]

Commits the current PostgreSQL transaction.


## [pgsql.transaction.create]

Creates a PostgreSQL transaction.


## [pgsql.transaction.rollback]

Rolls back the current PostgreSQL transaction.


## [pgsql.update]

Updates rows through the current PostgreSQL connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected

