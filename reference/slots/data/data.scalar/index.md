---
title: "[data.scalar]"
description: "data.scalar is a slot in the data namespace of Magic Cloud. Executes SQL and returns a scalar value from the current database connection."
generated: true
llms: "guide"
slot_json: "/reference/slots/data/data.scalar/slot.json"
---

`data.scalar` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL and returns a scalar value from the current database connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to a scalar value from the current database connection
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Guide

<!-- guide -->
This slot is similar to the **[\[data.select\]](/reference/slots/data/data.select/)** slot, but will only return one value as the
value of its node after execution. This slot is typically used for aggregate results. You can see
an example below.

```
data.connect:sakila
   data.scalar:select count(*) from actor
```

After execution, your result will resemble the following.

```
data.connect
   data.scalar:long:200
```

Yet again you should prefer the **[data.\*]** slots if you can.
<!-- /guide -->

### Related documentation

* Part of the [magic.data.common](/plugins/magic.data.common/) plugin, which documents every slot it contains.
* Discussed in [How to use [data.*]](/plugins/magic.data.common/how-to-use-data/).

### JSON declaration

This is the complete declaration of `data.scalar`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.scalar",
  "description": "Executes SQL and returns a scalar value from the current database connection",
  "signature": {
    "input": {
      "kind": "sql-scalar",
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
      "description": "Resolves to a scalar value from the current database connection"
    }
  }
}
```

</details>

---

[&larr; `data.read`](/reference/slots/data/data.read/) | [all `data.*` slots](/reference/slots/data/) | [`data.scan` &rarr;](/reference/slots/data/data.scan/)

