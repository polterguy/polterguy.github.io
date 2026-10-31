---
title: "[odbc.transaction.rollback]"
description: "odbc.transaction.rollback is a slot in the odbc namespace of Magic Cloud. Rolls back the current ODBC transaction."
generated: true
llms: false
slot_json: "/reference/slots/odbc/odbc.transaction.rollback/slot.json"
---

`odbc.transaction.rollback` is a slot in the `odbc` namespace, in Hyperlambda, the language of Magic Cloud. Rolls back the current ODBC transaction.

* **Scope**: requires `odbc.transaction` - Requires an active ODBC transaction created by [odbc.transaction.create]

### Guide

[How to use `odbc.transaction.rollback`](/plugins/magic.lambda.odbc/odbc.transaction.rollback/)

### JSON declaration

This is the complete declaration of `odbc.transaction.rollback`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "odbc.transaction.rollback",
  "description": "Rolls back the current ODBC transaction",
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

[&larr; `odbc.transaction.create`](/reference/slots/odbc/odbc.transaction.create/) | [all `odbc.*` slots](/reference/slots/odbc/)

