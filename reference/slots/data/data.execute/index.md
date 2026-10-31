---
title: "[data.execute]"
description: "data.execute is a slot in the data namespace of Magic Cloud. Executes SQL against the current database connection."
generated: true
llms: "guide"
slot_json: "/reference/slots/data/data.execute/slot.json"
---

`data.execute` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL against the current database connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Guide

<!-- guide -->
This slot should be used if you don't expect any type of result at all, such as in for instance
delete or update invocations, where you don't care about the result of the operation. You can
find an example below.

```
data.connect:sakila

   // Notice, will throw! (hopefully!)
   data.execute:delete from non_existing_table
```

Yet again, prefer **[data.delete]** if you can.
<!-- /guide -->

### Related documentation

* Part of the [magic.data.common](/plugins/magic.data.common/) plugin, which documents every slot it contains.
* Discussed in [How to use [data.*]](/plugins/magic.data.common/how-to-use-data/).

### JSON declaration

This is the complete declaration of `data.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.execute",
  "description": "Executes SQL against the current database connection",
  "signature": {
    "input": {
      "kind": "sql-execute",
      "description": "SQL statement to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "database-type": {
        "type": "string",
        "kind": "database-type",
        "description": "Database adapter to use instead of the configured default",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne"
      },
      "*": {
        "type": "object",
        "kind": "sql-parameter-value,text,number,boolean,date,guid,content,value",
        "description": "SQL parameter value; child name is used as the parameter name referenced by the SQL statement",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "Value"
      }
    },
    "scope": {
      "requires": "data.connection",
      "description": "Requires an open database connection created by [data.connect]"
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of rows affected by the SQL statement"
    }
  }
}
```

</details>

---

[&larr; `data.delete`](/reference/slots/data/data.delete/) | [all `data.*` slots](/reference/slots/data/) | [`data.read` &rarr;](/reference/slots/data/data.read/)

