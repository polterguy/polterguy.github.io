---
title: "[sqlite.execute]"
description: "sqlite.execute is a slot in the sqlite namespace of Magic Cloud. Executes SQL on the current SQLite connection."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.execute/slot.json"
---

`sqlite.execute` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL on the current SQLite connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Related documentation

* Part of the [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sqlite.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.execute",
  "description": "Executes SQL on the current SQLite connection",
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
      "requires": "sqlite.connection",
      "description": "Requires an open SQLite connection created by [sqlite.connect]"
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

[&larr; `sqlite.delete`](/reference/slots/sqlite/sqlite.delete/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.load-extension` &rarr;](/reference/slots/sqlite/sqlite.load-extension/)

