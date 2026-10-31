---
title: magic.data.common slot reference
description: Every slot in magic.data.common with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.data.common](https://github.com/polterguy/magic/tree/master/plugins/magic.data.common). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.data.common](/plugins/magic.data.common/)._

## [data.connect]

Opens a database connection using the configured provider.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default |

Guide: [How to use [data.connect]](/plugins/magic.data.common/#how-to-use-dataconnect)

## [data.create]

Inserts a new row into the current open database connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` |  | no | Database adapter to use instead of the configured default |

Guide: [How to use [data.create]](/plugins/magic.data.common/#how-to-use-datacreate)

## [data.delete]

Deletes rows in the current open database connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected

## [data.execute]

Executes SQL against the current database connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | SQL parameter value; child name is used as the parameter name referenced by the SQL statement |

Guide: [How to use [data.execute]](/plugins/magic.data.common/#how-to-use-dataexecute)

## [data.read]

Selects rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied.

* **Returns**: Resolves to matching rows as child nodes

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | Column value; child name is the column name (or alias) declared in the read |
| `[*]` |  | Column name or aggregate expression; optional [as] child declares an alias |
| `[*]` |  | Column name or aggregate expression |

## [data.scalar]

Executes SQL and returns a scalar value from the current database connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to a scalar value from the current database connection

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | SQL parameter value; child name is used as the parameter name referenced by the SQL statement |

Guide: [How to use [data.scalar]](/plugins/magic.data.common/#how-to-use-datascalar)

## [data.scan]

Scans rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied.

* **Returns**: Resolves to scanned rows as child nodes

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | Column value; child name is the column name (or alias) declared in the read |
| `[*]` |  | Column name or aggregate expression; optional [as] child declares an alias |
| `[*]` |  | Column name or aggregate expression |

Guide: [How to use [data.scan]](/plugins/magic.data.common/#how-to-use-datascan)

## [data.select]

Executes a query and returns rows from the current database connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Resolves to query result rows as child nodes

| Returned node | Type | Description |
|---|---|---|
| `[max]` | long | Maximum number of rows to return; omitted or -1 returns all rows |
| `[multiple-result-sets]` | bool | Whether multiple SELECT statements in the SQL input should be returned as separate child result containers |

Guide: [How to use [data.select]](/plugins/magic.data.common/#how-to-use-dataselect)

## [data.transaction.commit]

Commits the current database transaction using the configured provider.


## [data.transaction.create]

Creates a database transaction using the configured provider.


## [data.transaction.rollback]

Rolls back the current database transaction using the configured provider.


## [data.update]

Updates rows in the current open database connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected

Guide: [How to use [data.update]](/plugins/magic.data.common/#how-to-use-dataupdate)

## [sql.create]

Builds a parameterized INSERT SQL statement.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Column name and value |
| `[.]` |  | no | Value item used by operators such as .in |
| `[type]` |  | no | Join type: inner, left, right, or full |
| `[as]` |  | no | Optional joined table alias |
| `[on]` |  | yes | Join predicate tree comparing columns (AND-only at the schema level; the SQL builder still accepts hand-written [or] for legacy code) |

Guide: [How to use [sql.create]](/plugins/magic.data.common/#how-to-use-sqlcreate)

## [sql.delete]

Builds a parameterized DELETE SQL statement; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

Guide: [How to use [sql.delete]](/plugins/magic.data.common/#how-to-use-sqldelete)

## [sql.read]

Builds a parameterized SELECT SQL statement.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | Column value; child name is the column name (or alias) declared in the read |
| `[*]` |  | Column name or aggregate expression; optional [as] child declares an alias |
| `[*]` |  | Column name or aggregate expression |

Guide: [How to use [sql.read]](/plugins/magic.data.common/#how-to-use-sqlread)

## [sql.update]

Builds a parameterized UPDATE SQL statement; use [where] to constrain affected rows.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

Guide: [How to use [sql.update]](/plugins/magic.data.common/#how-to-use-sqlupdate)

