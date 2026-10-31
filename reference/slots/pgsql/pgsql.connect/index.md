---
title: "[pgsql.connect]"
description: "pgsql.connect is a slot in the pgsql namespace of Magic Cloud. Opens a PostgreSQL connection."
generated: true
llms: false
slot_json: "/reference/slots/pgsql/pgsql.connect/slot.json"
---

`pgsql.connect` is a slot in the `pgsql` namespace, in Hyperlambda, the language of Magic Cloud. Opens a PostgreSQL connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `pgsql.connection` - Creates an open PostgreSQL connection scope for pgsql.* slots

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### JSON declaration

This is the complete declaration of `pgsql.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pgsql.connect",
  "description": "Opens a PostgreSQL connection",
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
      "provides": "pgsql.connection",
      "description": "Creates an open PostgreSQL connection scope for pgsql.* slots"
    }
  }
}
```

</details>

---

[all `pgsql.*` slots](/reference/slots/pgsql/) | [`pgsql.create` &rarr;](/reference/slots/pgsql/pgsql.create/)

