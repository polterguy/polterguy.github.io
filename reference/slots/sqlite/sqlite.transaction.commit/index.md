---
title: "[sqlite.transaction.commit]"
description: "sqlite.transaction.commit is a slot in the sqlite namespace of Magic Cloud. Commits the current SQLite transaction."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.transaction.commit/slot.json"
---

`sqlite.transaction.commit` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Commits the current SQLite transaction.

* **Scope**: requires `sqlite.transaction` - Requires an active SQLite transaction created by [sqlite.transaction.create]

### Related documentation

* Part of the [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sqlite.transaction.commit`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.transaction.commit",
  "description": "Commits the current SQLite transaction",
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

[&larr; `sqlite.select`](/reference/slots/sqlite/sqlite.select/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.transaction.create` &rarr;](/reference/slots/sqlite/sqlite.transaction.create/)

