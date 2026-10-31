---
title: "[data.select]"
description: "data.select is a slot in the data namespace of Magic Cloud. Executes a query and returns rows from the current database connection."
generated: true
llms: "guide"
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

### Guide

<!-- guide -->
This slot allows you to pass in any arbitrary SQL you wish, and evaluate it to a `DataReader`, and return
all records as a lambda object. You can find an example below.

```
data.connect:sakila
   data.select:select first_name, last_name from actor limit 5
```

Assuming you have the _"sakila"_ database from Oracle installed in your database, and your default
database type is MySQL, the result of the above will end up looking like the following.

```
data.connect
   data.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
      ""
         first_name:ED
         last_name:CHASE
      ""
         first_name:JENNIFER
         last_name:DAVIS
      ""
         first_name:JOHNNY
         last_name:LOLLOBRIGIDA
```

This slot requires SQL resembling your specialised database type of dialect, and will
not in any ways transpile the SQL towards your specific underlying database type's SQL dialect.
If you can, you should rather use **[data.read]**, to avoid lockin towards a specific database
vendor's SQL dialect.
You can also select multiple result sets if you have batch type of SQL statements, containing
multiple SQL statements, and you want to return the result of all SQL statements you're executing.
You do this by providing a **[multiple-result-sets]** argument and set its value to boolean true.
If you do this, the slot will return an array of arrays, one outer array for each result set
your SQL generates. Below is an example.

```sql
data.select:"select * from table1; select * from table2;"
   multiple-result-sets:bool:true
```

Which would result in something resembling the following.

```
   data.select
      ""
         ""
            field1:foo1
            field2:bar1
         ""
            field1:foo2
            field2:bar2
      ""
         ""
            field1:foo1
            field2:bar1
         ""
            field1:foo2
            field2:bar2
```
<!-- /guide -->

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

