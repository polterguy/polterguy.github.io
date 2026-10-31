---
title: "[mysql.execute]"
description: "mysql.execute is a slot in the mysql namespace of Magic Cloud. Executes SQL on the current MySQL connection."
generated: true
llms: false
slot_json: "/reference/slots/mysql/mysql.execute/slot.json"
---

`mysql.execute` is a slot in the `mysql` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL on the current MySQL connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `mysql.connection` - Requires an open MySQL connection created by [mysql.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### JSON declaration

This is the complete declaration of `mysql.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mysql.execute",
  "description": "Executes SQL on the current MySQL connection",
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
      "requires": "mysql.connection",
      "description": "Requires an open MySQL connection created by [mysql.connect]"
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

[&larr; `mysql.delete`](/reference/slots/mysql/mysql.delete/) | [all `mysql.*` slots](/reference/slots/mysql/) | [`mysql.read` &rarr;](/reference/slots/mysql/mysql.read/)

