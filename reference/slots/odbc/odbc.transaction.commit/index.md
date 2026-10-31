---
title: "[odbc.transaction.commit]"
description: "odbc.transaction.commit is a slot in the odbc namespace of Magic Cloud. Commits the current ODBC transaction."
generated: true
llms: false
slot_json: "/reference/slots/odbc/odbc.transaction.commit/slot.json"
---

`odbc.transaction.commit` is a slot in the `odbc` namespace, in Hyperlambda, the language of Magic Cloud. Commits the current ODBC transaction.

* **Scope**: requires `odbc.transaction` - Requires an active ODBC transaction created by [odbc.transaction.create]

### JSON declaration

This is the complete declaration of `odbc.transaction.commit`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "odbc.transaction.commit",
  "description": "Commits the current ODBC transaction",
  "signature": {
    "scope": {
      "requires": "odbc.transaction",
      "description": "Requires an active ODBC transaction created by [odbc.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `odbc.select`](/reference/slots/odbc/odbc.select/) | [all `odbc.*` slots](/reference/slots/odbc/) | [`odbc.transaction.create` &rarr;](/reference/slots/odbc/odbc.transaction.create/)

