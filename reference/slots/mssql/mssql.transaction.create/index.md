---
title: "[mssql.transaction.create]"
description: "mssql.transaction.create is a slot in the mssql namespace of Magic Cloud. Creates a SQL Server transaction."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.transaction.create/slot.json"
---

`mssql.transaction.create` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Creates a SQL Server transaction.

* **Scope**: requires `mssql.connection`; provides `mssql.transaction` - Requires an open SQL Server connection created by [mssql.connect]

### Related documentation

* Part of the [magic.lambda.mssql](/plugins/magic.lambda.mssql/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mssql.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.transaction.create",
  "description": "Creates a SQL Server transaction",
  "signature": {
    "scope": {
      "provides": "mssql.transaction",
      "requires": "mssql.connection",
      "description": "Requires an open SQL Server connection created by [mssql.connect]"
    }
  }
}
```

</details>

---

[&larr; `mssql.transaction.commit`](/reference/slots/mssql/mssql.transaction.commit/) | [all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.transaction.rollback` &rarr;](/reference/slots/mssql/mssql.transaction.rollback/)

