---
title: "[data.connect]"
description: "data.connect is a slot in the data namespace of Magic Cloud. Opens a database connection using the configured provider."
generated: true
llms: false
slot_json: "/reference/slots/data/data.connect/slot.json"
---

`data.connect` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Opens a database connection using the configured provider.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `data.connection` - Creates an open database connection scope for data.* slots

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### Guide

[How to use `data.connect`](/plugins/magic.data.common/data.connect/)

### JSON declaration

This is the complete declaration of `data.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.connect",
  "description": "Opens a database connection using the configured provider",
  "signature": {
    "input": {
      "kind": "database-name,connection-string",
      "description": "Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "database-type": {
        "type": "string",
        "kind": "database-type",
        "description": "Database adapter to use instead of the configured default",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
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
      "provides": "data.connection",
      "description": "Creates an open database connection scope for data.* slots"
    }
  }
}
```

</details>

---

[all `data.*` slots](/reference/slots/data/) | [`data.create` &rarr;](/reference/slots/data/data.create/)

