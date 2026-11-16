---
title: "[mssql.transaction.create]"
description: "mssql.transaction.create is a slot in the mssql namespace of Magic Cloud. Creates a SQL Server transaction."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.transaction.create/slot.json"
---

`mssql.transaction.create` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Creates a SQL Server transaction.

* **Scope**: requires `mssql.connection`; provides `mssql.transaction` - Requires an open SQL Server connection created by [mssql.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### Guide

[How to use `mssql.transaction.create`](/plugins/magic.lambda.mssql/mssql.transaction.create/)

### JSON declaration

This is the complete declaration of `mssql.transaction.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.transaction.create",
  "description": "Creates a SQL Server transaction",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot evaluated while the database connection is open",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
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

