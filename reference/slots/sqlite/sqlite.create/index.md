---
title: "[sqlite.create]"
description: "sqlite.create is a slot in the sqlite namespace of Magic Cloud. Inserts rows through the current SQLite connection."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.create/slot.json"
---

`sqlite.create` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Inserts rows through the current SQLite connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |
| `[generate]` | bool | no | Whether to only generate SQL and parameter nodes instead of executing it. Default: `false`. |
| `[return-id]` | bool | no | Whether to return the created row ID. Default: `true`. |

### Related documentation

* Part of the [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sqlite.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.create",
  "description": "Inserts rows through the current SQLite connection",
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
      "requires": "sqlite.connection",
      "description": "Requires an open SQLite connection created by [sqlite.connect]"
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

[&larr; `sqlite.connections.flush`](/reference/slots/sqlite/sqlite.connections.flush/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.delete` &rarr;](/reference/slots/sqlite/sqlite.delete/)

