---
title: "[data.create]"
description: "data.create is a slot in the data namespace of Magic Cloud. Inserts a new row into the current open database connection."
generated: true
llms: false
slot_json: "/reference/slots/data/data.create/slot.json"
---

`data.create` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Inserts a new row into the current open database connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[return-id]` | bool | no | Whether to return the created row ID. Default: `true`. |

### Guide

[How to use `data.create`](/plugins/magic.data.common/data.create/)

### JSON declaration

This is the complete declaration of `data.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.create",
  "description": "Inserts a new row into the current open database connection",
  "signature": {
    "children": {
      "database-type": {
        "type": "string",
        "kind": "database-type",
        "description": "Database adapter to use instead of the configured default",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne"
      },
      "generate": {
        "type": "bool",
        "description": "Whether to only generate SQL and parameter nodes instead of executing it",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false"
      },
      "return-id": {
        "type": "bool",
        "description": "Whether to return the created row ID",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true"
      },
      "table": {
        "type": "string",
        "kind": "table-name",
        "description": "Table name to use in the SQL statement",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne"
      },
      "values": {
        "type": "lambda",
        "description": "Column values to insert or update",
        "required": true,
        "mode": "DynamicNamedValues",
        "cardinality": "ExactlyOne",
        "children": {
          "*": {
            "type": "object",
            "kind": "sql-column-value,text,number,boolean,date,guid,content,value",
            "description": "Column name and value",
            "required": true,
            "mode": "ValueOrExpression",
            "cardinality": "OneOrMore"
          }
        }
      }
    },
    "scope": {
      "requires": "data.connection",
      "description": "Requires an open database connection created by [data.connect]"
    },
    "output": {
      "mode": "Value",
      "description": "Resolves to the created row ID when [return-id] is true, otherwise null"
    }
  }
}
```

</details>

---

[&larr; `data.connect`](/reference/slots/data/data.connect/) | [all `data.*` slots](/reference/slots/data/) | [`data.delete` &rarr;](/reference/slots/data/data.delete/)

