---
title: "[mssql.connect]"
description: "mssql.connect is a slot in the mssql namespace of Magic Cloud. Opens a SQL Server connection."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.connect/slot.json"
---

`mssql.connect` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Opens a SQL Server connection.

* **Value** (`database-name,connection-string`), optional: Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override
* **Scope**: provides `mssql.connection` - Creates an open SQL Server connection scope for mssql.* slots

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the database connection is open. Can be repeated. |

### JSON declaration

This is the complete declaration of `mssql.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.connect",
  "description": "Opens a SQL Server connection",
  "signature": {
    "input": {
      "kind": "database-name,connection-string",
      "description": "Optional DATABASE_NAME or [CONNECTION_STRING|DATABASE_NAME] override",
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
      "provides": "mssql.connection",
      "description": "Creates an open SQL Server connection scope for mssql.* slots"
    }
  }
}
```

</details>

---

[all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.create` &rarr;](/reference/slots/mssql/mssql.create/)

