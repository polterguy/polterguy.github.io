---
title: "[mysql.transaction.create]"
description: "mysql.transaction.create is a slot in the mysql namespace of Magic Cloud. Creates a MySQL transaction."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.transaction.create/slot.json"
---

`mysql.transaction.create` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Creates a MySQL transaction.

* **Scope**: requires `mysql.connection`; provides `mysql.transaction` - Requires an open MySQL connection created by [mysql.connect]

### Related documentation

* Part of the [magic.lambda.mysql](/plugins/magic.lambda.mysql/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mysql.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.transaction.create",
  "description": "Creates a MySQL transaction",
  "signature": {
    "scope": {
      "provides": "mysql.transaction",
      "requires": "mysql.connection",
      "description": "Requires an open MySQL connection created by [mysql.connect]"
    }
  }
}
```

</details>

---

[&larr; `mysql.transaction.commit`](/reference/slots/mysql/mysql.transaction.commit/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.transaction.rollback` &rarr;](/reference/slots/mysql/mysql.transaction.rollback/)

