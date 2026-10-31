---
title: "[sqlite.transaction.create]"
description: "sqlite.transaction.create is a slot in the sqlite namespace of Magic Cloud. Creates a SQLite transaction."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.transaction.create/slot.json"
---

`sqlite.transaction.create` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Creates a SQLite transaction.

* **Scope**: requires `sqlite.connection`; provides `sqlite.transaction` - Requires an open SQLite connection created by [sqlite.connect]

### Related documentation

* Part of the [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sqlite.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.transaction.create",
  "description": "Creates a SQLite transaction",
  "signature": {
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

