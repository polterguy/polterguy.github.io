---
title: magic.lambda.mysql slot reference
description: Every slot in magic.lambda.mysql with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.mysql](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.mysql). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.mysql](/plugins/magic.lambda.mysql/)._

## [.db-factory.connection.mysql]

Creates a MySQL connection factory.

* **Returns**: Resolves to a new MySQL connection instance

## [mysql.connect]

Opens a MySQL connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override

## [mysql.create]

Inserts rows through the current MySQL connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null

## [mysql.delete]

Deletes rows through the current MySQL connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected

## [mysql.execute]

Executes SQL on the current MySQL connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement

## [mysql.read]

Reads rows through the current MySQL connection.

* **Returns**: Returns one child node per row read from the current MySQL connection

## [mysql.scalar]

Executes SQL and returns a scalar value from the current MySQL connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement

## [mysql.select]

Executes a SELECT query on the current MySQL connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query

## [mysql.transaction.commit]

Commits the current MySQL transaction.


## [mysql.transaction.create]

Creates a MySQL transaction.


## [mysql.transaction.rollback]

Rolls back the current MySQL transaction.


## [mysql.update]

Updates rows through the current MySQL connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected

