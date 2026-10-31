---
title: "[mssql.execute]"
description: "mssql.execute is a slot in the mssql namespace of Magic Cloud. Executes SQL on the current SQL Server connection."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.execute/slot.json"
---

`mssql.execute` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Executes SQL on the current SQL Server connection.

* **Value** (`sql-execute`), required: SQL statement to execute
* **Returns**: Resolves to the number of rows affected by the SQL statement
* **Scope**: requires `mssql.connection` - Requires an open SQL Server connection created by [mssql.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Related documentation

* Part of the [magic.lambda.mssql](/plugins/magic.lambda.mssql/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mssql.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.execute",
  "description": "Executes SQL on the current SQL Server connection",
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
      "requires": "mssql.connection",
      "description": "Requires an open SQL Server connection created by [mssql.connect]"
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

[&larr; `mssql.delete`](/reference/slots/mssql/mssql.delete/) | [all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.execute-batch` &rarr;](/reference/slots/mssql/mssql.execute-batch/)

