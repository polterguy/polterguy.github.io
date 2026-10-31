---
title: "[data.transaction.create]"
description: "data.transaction.create is a slot in the data namespace of Magic Cloud. Creates a database transaction using the configured provider."
generated: true
llms: false
slot_json: "/reference/slots/data/data.transaction.create/slot.json"
---

`data.transaction.create` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Creates a database transaction using the configured provider.

* **Scope**: requires `data.connection`; provides `data.transaction` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |

### JSON declaration

This is the complete declaration of `data.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.transaction.create",
  "description": "Creates a database transaction using the configured provider",
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
      "provides": "data.transaction",
      "requires": "data.connection",
      "description": "Requires an open database connection created by [data.connect]"
    }
  }
}
```

</details>

---

[&larr; `data.transaction.commit`](/reference/slots/data/data.transaction.commit/) | [all `data.*` slots](/reference/slots/data/) | [`data.transaction.rollback` &rarr;](/reference/slots/data/data.transaction.rollback/)

