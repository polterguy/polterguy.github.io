---
title: "[sql.create]"
description: "sql.create is a slot in the sql namespace of Magic Cloud. Builds a parameterized INSERT SQL statement."
generated: true
llms: "guide"
slot_json: "/reference/slots/sql/sql.create/slot.json"
---

`sql.create` is a slot in the `sql` namespace, in Hyperlambda, the language of Magic Cloud. Builds a parameterized INSERT SQL statement.

* **Returns**: Resolves to the generated SQL string in value and the generated parameter nodes as children

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[table]` | string | yes | Table name to use in the SQL statement. |
| `[values]` | lambda | yes | Column values to insert or update. |
| `[values]` / _any node name_ | object | yes | Column name and value. Can be repeated. |

### Guide

<!-- guide -->
This slot will generate the SQL necessary to insert a record into a database for you. Besides the table
argument, this slot can only be given one argument, which is __[values]__. Below is an example of usage.

```
sql.create
   table:table1
   values
      field1:howdy
      field2:world
```

Notice, to avoid SQL injection attacks, this slot will always return parameters expected to be passed in
from any potentially malicious clients as SQL parameters - Hence, the complete returned value of the
above Hyperlambda will be as follows.

```
sql.create:insert into 'table1' ('field1', 'field2') values (@0, @1)
   @0:howdy
   @1:world
```

The basic idea is that everything that might be dynamically injected into your data access layer,
should be consumed as `SqlParameters`, or something equivalent, to prevent SQL injection attacks
towards your database. This is true for all arguments passed in as data for all slots in the project.
The slot will in its specialized implementations return the ID of the inserted record if possible,
unless you explicitly parametrize it with a **[return-id]** argument and set its value to boolean
`false`.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `sql.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sql.create",
  "description": "Builds a parameterized INSERT SQL statement",
  "signature": {
    "children": {
      "table": {
        "type": "string",
        "kind": "table-name",
        "description": "Table name to use in the SQL statement",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne"
      },
      "values": {
        "type": "lambda",
        "description": "Column values to insert or update",
        "required": true,
        "mode": "DynamicNamedValues",
        "cardinality": "ExactlyOne",
        "children": {
          "*": {
            "type": "object",
            "kind": "sql-column-value,text,number,boolean,date,guid,content,value",
            "description": "Column name and value",
            "required": true,
            "mode": "ValueOrExpression",
            "cardinality": "OneOrMore"
          }
        }
      }
    },
    "output": {
      "mode": "Both",
      "description": "Resolves to the generated SQL string in value and the generated parameter nodes as children"
    }
  }
}
```

</details>

---

[all `sql.*` slots](/reference/slots/sql/) | [`sql.delete` &rarr;](/reference/slots/sql/sql.delete/)

