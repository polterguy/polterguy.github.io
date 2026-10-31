---
title: "[mysql.transaction.rollback]"
description: "mysql.transaction.rollback is a slot in the mysql namespace of Magic Cloud. Rolls back the current MySQL transaction."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.transaction.rollback/slot.json"
---

`mysql.transaction.rollback` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Rolls back the current MySQL transaction.

* **Scope**: requires `mysql.transaction` - Requires an active MySQL transaction created by [mysql.transaction.create]

### Related documentation

* Part of the [magic.lambda.mysql](/plugins/magic.lambda.mysql/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mysql.transaction.rollback`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.transaction.rollback",
  "description": "Rolls back the current MySQL transaction",
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

[&larr; `mysql.transaction.create`](/reference/slots/mysql/mysql.transaction.create/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.update` &rarr;](/reference/slots/mysql/mysql.update/)

