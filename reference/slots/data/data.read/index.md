---
title: "[data.read]"
description: "data.read is a slot in the data namespace of Magic Cloud. Selects rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied."
generated: true
llms: false
slot_json: "/reference/slots/data/data.read/slot.json"
---

`data.read` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Selects rows from the current open database connection; returns all columns unless [columns] is supplied and limits to 25 rows unless [limit] is supplied.

* **Returns**: Resolves to matching rows as child nodes
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[table]` / `[as]` | string | no | Optional table alias. |
| `[table]` / `[join]` | string | no | Joined table name. Can be repeated. |
| `[table]` / `[join]` / `[on]` | lambda | yes | Join predicate tree comparing columns (AND-only at the schema level; the SQL builder still accepts hand-written [or] for legacy code). |
| `[table]` / `[join]` / `[on]` / `[and]` | lambda | yes | Boolean AND group. |
| `[table]` / `[join]` / `[on]` / `[and]` / _any node name_ | object | yes | Join predicate: LHS is a column-with-operator suffix, RHS is the joined-side column reference (leaf-only — value-list children are a WHERE-clause feature, not meaningful in JOIN ON). |
| `[table]` / `[join]` / `[type]` | string | no | Join type: inner, left, right, or full. Default: `inner`. |
| `[table]` / `[join]` / `[as]` | string | no | Optional joined table alias. |
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[distinct]` | bool | no | Removes duplicate rows from the result set when true. Default: `false`. |
| `[columns]` | lambda | no | Columns or aggregate expressions to select; omitted or empty means all columns. |
| `[columns]` / _any node name_ | string | no | Column name or aggregate expression; optional [as] child declares an alias. Can be repeated. |
| `[columns]` / _any node name_ / `[as]` | string | no | Column alias. |
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
| `[group]` | lambda | no | Columns or aggregate expressions to group by. |
| `[group]` / _any node name_ | string | no | Column name or aggregate expression. Can be repeated. |
| `[order]` | string | no | Column, comma-separated columns, or aggregate expression to order by. Can be repeated. |
| `[order]` / `[direction]` | string | no | Order direction for this specific order node. Default: `asc`. |
| `[direction]` | string | no | Default order direction. Default: `asc`. |
| `[limit]` | long | no | Maximum number of rows to return; omitted defaults to 25 and -1 suppresses the generated limit clause. Default: `25`. |
| `[offset]` | long | no | Number of rows to skip. Default: `0`. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

### Guide

[How to use `data.read`](/plugins/magic.data.common/sql.read/)

### JSON declaration

This is the complete declaration of `data.read`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `data.execute`](/reference/slots/data/data.execute/) | [all `data.*` slots](/reference/slots/data/) | [`data.scalar` &rarr;](/reference/slots/data/data.scalar/)

