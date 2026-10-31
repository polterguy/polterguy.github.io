---
title: "[odbc.scalar]"
description: "odbc.scalar is a slot in the odbc namespace of Magic Cloud. Executes SQL and returns a scalar value from the current ODBC connection."
generated: true
llms: false
slot_json: "/reference/slots/odbc/odbc.scalar/slot.json"
---

`odbc.scalar` is a slot in the `odbc` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL and returns a scalar value from the current ODBC connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `odbc.connection` - Requires an open ODBC connection created by [odbc.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Guide

[How to use `odbc.scalar`](/plugins/magic.lambda.odbc/odbc.scalar/)

### JSON declaration

This is the complete declaration of `odbc.scalar`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "odbc.scalar",
  "description": "Executes SQL and returns a scalar value from the current ODBC connection",
  "signature": {
    "input": {
      "kind": "sql-scalar",
      "description": "SQL statement to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "sql-parameter-value,text,number,boolean,date,guid,content,value",
        "description": "SQL parameter value; child name is used as the parameter name referenced by the SQL statement",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "Value"
      }
    },
    "scope": {
      "requires": "odbc.connection",
      "description": "Requires an open ODBC connection created by [odbc.connect]"
    },
    "output": {
      "mode": "Value",
      "description": "Resolves to the scalar result of the SQL statement"
    }
  }
}
```

</details>

---

[&larr; `odbc.execute`](/reference/slots/odbc/odbc.execute/) | [all `odbc.*` slots](/reference/slots/odbc/) | [`odbc.select` &rarr;](/reference/slots/odbc/odbc.select/)

