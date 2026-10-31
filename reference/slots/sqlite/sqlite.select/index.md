---
title: "[sqlite.select]"
description: "sqlite.select is a slot in the sqlite namespace of Magic Cloud. Executes a SELECT query on the current SQLite connection."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.select/slot.json"
---

`sqlite.select` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Executes a SELECT query on the current SQLite connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Returns one child node per row returned by the SELECT query
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | long | no | Maximum number of rows to return; omitted or -1 returns all rows. Default: `-1`. |
| `[multiple-result-sets]` | bool | no | Whether multiple SELECT statements in the SQL input should be returned as separate child result containers. Default: `false`. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

### JSON declaration

This is the complete declaration of `sqlite.select`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.select",
  "description": "Executes a SELECT query on the current SQLite connection",
  "signature": {
    "input": {
      "kind": "sql-select",
      "description": "SQL query to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "max": {
        "type": "long",
        "description": "Maximum number of rows to return; omitted or -1 returns all rows",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "-1",
        "role": "Option",
        "projection": "Value"
      },
      "multiple-result-sets": {
        "type": "bool",
        "description": "Whether multiple SELECT statements in the SQL input should be returned as separate child result containers",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
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
      "mode": "Lambda",
      "kind": "node-list",
      "element-kind": "row-object,lambda-tree",
      "description": "Returns one child node per row returned by the SELECT query",
      "children": [
        {
          "type": "lambda",
          "kind": "row",
          "description": "One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "StructuredObject",
          "projection": "StructuredTree",
          "children": {
            "*": {
              "type": "string",
              "kind": "column-value",
              "description": "Column value; child name is the column name (or alias) declared in the read",
              "required": false,
              "mode": "Value",
              "cardinality": "ZeroOrMore",
              "role": "Option",
              "projection": "Value"
            }
          }
        }
      ]
    }
  }
}
```

</details>

---

[&larr; `sqlite.scalar`](/reference/slots/sqlite/sqlite.scalar/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.transaction.commit` &rarr;](/reference/slots/sqlite/sqlite.transaction.commit/)

