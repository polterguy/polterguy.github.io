---
title: mysql.* slots
description: The 11 slots named mysql.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [mysql.connect]

Opens a MySQL connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `mysql.connection` - Creates an open MySQL connection scope for mysql.* slots

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

## [mysql.create]

Inserts rows through the current MySQL connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[return-id]` | bool | no | Whether to return the created row ID. Default: `true`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |

## [mysql.delete]

Deletes rows through the current MySQL connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

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

## [mysql.execute]

Executes SQL on the current MySQL connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

## [mysql.read]

Reads rows through the current MySQL connection.

* **Returns**: Returns one child node per row read from the current MySQL connection
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[table]` / `[as]` | string | no | Optional table alias. |
| `[table]` / `[join]` | string | no | Joined table name. Can be repeated. |
| `[table]` / `[join]` / `[type]` | string | no | Join type: inner, left, right, or full. Default: `inner`. |
| `[table]` / `[join]` / `[as]` | string | no | Optional joined table alias. |
| `[table]` / `[join]` / `[on]` | lambda | yes | Join predicate tree comparing columns (AND-only at the schema level; the SQL builder still accepts hand-written [or] for legacy code). |
| `[distinct]` | bool | no | Removes duplicate rows from the result set when true. Default: `false`. |
| `[columns]` | lambda | no | Columns or aggregate expressions to select; omitted or empty means all columns. |
| `[columns]` / _any node name_ | string | no | Column name or aggregate expression; optional [as] child declares an alias. Can be repeated. |
| `[columns]` / _any node name_ / `[as]` | string | no | Column alias. |
| `[where]` | lambda | no | Optional boolean predicate tree. |
| `[where]` / `[and]` | lambda | no | Boolean AND group. |
| `[where]` / `[and]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[and]` / `[or]` | lambda | no | Boolean OR group. Can be repeated. |
| `[where]` / `[or]` | lambda | no | Boolean OR group. |
| `[where]` / `[or]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[or]` / `[and]` | lambda | no | Boolean AND group. Can be repeated. |
| `[group]` | lambda | no | Columns or aggregate expressions to group by. |
| `[group]` / _any node name_ | string | no | Column name or aggregate expression. Can be repeated. |
| `[order]` | string | no | Column, comma-separated columns, or aggregate expression to order by. Can be repeated. |
| `[order]` / `[direction]` | string | no | Order direction for this specific order node. Default: `asc`. |
| `[limit]` | long | no | Maximum number of rows to return; omitted defaults to 25 and -1 suppresses the generated limit clause. Default: `25`. |
| `[offset]` | long | no | Number of rows to skip. Default: `0`. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

## [mysql.scalar]

Executes SQL and returns a scalar value from the current MySQL connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

## [mysql.select]

Executes a SELECT query on the current MySQL connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | long | no | Maximum number of rows to return; omitted or -1 returns all rows. Default: `-1`. |
| `[multiple-result-sets]` | bool | no | Whether multiple SELECT statements in the SQL input should be returned as separate child result containers. Default: `false`. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

## [mysql.transaction.commit]

Commits the current MySQL transaction.

* **Scope**: requires `mysql.transaction` - Requires an active MySQL transaction created by [mysql.transaction.create]

## [mysql.transaction.create]

Creates a MySQL transaction.

* **Scope**: requires `mysql.connection`; provides `mysql.transaction` - Requires an open MySQL connection created by [mysql.connect]

## [mysql.transaction.rollback]

Rolls back the current MySQL transaction.

* **Scope**: requires `mysql.transaction` - Requires an active MySQL transaction created by [mysql.transaction.create]

## [mysql.update]

Updates rows through the current MySQL connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

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

