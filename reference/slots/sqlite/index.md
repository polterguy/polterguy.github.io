---
title: sqlite.* slots
description: The 14 slots named sqlite.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [sqlite.backup]

Creates a backup of the current SQLite connection.

* **Value** (`file-path`), required: Target SQLite database filename under files/data/
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

Guide: [How to use [sqlite.backup]](/plugins/magic.lambda.sqlite/#how-to-use-sqlitebackup)

## [sqlite.connect]

Opens a SQLite connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `sqlite.connection` - Creates an open SQLite connection scope for sqlite.* slots

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

## [sqlite.connections.flush]

Flushes cached SQLite connections.

## [sqlite.create]

Inserts rows through the current SQLite connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[return-id]` | bool | no | Whether to return the created row ID. Default: `true`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |

## [sqlite.delete]

Deletes rows through the current SQLite connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[where]` | lambda | yes | Required boolean predicate tree — destructive SQL must constrain affected rows. |
| `[where]` / `[and]` | lambda | no | Boolean AND group. |
| `[where]` / `[and]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[and]` / `[or]` | lambda | no | Boolean OR group. Can be repeated. |
| `[where]` / `[or]` | lambda | no | Boolean OR group. |
| `[where]` / `[or]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[or]` / `[and]` | lambda | no | Boolean AND group. Can be repeated. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

## [sqlite.execute]

Executes SQL on the current SQLite connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

## [sqlite.load-extension]

Loads a SQLite extension into the current connection from child-node arguments.

* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[append-platform]` | bool | no | Whether to append the current platform suffix. Default: `true`. |
| `[file]` | string | yes | SQLite extension filename. |
| `[proc]` | string | no | Optional extension entry point. |

Guide: [How to use [sqlite.load-extension]](/plugins/magic.lambda.sqlite/#how-to-use-sqliteload-extension)

## [sqlite.read]

Reads rows through the current SQLite connection.

* **Returns**: Returns one child node per row read from the current SQLite connection
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[columns]` | lambda | no | Columns or aggregate expressions to select; omitted or empty means all columns. |
| `[columns]` / _any node name_ | string | no | Column name or aggregate expression; optional [as] child declares an alias. Can be repeated. |
| `[columns]` / _any node name_ / `[as]` | string | no | Column alias. |
| `[distinct]` | bool | no | Removes duplicate rows from the result set when true. Default: `false`. |
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[group]` | lambda | no | Columns or aggregate expressions to group by. |
| `[group]` / _any node name_ | string | no | Column name or aggregate expression. Can be repeated. |
| `[limit]` | long | no | Maximum number of rows to return; omitted defaults to 25 and -1 suppresses the generated limit clause. Default: `25`. |
| `[offset]` | long | no | Number of rows to skip. Default: `0`. |
| `[order]` | string | no | Column, comma-separated columns, or aggregate expression to order by. Can be repeated. |
| `[order]` / `[direction]` | string | no | Order direction for this specific order node. Default: `asc`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[table]` / `[as]` | string | no | Optional table alias. |
| `[table]` / `[join]` | string | no | Joined table name. Can be repeated. |
| `[table]` / `[join]` / `[as]` | string | no | Optional joined table alias. |
| `[table]` / `[join]` / `[on]` | lambda | yes | Join predicate tree comparing columns (AND-only at the schema level; the SQL builder still accepts hand-written [or] for legacy code). |
| `[table]` / `[join]` / `[type]` | string | no | Join type: inner, left, right, or full. Default: `inner`. |
| `[where]` | lambda | no | Optional boolean predicate tree. |
| `[where]` / `[and]` | lambda | no | Boolean AND group. |
| `[where]` / `[and]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[and]` / `[or]` | lambda | no | Boolean OR group. Can be repeated. |
| `[where]` / `[or]` | lambda | no | Boolean OR group. |
| `[where]` / `[or]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[or]` / `[and]` | lambda | no | Boolean AND group. Can be repeated. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

## [sqlite.scalar]

Executes SQL and returns a scalar value from the current SQLite connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

## [sqlite.select]

Executes a SELECT query on the current SQLite connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |
| `[max]` | long | no | Maximum number of rows to return; omitted or -1 returns all rows. Default: `-1`. |
| `[multiple-result-sets]` | bool | no | Whether multiple SELECT statements in the SQL input should be returned as separate child result containers. Default: `false`. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

## [sqlite.transaction.commit]

Commits the current SQLite transaction.

* **Scope**: requires `sqlite.transaction` - Requires an active SQLite transaction created by [sqlite.transaction.create]

## [sqlite.transaction.create]

Creates a SQLite transaction.

* **Scope**: requires `sqlite.connection`; provides `sqlite.transaction` - Requires an open SQLite connection created by [sqlite.connect]

## [sqlite.transaction.rollback]

Rolls back the current SQLite transaction.

* **Scope**: requires `sqlite.transaction` - Requires an active SQLite transaction created by [sqlite.transaction.create]

## [sqlite.update]

Updates rows through the current SQLite connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |
| `[where]` | lambda | yes | Required boolean predicate tree — destructive SQL must constrain affected rows. |
| `[where]` / `[and]` | lambda | no | Boolean AND group. |
| `[where]` / `[and]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[and]` / `[or]` | lambda | no | Boolean OR group. Can be repeated. |
| `[where]` / `[or]` | lambda | no | Boolean OR group. |
| `[where]` / `[or]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[or]` / `[and]` | lambda | no | Boolean AND group. Can be repeated. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

