---
title: "[odbc.execute]"
description: "odbc.execute is a slot in the odbc namespace of Magic Cloud. Executes SQL on the current ODBC connection."
generated: true
llms: false
slot_json: "/reference/slots/odbc/odbc.execute/slot.json"
---

`odbc.execute` is a slot in the `odbc` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL on the current ODBC connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `odbc.connection` - Requires an open ODBC connection created by [odbc.connect]

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### JSON declaration

This is the complete declaration of `odbc.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "odbc.execute",
  "description": "Executes SQL on the current ODBC connection",
  "signature": {
    "input": {
      "kind": "sql-execute",
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
      "kind": "integer,number",
      "description": "Resolves to the number of rows affected by the SQL statement"
    }
  }
}
```

</details>

---

[&larr; `odbc.connect`](/reference/slots/odbc/odbc.connect/) | [all `odbc.*` slots](/reference/slots/odbc/) | [`odbc.scalar` &rarr;](/reference/slots/odbc/odbc.scalar/)

