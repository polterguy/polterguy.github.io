---
title: "[sql.delete]"
description: "sql.delete is a slot in the sql namespace of Magic Cloud. Builds a parameterized DELETE SQL statement; include a [where] child unless intentionally deleting every row in the table."
generated: true
llms: false
slot_json: "/reference/slots/sql/sql.delete/slot.json"
---

`sql.delete` is a slot in the `sql` namespace, in Hyperlambda, the language of Magic Cloud. Builds a parameterized DELETE SQL statement; include a [where] child unless intentionally deleting every row in the table.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
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

Guide: [How to use [sql.delete]](/plugins/magic.data.common/#how-to-use-sqldelete)

### JSON declaration

This is the complete declaration of `sql.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `sql.create`](/reference/slots/sql/sql.create/) | [all `sql.*` slots](/reference/slots/sql/) | [`sql.read` &rarr;](/reference/slots/sql/sql.read/)

