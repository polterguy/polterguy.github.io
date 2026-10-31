---
title: "[mysql.transaction.commit]"
description: "mysql.transaction.commit is a slot in the mysql namespace of Magic Cloud. Commits the current MySQL transaction."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.transaction.commit/slot.json"
---

`mysql.transaction.commit` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Commits the current MySQL transaction.

* **Scope**: requires `mysql.transaction` - Requires an active MySQL transaction created by [mysql.transaction.create]

### JSON declaration

This is the complete declaration of `mysql.transaction.commit`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.transaction.commit",
  "description": "Commits the current MySQL transaction",
  "signature": {
    "scope": {
      "requires": "mysql.transaction",
      "description": "Requires an active MySQL transaction created by [mysql.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `mysql.select`](/reference/slots/mysql/mysql.select/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.transaction.create` &rarr;](/reference/slots/mysql/mysql.transaction.create/)

