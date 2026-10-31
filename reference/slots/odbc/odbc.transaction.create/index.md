---
title: "[odbc.transaction.create]"
description: "odbc.transaction.create is a slot in the odbc namespace of Magic Cloud. Creates a ODBC transaction."
generated: true
llms: false
slot_json: "/reference/slots/odbc/odbc.transaction.create/slot.json"
---

`odbc.transaction.create` is a slot in the `odbc` namespace, in Hyperlambda, the language of Magic Cloud. Creates a ODBC transaction.

* **Scope**: requires `odbc.connection`; provides `odbc.transaction` - Requires an open ODBC connection created by [odbc.connect]

### JSON declaration

This is the complete declaration of `odbc.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "odbc.transaction.create",
  "description": "Creates a ODBC transaction",
  "signature": {
    "scope": {
      "provides": "odbc.transaction",
      "requires": "odbc.connection",
      "description": "Requires an open ODBC connection created by [odbc.connect]"
    }
  }
}
```

</details>

---

[&larr; `odbc.transaction.commit`](/reference/slots/odbc/odbc.transaction.commit/) | [all `odbc.*` slots](/reference/slots/odbc/) | [`odbc.transaction.rollback` &rarr;](/reference/slots/odbc/odbc.transaction.rollback/)

