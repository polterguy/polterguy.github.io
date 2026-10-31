---
title: "[mssql.transaction.rollback]"
description: "mssql.transaction.rollback is a slot in the mssql namespace of Magic Cloud. Rolls back the current SQL Server transaction."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.transaction.rollback/slot.json"
---

`mssql.transaction.rollback` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Rolls back the current SQL Server transaction.

* **Scope**: requires `mssql.transaction` - Requires an active SQL Server transaction created by [mssql.transaction.create]

### Related documentation

* Part of the [magic.lambda.mssql](/plugins/magic.lambda.mssql/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mssql.transaction.rollback`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.transaction.rollback",
  "description": "Rolls back the current SQL Server transaction",
  "signature": {
    "scope": {
      "requires": "mssql.transaction",
      "description": "Requires an active SQL Server transaction created by [mssql.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `mssql.transaction.create`](/reference/slots/mssql/mssql.transaction.create/) | [all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.update` &rarr;](/reference/slots/mssql/mssql.update/)

