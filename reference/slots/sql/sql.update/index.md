---
title: "[sql.update]"
description: "sql.update is a slot in the sql namespace of Magic Cloud. Builds a parameterized UPDATE SQL statement; use [where] to constrain affected rows."
generated: true
llms: "guide"
slot_json: "/reference/slots/sql/sql.update/slot.json"
---

`sql.update` is a slot in the `sql` namespace, in Hyperlambda, the language of Magic Cloud. Builds a parameterized UPDATE SQL statement; use [where] to constrain affected rows.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |
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

### Guide

<!-- guide -->
This slot allows you to update one or more records, in a specified **[table]**. Just like create, it requires
one mandatory argument, being **[values]**, implying columns/values you wish to update. This slot also takes
an optional **[where]** argument, which is described further down in this document. Its simplest version can be
imagined as follows.

```
sql.update
   table:table1
   values
      field1:howdy
```

The above of course will result in the following.

```sql
sql.update:update 'table1' set 'field1' = @v0
   @v0:howdy
```

**Notice**, if you don't apply a **[where]** argument, then *all* records in your table will
be updated - Which is highly unlikely what your intentions are. Hence, make sure you apply a
**[where]** argument as you invoke this slot.
<!-- /guide -->

### Related documentation

* Part of the [magic.data.common](/plugins/magic.data.common/) plugin, which documents every slot it contains.
* Discussed in [The [where] argument](/plugins/magic.data.common/the-where-argument/).

### JSON declaration

This is the complete declaration of `sql.update`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `sql.read`](/reference/slots/sql/sql.read/) | [all `sql.*` slots](/reference/slots/sql/)

