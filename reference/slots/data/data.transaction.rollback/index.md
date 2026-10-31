---
title: "[data.transaction.rollback]"
description: "data.transaction.rollback is a slot in the data namespace of Magic Cloud. Rolls back the current database transaction using the configured provider."
generated: true
llms: false
slot_json: "/reference/slots/data/data.transaction.rollback/slot.json"
---

`data.transaction.rollback` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Rolls back the current database transaction using the configured provider.

* **Scope**: requires `data.transaction` - Requires an active database transaction created by [data.transaction.create]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |

### JSON declaration

This is the complete declaration of `data.transaction.rollback`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.transaction.rollback",
  "description": "Rolls back the current database transaction using the configured provider",
  "signature": {
    "children": {
      "database-type": {
        "type": "string",
        "kind": "database-type",
        "description": "Database adapter to use instead of the configured default",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne"
      }
    },
    "scope": {
      "requires": "data.transaction",
      "description": "Requires an active database transaction created by [data.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `data.transaction.create`](/reference/slots/data/data.transaction.create/) | [all `data.*` slots](/reference/slots/data/) | [`data.update` &rarr;](/reference/slots/data/data.update/)

