---
title: "[mysql.scalar]"
description: "mysql.scalar is a slot in the mysql namespace of Magic Cloud. Executes SQL and returns a scalar value from the current MySQL connection."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.scalar/slot.json"
---

`mysql.scalar` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL and returns a scalar value from the current MySQL connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Guide

[How to use `mysql.scalar`](/plugins/magic.lambda.mysql/mysql.scalar/)

### JSON declaration

This is the complete declaration of `mysql.scalar`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.scalar",
  "description": "Executes SQL and returns a scalar value from the current MySQL connection",
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
      "requires": "mysql.connection",
      "description": "Requires an open MySQL connection created by [mysql.connect]"
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

[&larr; `mysql.read`](/reference/slots/mysql/mysql.read/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.select` &rarr;](/reference/slots/mysql/mysql.select/)

