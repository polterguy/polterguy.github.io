---
title: "[sql.create]"
description: "sql.create is a slot in the sql namespace of Magic Cloud. Builds a parameterized INSERT SQL statement."
generated: true
llms: false
slot_json: "/reference/slots/sql/sql.create/slot.json"
---

`sql.create` is a slot in the `sql` namespace, in Hyperlambda, the language of Magic Cloud. Builds a parameterized INSERT SQL statement.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |

Guide: [How to use [sql.create]](/plugins/magic.data.common/#how-to-use-sqlcreate)

### JSON declaration

This is the complete declaration of `sql.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sql.create",
  "description": "Builds a parameterized INSERT SQL statement",
  "signature": {
    "children": {
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
    "output": {
      "mode": "Both",
      "description": "Resolves to the generated SQL string in value and the generated parameter nodes as children"
    }
  }
}
```

</details>

---

[all `sql.*` slots](/reference/slots/sql/) | [`sql.delete` &rarr;](/reference/slots/sql/sql.delete/)

