---
title: magic.lambda.odbc slot reference
description: Every slot in magic.lambda.odbc with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.odbc](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.odbc). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.odbc](/plugins/magic.lambda.odbc/)._

## [odbc.connect]

Opens a ODBC connection.

* **Value** (`connection-string`), optional: Optional ODBC connection string override; ODBC does not use the database-name shorthand supported by other database providers

## [odbc.execute]

Executes SQL on the current ODBC connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement

## [odbc.scalar]

Executes SQL and returns a scalar value from the current ODBC connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement

## [odbc.select]

Executes a SELECT query on the current ODBC connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query

## [odbc.transaction.commit]

Commits the current ODBC transaction.


## [odbc.transaction.create]

Creates a ODBC transaction.


## [odbc.transaction.rollback]

Rolls back the current ODBC transaction.


