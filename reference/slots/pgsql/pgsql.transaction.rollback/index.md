---
title: "[pgsql.transaction.rollback]"
description: "pgsql.transaction.rollback is a slot in the pgsql namespace of Magic Cloud. Rolls back the current PostgreSQL transaction."
generated: true
llms: false
slot_json: "/reference/slots/pgsql/pgsql.transaction.rollback/slot.json"
---

`pgsql.transaction.rollback` is a slot in the `pgsql` namespace, in Hyperlambda, the language of Magic Cloud. Rolls back the current PostgreSQL transaction.

* **Scope**: requires `pgsql.transaction` - Requires an active PostgreSQL transaction created by [pgsql.transaction.create]

### JSON declaration

This is the complete declaration of `pgsql.transaction.rollback`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pgsql.transaction.rollback",
  "description": "Rolls back the current PostgreSQL transaction",
  "signature": {
    "scope": {
      "requires": "pgsql.transaction",
      "description": "Requires an active PostgreSQL transaction created by [pgsql.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `pgsql.transaction.create`](/reference/slots/pgsql/pgsql.transaction.create/) | [all `pgsql.*` slots](/reference/slots/pgsql/) | [`pgsql.update` &rarr;](/reference/slots/pgsql/pgsql.update/)

