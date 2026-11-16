---
title: "[sqlite.transaction.create]"
description: "sqlite.transaction.create is a slot in the sqlite namespace of Magic Cloud. Creates a SQLite transaction."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.transaction.create/slot.json"
---

`sqlite.transaction.create` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Creates a SQLite transaction.

* **Scope**: requires `sqlite.connection`; provides `sqlite.transaction` - Requires an open SQLite connection created by [sqlite.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### Guide

[How to use `sqlite.transaction.create`](/plugins/magic.lambda.sqlite/sqlite.transaction.create/)

### JSON declaration

This is the complete declaration of `sqlite.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.transaction.create",
  "description": "Creates a SQLite transaction",
  "signature": {
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
      "provides": "sqlite.transaction",
      "requires": "sqlite.connection",
      "description": "Requires an open SQLite connection created by [sqlite.connect]"
    }
  }
}
```

</details>

---

[&larr; `sqlite.transaction.commit`](/reference/slots/sqlite/sqlite.transaction.commit/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.transaction.rollback` &rarr;](/reference/slots/sqlite/sqlite.transaction.rollback/)

