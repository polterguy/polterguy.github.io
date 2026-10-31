---
title: "[pgsql.execute]"
description: "pgsql.execute is a slot in the pgsql namespace of Magic Cloud. Executes SQL on the current PostgreSQL connection."
generated: true
llms: false
slot_json: "/reference/slots/pgsql/pgsql.execute/slot.json"
---

`pgsql.execute` is a slot in the `pgsql` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL on the current PostgreSQL connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `pgsql.connection` - Requires an open PostgreSQL connection created by [pgsql.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### JSON declaration

This is the complete declaration of `pgsql.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pgsql.execute",
  "description": "Executes SQL on the current PostgreSQL connection",
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
      "requires": "pgsql.connection",
      "description": "Requires an open PostgreSQL connection created by [pgsql.connect]"
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

[&larr; `pgsql.delete`](/reference/slots/pgsql/pgsql.delete/) | [all `pgsql.*` slots](/reference/slots/pgsql/) | [`pgsql.read` &rarr;](/reference/slots/pgsql/pgsql.read/)

