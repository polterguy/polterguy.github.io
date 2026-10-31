---
title: "[pgsql.scalar]"
description: "pgsql.scalar is a slot in the pgsql namespace of Magic Cloud. Executes SQL and returns a scalar value from the current PostgreSQL connection."
generated: true
llms: false
slot_json: "/reference/slots/pgsql/pgsql.scalar/slot.json"
---

`pgsql.scalar` is a slot in the `pgsql` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL and returns a scalar value from the current PostgreSQL connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `pgsql.connection` - Requires an open PostgreSQL connection created by [pgsql.connect]

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### JSON declaration

This is the complete declaration of `pgsql.scalar`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pgsql.scalar",
  "description": "Executes SQL and returns a scalar value from the current PostgreSQL connection",
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
      "requires": "pgsql.connection",
      "description": "Requires an open PostgreSQL connection created by [pgsql.connect]"
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

[&larr; `pgsql.read`](/reference/slots/pgsql/pgsql.read/) | [all `pgsql.*` slots](/reference/slots/pgsql/) | [`pgsql.select` &rarr;](/reference/slots/pgsql/pgsql.select/)

