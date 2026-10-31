---
title: magic.lambda.mssql slot reference
description: Every slot in magic.lambda.mssql with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.mssql](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.mssql). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.mssql](/plugins/magic.lambda.mssql/)._

## [.db-factory.connection.mssql]

Creates a SQL Server connection factory.

* **Returns**: Resolves to a new SQL Server connection instance

## [mssql.connect]

Opens a SQL Server connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override

## [mssql.create]

Inserts rows through the current SQL Server connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null

## [mssql.delete]

Deletes rows through the current SQL Server connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected

## [mssql.execute]

Executes SQL on the current SQL Server connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement

## [mssql.execute-batch]

Executes a batch SQL script on the current SQL Server connection.

* **Value** (`sql-batch`), required: Batch SQL script to execute
* **Returns**: Returns one child node per batch execution result

Guide: [How to use [mssql.execute-batch]](/plugins/magic.lambda.mssql/#how-to-use-mssqlexecute-batch)

## [mssql.read]

Reads rows through the current SQL Server connection.

* **Returns**: Returns one child node per row read from the current SQL Server connection

## [mssql.scalar]

Executes SQL and returns a scalar value from the current SQL Server connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement

## [mssql.select]

Executes a SELECT query on the current SQL Server connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query

## [mssql.transaction.commit]

Commits the current SQL Server transaction.


## [mssql.transaction.create]

Creates a SQL Server transaction.


## [mssql.transaction.rollback]

Rolls back the current SQL Server transaction.


## [mssql.update]

Updates rows through the current SQL Server connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected

