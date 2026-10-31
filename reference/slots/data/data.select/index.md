---
title: "[data.select]"
description: "data.select is a slot in the data namespace of Magic Cloud. Executes a query and returns rows from the current database connection."
generated: true
llms: false
slot_json: "/reference/slots/data/data.select/slot.json"
---

`data.select` is a slot in the `data` namespace, in Hyperlambda, the language of Magic Cloud. Executes a query and returns rows from the current database connection.

* **Value** (`sql-select`), required: SQL query to execute
* **Returns**: Resolves to query result rows as child nodes
* **Scope**: requires `data.connection` - Requires an open database connection created by [data.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[database-type]` | string | no | Database adapter to use instead of the configured default. |
| `[max]` | long | no | Maximum number of rows to return; omitted or -1 returns all rows. Default: `-1`. |
| `[multiple-result-sets]` | bool | no | Whether multiple SELECT statements in the SQL input should be returned as separate child result containers. Default: `false`. |
| _any node name_ | object | no | SQL parameter value; child name is used as the parameter name referenced by the SQL statement. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One row returned by the read; child nodes carry the selected column values, with each child's name being the column name or alias from the SELECT statement. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | Column value; child name is the column name (or alias) declared in the read. Can be repeated. |

Guide: [How to use [data.select]](/plugins/magic.data.common/#how-to-use-dataselect)

### JSON declaration

This is the complete declaration of `data.select`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "data.select",
  "description": "Executes a query and returns rows from the current database connection",
  "signature": {
    "input": {
      "kind": "sql-select",
      "description": "SQL query to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "database-type": {
        "type": "string",
        "kind": "database-type",
        "description": "Database adapter to use instead of the configured default",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne"
      },
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
      "requires": "data.connection",
      "description": "Requires an open database connection created by [data.connect]"
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "element-kind": "row-object,lambda-tree",
      "description": "Resolves to query result rows as child nodes",
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

[&larr; `data.scan`](/reference/slots/data/data.scan/) | [all `data.*` slots](/reference/slots/data/) | [`data.transaction.commit` &rarr;](/reference/slots/data/data.transaction.commit/)

