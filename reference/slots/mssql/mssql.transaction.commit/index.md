---
title: "[mssql.transaction.commit]"
description: "mssql.transaction.commit is a slot in the mssql namespace of Magic Cloud. Commits the current SQL Server transaction."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.transaction.commit/slot.json"
---

`mssql.transaction.commit` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Commits the current SQL Server transaction.

* **Scope**: requires `mssql.transaction` - Requires an active SQL Server transaction created by [mssql.transaction.create]

### Guide

[How to use `mssql.transaction.commit`](/plugins/magic.lambda.mssql/mssql.transaction.commit/)

### JSON declaration

This is the complete declaration of `mssql.transaction.commit`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.transaction.commit",
  "description": "Commits the current SQL Server transaction",
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

[&larr; `mssql.select`](/reference/slots/mssql/mssql.select/) | [all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.transaction.create` &rarr;](/reference/slots/mssql/mssql.transaction.create/)

