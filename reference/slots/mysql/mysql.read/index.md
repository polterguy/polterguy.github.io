---
title: "[mysql.read]"
description: "mysql.read is a slot in the mysql namespace of Magic Cloud. Reads rows through the current MySQL connection."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.read/slot.json"
---

`mysql.read` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Reads rows through the current MySQL connection.

* **Returns**: Returns one child node per row read from the current MySQL connection
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

### Arguments

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
| `[table]` / `[join]` / `[on]` / `[and]` | lambda | yes | Boolean AND group. |
| `[table]` / `[join]` / `[on]` / `[and]` / _any node name_ | object | yes | Join predicate: LHS is a column-with-operator suffix, RHS is the joined-side column reference (leaf-only — value-list children are a WHERE-clause feature, not meaningful in JOIN ON). |
| `[table]` / `[join]` / `[type]` | string | no | Join type: inner, left, right, or full. Default: `inner`. |
| `[where]` | lambda | no | Optional boolean predicate tree. |
| `[where]` / `[and]` | lambda | no | Boolean AND group. |
| `[where]` / `[and]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[and]` / _any node name_ / _unnamed child node_ | object | no | Value item used by operators such as .in. |
| `[where]` / `[and]` / `[or]` | lambda | no | Boolean OR group. Can be repeated. |
| `[where]` / `[and]` / `[or]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[and]` / `[or]` / _any node name_ / _unnamed child node_ | object | no | Value item used by operators such as .in. |
| `[where]` / `[or]` | lambda | no | Boolean OR group. |
| `[where]` / `[or]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[or]` / _any node name_ / _unnamed child node_ | object | no | Value item used by operators such as .in. |
| `[where]` / `[or]` / `[and]` | lambda | no | Boolean AND group. Can be repeated. |
| `[where]` / `[or]` / `[and]` / _any node name_ | object | yes | Column condition; suffix the name with .eq, .neq, .gt, .gte, .lt, .lte, .like, .ilike, or .in to select an operator. Can be repeated. |
| `[where]` / `[or]` / `[and]` / _any node name_ / _unnamed child node_ | object | no | Value item used by operators such as .in. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

### JSON declaration

This is the complete declaration of `mysql.read`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `mysql.execute`](/reference/slots/mysql/mysql.execute/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.scalar` &rarr;](/reference/slots/mysql/mysql.scalar/)

