---
title: magic.lambda.sqlite slot reference
description: Every slot in magic.lambda.sqlite with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.sqlite](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.sqlite). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/)._

## [.db-factory.connection.sqlite]

Creates a SQLite connection factory.

* **Returns**: Resolves to a new SQLite connection instance

## [sqlite.backup]

Creates a backup of the current SQLite connection.

* **Value** (`file-path`), required: Target SQLite database filename under files/data/

Guide: [How to use [sqlite.backup]](/plugins/magic.lambda.sqlite/#how-to-use-sqlitebackup)

## [sqlite.connect]

Opens a SQLite connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override

## [sqlite.connections.flush]

Flushes cached SQLite connections.


## [sqlite.create]

Inserts rows through the current SQLite connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null

## [sqlite.delete]

Deletes rows through the current SQLite connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected

## [sqlite.execute]

Executes SQL on the current SQLite connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement

## [sqlite.load-extension]

Loads a SQLite extension into the current connection from child-node arguments.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | yes | SQLite extension filename |
| `[proc]` | string | no | Optional extension entry point |
| `[append-platform]` | bool | no | Whether to append the current platform suffix |

Guide: [How to use [sqlite.load-extension]](/plugins/magic.lambda.sqlite/#how-to-use-sqliteload-extension)

## [sqlite.read]

Reads rows through the current SQLite connection.

* **Returns**: Returns one child node per row read from the current SQLite connection

## [sqlite.scalar]

Executes SQL and returns a scalar value from the current SQLite connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement

## [sqlite.select]

Executes a SELECT query on the current SQLite connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query

## [sqlite.transaction.commit]

Commits the current SQLite transaction.


## [sqlite.transaction.create]

Creates a SQLite transaction.


## [sqlite.transaction.rollback]

Rolls back the current SQLite transaction.


## [sqlite.update]

Updates rows through the current SQLite connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected

