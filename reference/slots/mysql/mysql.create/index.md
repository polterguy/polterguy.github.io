---
title: "[mysql.create]"
description: "mysql.create is a slot in the mysql namespace of Magic Cloud. Inserts rows through the current MySQL connection."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.create/slot.json"
---

`mysql.create` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Inserts rows through the current MySQL connection.

* **Returns**: Resolves to the created row ID when [return-id] is true, otherwise null
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

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

* Part of the [magic.lambda.mysql](/plugins/magic.lambda.mysql/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mysql.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.create",
  "description": "Inserts rows through the current MySQL connection",
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
      "requires": "mysql.connection",
      "description": "Requires an open MySQL connection created by [mysql.connect]"
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

[&larr; `mysql.connect`](/reference/slots/mysql/mysql.connect/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.delete` &rarr;](/reference/slots/mysql/mysql.delete/)

