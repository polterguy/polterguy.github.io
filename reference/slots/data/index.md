---
title: data.* slots
description: The 12 slots named data.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [data.connect]

Opens a database connection using the configured provider.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `data.connection` - Creates an open database connection scope for data.* slots

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

Guide: [How to use [data.connect]](/plugins/magic.data.common/#how-to-use-dataconnect)

## [data.create]

Inserts a new row into the current open database connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[return-id]` | bool | no | Whether to return the created row ID. Default: `true`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |

Guide: [How to use [data.create]](/plugins/magic.data.common/#how-to-use-datacreate)

## [data.delete]

Deletes rows in the current open database connection; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
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

## [data.execute]

Executes SQL against the current database connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

Guide: [How to use [data.execute]](/plugins/magic.data.common/#how-to-use-dataexecute)

## [data.read]

Selects rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied.

* **Returns**: Resolves to matching rows as child nodes
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
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

## [data.scalar]

Executes SQL and returns a scalar value from the current database connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to a scalar value from the current database connection
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

Guide: [How to use [data.scalar]](/plugins/magic.data.common/#how-to-use-datascalar)

## [data.scan]

Scans rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied.

* **Returns**: Resolves to scanned rows as child nodes
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
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

Guide: [How to use [data.scan]](/plugins/magic.data.common/#how-to-use-datascan)

## [data.select]

Executes a query and returns rows from the current database connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Resolves to query result rows as child nodes
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| `[max]` | long | no | Maximum number of rows to return; omitted or -1 returns all rows. Default: `-1`. |
| `[multiple-result-sets]` | bool | no | Whether multiple SELECT statements in the SQL input should be returned as separate child result containers. Default: `false`. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

Guide: [How to use [data.select]](/plugins/magic.data.common/#how-to-use-dataselect)

## [data.transaction.commit]

Commits the current database transaction using the configured provider.

* **Scope**: requires `data.transaction` - Requires an active database transaction created by [data.transaction.create]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |

## [data.transaction.create]

Creates a database transaction using the configured provider.

* **Scope**: requires `data.connection`; provides `data.transaction` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |

## [data.transaction.rollback]

Rolls back the current database transaction using the configured provider.

* **Scope**: requires `data.transaction` - Requires an active database transaction created by [data.transaction.create]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |

## [data.update]

Updates rows in the current open database connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
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

Guide: [How to use [data.update]](/plugins/magic.data.common/#how-to-use-dataupdate)

