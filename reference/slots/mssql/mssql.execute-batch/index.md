---
title: "[mssql.execute-batch]"
description: "mssql.execute-batch is a slot in the mssql namespace of Magic Cloud. Executes a batch SQL script on the current SQL Server connection."
generated: true
llms: false
slot_json: "/reference/slots/mssql/mssql.execute-batch/slot.json"
---

`mssql.execute-batch` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Executes a batch SQL script on the current SQL Server connection.

* **Value** (`sql-batch`), required: Batch SQL script to execute
* **Returns**: Returns one child node per batch execution result
* **Scope**: requires `mssql.connection` - Requires an open SQL Server connection created by [mssql.connect]

### Guide

[How to use `mssql.execute-batch`](/plugins/magic.lambda.mssql/mssql.execute-batch/)

### JSON declaration

This is the complete declaration of `mssql.execute-batch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mssql.execute-batch",
  "description": "Executes a batch SQL script on the current SQL Server connection",
  "signature": {
    "input": {
      "kind": "sql-batch",
      "description": "Batch SQL script to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "scope": {
      "requires": "mssql.connection",
      "description": "Requires an open SQL Server connection created by [mssql.connect]"
    },
    "output": {
      "mode": "Lambda",
      "kind": "sql-batch-result-list,node-list",
      "element-kind": "row",
      "description": "Returns one child node per batch execution result"
    }
  }
}
```

</details>

---

[&larr; `mssql.execute`](/reference/slots/mssql/mssql.execute/) | [all `mssql.*` slots](/reference/slots/mssql/) | [`mssql.read` &rarr;](/reference/slots/mssql/mssql.read/)

