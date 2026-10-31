---
title: "[mssql.execute-batch]"
description: "mssql.execute-batch is a slot in the mssql namespace of Magic Cloud. Executes a batch SQL script on the current SQL Server connection."
generated: true
llms: "guide"
slot_json: "/reference/slots/mssql/mssql.execute-batch/slot.json"
---

`mssql.execute-batch` is a slot in the `mssql` namespace, in Hyperlambda, the language of Magic Cloud. Executes a batch SQL script on the current SQL Server connection.

* **Value** (`sql-batch`), required: Batch SQL script to execute
* **Returns**: Returns one child node per batch execution result
* **Scope**: requires `mssql.connection` - Requires an open SQL Server connection created by [mssql.connect]

### Guide

<!-- guide -->
Executes a batch SQL script, such as a schema creation script, on the SQL Server connection opened by **[mssql.connect]**.
SQL Server cannot execute scripts containing `GO` separators as one single command, so this slot splits the script
on every line consisting only of `GO` (case insensitive), and executes each part as its own command. This is the
difference between this slot and **[mssql.execute]**, which executes its SQL as one single command.

* __[value]__ - The batch SQL script to execute. Can be a constant or an expression.

After execution the slot's value is `null`, and it has one child per executed batch, each containing a
**[Records affected]** node.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.mssql](/plugins/magic.lambda.mssql/) plugin, which documents every slot it contains.

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

