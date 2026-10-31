---
title: "[mysql.connect]"
description: "mysql.connect is a slot in the mysql namespace of Magic Cloud. Opens a MySQL connection."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.connect/slot.json"
---

`mysql.connect` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Opens a MySQL connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `mysql.connection` - Creates an open MySQL connection scope for mysql.* slots

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### JSON declaration

This is the complete declaration of `mysql.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.connect",
  "description": "Opens a MySQL connection",
  "signature": {
    "input": {
      "kind": "database-name,connection-string",
      "description": "Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot evaluated while the database connection is open",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "mysql.connection",
      "description": "Creates an open MySQL connection scope for mysql.* slots"
    }
  }
}
```

</details>

---

[all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.create` &rarr;](/reference/slots/mysql/mysql.create/)

