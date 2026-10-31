---
title: "[sqlite.transaction.rollback]"
description: "sqlite.transaction.rollback is a slot in the sqlite namespace of Magic Cloud. Rolls back the current SQLite transaction."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.transaction.rollback/slot.json"
---

`sqlite.transaction.rollback` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Rolls back the current SQLite transaction.

* **Scope**: requires `sqlite.transaction` - Requires an active SQLite transaction created by [sqlite.transaction.create]

### Related documentation

* Part of the [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sqlite.transaction.rollback`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.transaction.rollback",
  "description": "Rolls back the current SQLite transaction",
  "signature": {
    "scope": {
      "requires": "sqlite.transaction",
      "description": "Requires an active SQLite transaction created by [sqlite.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `sqlite.transaction.create`](/reference/slots/sqlite/sqlite.transaction.create/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.update` &rarr;](/reference/slots/sqlite/sqlite.update/)

