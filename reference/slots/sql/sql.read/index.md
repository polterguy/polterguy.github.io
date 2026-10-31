---
title: "[sql.read]"
description: "sql.read is a slot in the sql namespace of Magic Cloud. Builds a parameterized SELECT SQL statement."
generated: true
llms: "guide"
slot_json: "/reference/slots/sql/sql.read/slot.json"
---

`sql.read` is a slot in the `sql` namespace, in Hyperlambda, the language of Magic Cloud. Builds a parameterized SELECT SQL statement.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

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
| `[limit]` | long | no | Maximum number of rows to return; omitted defaults to 25 and -1 suppresses the generated limit clause. Default: `25`. |
| `[offset]` | long | no | Number of rows to skip. Default: `0`. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

### Guide

<!-- guide -->
This slot requires only one mandatory argument, being your table name. The slot creates a select
SQL statement for you. An example can be found below.

```
sql.read
   table:foo
```

The above will result in the following SQL returned to you. If you're using the special implementations,
such as e.g. **[\[data.read\]](/reference/slots/data/data.read/)**, and/or **[\[mssql.read\]](/reference/slots/mssql/mssql.read/)** - The returned SQL might vary according to your dialect.
But the results of executing the SQL will be the same.

```
select * from 'foo' limit 25
```

To avoid accidentally exhausting your database, this slot will by default limit your result set
to 25 records unless explicitly overridden by your code with a **[limit]** argument. You can optionally
supply the following arguments to this slot.

* __[columns]__ - Columns to select
* __[order]__ - Which column(s) to order the results by. You can supply multiple **[order]** arguments
* __[direction]__ - Which direction to order your columns
* __[limit]__ - How many records to return, default is 25. Set this value to -1 to avoid having the parser inject its default value
* __[offset]__ - Offset of where to start returning records
* __[where]__ - Where condition
* __[\[join\]](/reference/slots/core/join/)__ - Join condition
* __[group]__ - Group by declaration

For instance, to select only the _"field1"_ column and the _"field2"_ column from _"table1"_,
and ordering descendingly by _"field3"_ - You can use something resembling the following.

```
sql.read
   table:table1
   columns
      field1
      field2
   order:field3
   direction:desc
```

This will result in the following SQL returned.

```
select 'field1','field2' from 'table1' order by 'field3' desc limit 25
```

The **[direction]** argument can _only_ be either _"asc"_ or _"desc"_, implying ascending or descending.
You can also supply multiple ordering columns, by separating them by _","_. See an example below, which also specifies
what table to use while ordering your results.

```
sql.read
   table:table1
   order:table1.field1, table1.field2
```

The above will result in the following SQL.

```sql
select * from 'table1' order by 'table1'.'field1' asc,'table1'.'field2' asc limit 25
```

And finally you can provide the **[direction]** argument on separate **[order]** arguments, such as the
following illustrates.

```
sql.read
   table:table1

   order:field1
      direction:asc

   order:field2
      direction:desc
```

If you do, the ordering is sequentially applied.
<!-- /guide -->

### Related documentation

* Part of the [magic.data.common](/plugins/magic.data.common/) plugin, which documents every slot it contains.
* Discussed in ['Namespacing' columns](/plugins/magic.data.common/namespacing-columns/).
* Discussed in [Aggregate results](/plugins/magic.data.common/aggregate-results/).
* Discussed in [Comparison operators](/plugins/magic.data.common/comparison-operators/).
* Discussed in [Differences between [join] and [where]](/plugins/magic.data.common/differences-between-join-and-where/).
* Discussed in [Joins](/plugins/magic.data.common/joins/).
* Discussed in [The [where] argument](/plugins/magic.data.common/the-where-argument/).

### JSON declaration

This is the complete declaration of `sql.read`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `sql.delete`](/reference/slots/sql/sql.delete/) | [all `sql.*` slots](/reference/slots/sql/) | [`sql.update` &rarr;](/reference/slots/sql/sql.update/)

