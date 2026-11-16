---
title: "[pgsql.transaction.create]"
description: "pgsql.transaction.create is a slot in the pgsql namespace of Magic Cloud. Creates a PostgreSQL transaction."
generated: true
llms: false
slot_json: "/reference/slots/pgsql/pgsql.transaction.create/slot.json"
---

`pgsql.transaction.create` is a slot in the `pgsql` namespace, in Hyperlambda, the language of Magic Cloud. Creates a PostgreSQL transaction.

* **Scope**: requires `pgsql.connection`; provides `pgsql.transaction` - Requires an open PostgreSQL connection created by [pgsql.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### Guide

[How to use `pgsql.transaction.create`](/plugins/magic.lambda.pgsql/pgsql.transaction.create/)

### JSON declaration

This is the complete declaration of `pgsql.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pgsql.transaction.create",
  "description": "Creates a PostgreSQL transaction",
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
      "provides": "pgsql.transaction",
      "requires": "pgsql.connection",
      "description": "Requires an open PostgreSQL connection created by [pgsql.connect]"
    }
  }
}
```

</details>

---

[&larr; `pgsql.transaction.commit`](/reference/slots/pgsql/pgsql.transaction.commit/) | [all `pgsql.*` slots](/reference/slots/pgsql/) | [`pgsql.transaction.rollback` &rarr;](/reference/slots/pgsql/pgsql.transaction.rollback/)

