---
title: odbc.* slots
description: The 7 slots named odbc.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [odbc.connect]

Opens a ODBC connection.

* **Value** (`connection-string`), optional: Optional ODBC connection string override; ODBC does not use the database-name shorthand supported by other database providers
* **Scope**: provides `odbc.connection` - Creates an open ODBC connection scope for odbc.* slots

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

## [odbc.execute]

Executes SQL on the current ODBC connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `odbc.connection` - Requires an open ODBC connection created by [odbc.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

## [odbc.scalar]

Executes SQL and returns a scalar value from the current ODBC connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `odbc.connection` - Requires an open ODBC connection created by [odbc.connect]

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

## [odbc.select]

Executes a SELECT query on the current ODBC connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query
* **Scope**: requires `odbc.connection` - Requires an open ODBC connection created by [odbc.connect]

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

## [odbc.transaction.commit]

Commits the current ODBC transaction.

* **Scope**: requires `odbc.transaction` - Requires an active ODBC transaction created by [odbc.transaction.create]

## [odbc.transaction.create]

Creates a ODBC transaction.

* **Scope**: requires `odbc.connection`; provides `odbc.transaction` - Requires an open ODBC connection created by [odbc.connect]

## [odbc.transaction.rollback]

Rolls back the current ODBC transaction.

* **Scope**: requires `odbc.transaction` - Requires an active ODBC transaction created by [odbc.transaction.create]

