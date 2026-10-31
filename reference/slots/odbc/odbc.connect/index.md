---
title: "[odbc.connect]"
description: "odbc.connect is a slot in the odbc namespace of Magic Cloud. Opens a ODBC connection."
generated: true
llms: false
slot_json: "/reference/slots/odbc/odbc.connect/slot.json"
---

`odbc.connect` is a slot in the `odbc` namespace, in Hyperlambda, the language of Magic Cloud. Opens a ODBC connection.

* **Value** (`connection-string`), optional: Optional ODBC connection string override; ODBC does not use the database-name shorthand supported by other database providers
* **Scope**: provides `odbc.connection` - Creates an open ODBC connection scope for odbc.* slots

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### Guide

[How to use `odbc.connect`](/plugins/magic.lambda.odbc/odbc.connect/)

### JSON declaration

This is the complete declaration of `odbc.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "odbc.connect",
  "description": "Opens a ODBC connection",
  "signature": {
    "input": {
      "kind": "connection-string",
      "description": "Optional ODBC connection string override; ODBC does not use the database-name shorthand supported by other database providers",
      "required": false,
      "mode": "ValueOrExpression"
    },
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
      "provides": "odbc.connection",
      "description": "Creates an open ODBC connection scope for odbc.* slots"
    }
  }
}
```

</details>

---

[all `odbc.*` slots](/reference/slots/odbc/) | [`odbc.execute` &rarr;](/reference/slots/odbc/odbc.execute/)

