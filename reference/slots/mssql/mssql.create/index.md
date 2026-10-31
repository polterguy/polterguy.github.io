---
title: "[mssql.create]"
description: "mssql.create is a slot in the mssql namespace of Magic Cloud. Inserts rows through the current SQL Server connection."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.create/slot.json"
---

`mssql.create` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Inserts rows through the current SQL Server connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `mssql.connection` - Requires an open SQL Server connection created by [mssql.connect]

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[return-id]` | bool | no | Whether to return the created row ID. Default: `true`. |
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |

### JSON declaration

This is the complete declaration of `mssql.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.create",
  "description": "Inserts rows through the current SQL Server connection",
  "signature": {
    "children": {
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
      "requires": "mssql.connection",
      "description": "Requires an open SQL Server connection created by [mssql.connect]"
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

[&larr; `mssql.connect`](/reference/slots/mssql/mssql.connect/) | [all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.delete` &rarr;](/reference/slots/mssql/mssql.delete/)

