---
title: "[sqlite.scalar]"
description: "sqlite.scalar is a slot in the sqlite namespace of Magic Cloud. Executes SQL and returns a scalar value from the current SQLite connection."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.scalar/slot.json"
---

`sqlite.scalar` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL and returns a scalar value from the current SQLite connection.

* **Value** (`sql-scalar`), required: SQL statement to execute
* **Returns**: Resolves to the scalar result of the SQL statement
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### JSON declaration

This is the complete declaration of `sqlite.scalar`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.scalar",
  "description": "Executes SQL and returns a scalar value from the current SQLite connection",
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
      "requires": "sqlite.connection",
      "description": "Requires an open SQLite connection created by [sqlite.connect]"
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

[&larr; `sqlite.read`](/reference/slots/sqlite/sqlite.read/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.select` &rarr;](/reference/slots/sqlite/sqlite.select/)

