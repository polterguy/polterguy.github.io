---
title: "[data.update]"
description: "data.update is a slot in the data namespace of Magic Cloud. Updates rows in the current open database connection; use [where] to constrain affected rows."
generated: true
llms: "guide"
slot_json: "/reference/slots/data/data.update/slot.json"
---

`data.update` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Updates rows in the current open database connection; use [where] to constrain affected rows.

* **Returns**: Resolves to the number of rows affected
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |
| `[where]` | lambda | yes | Required boolean predicate tree — destructive SQL must constrain affected rows. |
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
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Guide

<!-- guide -->
This slot updates rows in your database, using the current open connection created by **[data.connect]**.
It takes the same arguments as **[sql.update]**, and its value resolves to the number of rows affected.
Always supply a **[where]** argument to constrain which rows are updated, since the SQL generated does not
constrain the update to any specific row if you leave it out.

* __[table]__ - Name of the table to update. Mandatory, the slot throws if it is missing
* __[values]__ - Column names and their new values, as children nodes. Mandatory, the slot throws if it is missing
* __[where]__ - Condition constraining which rows to update, see the **[where]** documentation below
* __[database-type]__ - Database adapter to use instead of your default database type
* __[generate]__ - If true, only generates the SQL and its parameters instead of executing it, default is false
<!-- /guide -->

### Related documentation

* Part of the [magic.data.common](/plugins/magic.data.common/) plugin, which documents every slot it contains.
* Discussed in [How to use [data.*]](/plugins/magic.data.common/how-to-use-data/).

### JSON declaration

This is the complete declaration of `data.update`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `data.transaction.rollback`](/reference/slots/data/data.transaction.rollback/) | [all `data.*` slots](/reference/slots/data/)

