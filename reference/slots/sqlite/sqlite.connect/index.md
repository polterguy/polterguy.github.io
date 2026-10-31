---
title: "[sqlite.connect]"
description: "sqlite.connect is a slot in the sqlite namespace of Magic Cloud. Opens a SQLite connection."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.connect/slot.json"
---

`sqlite.connect` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Opens a SQLite connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `sqlite.connection` - Creates an open SQLite connection scope for sqlite.* slots

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### Guide

[How to use `sqlite.connect`](/plugins/magic.lambda.sqlite/sqlite.connect/)

### JSON declaration

This is the complete declaration of `sqlite.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.connect",
  "description": "Opens a SQLite connection",
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
      "provides": "sqlite.connection",
      "description": "Creates an open SQLite connection scope for sqlite.* slots"
    }
  }
}
```

</details>

---

[&larr; `sqlite.backup`](/reference/slots/sqlite/sqlite.backup/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.connections.flush` &rarr;](/reference/slots/sqlite/sqlite.connections.flush/)

