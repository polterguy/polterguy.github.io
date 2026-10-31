---
title: "[csv2lambda]"
description: "csv2lambda is a core slot of Magic Cloud. Transforms CSV into a lambda hierarchy."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/csv2lambda/slot.json"
---

`csv2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms CSV into a lambda hierarchy.

* **Value** (`csv`), required: CSV text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes; each child is one CSV row containing column-named values

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[types]` | lambda | no | Column type conversions keyed by column name. |
| `[types]` / _any node name_ | string | yes | Type name for the column. Can be repeated. |
| `[null-value]` | string | no | String used to represent null values. Default: `[NULL]`. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One CSV record returned as a child node; column values appear as named children keyed by the header column name. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | CSV column value; child name is the header column name. Can be repeated. |

### Guide

<!-- guide -->
This slot converts a CSV string into a lambda object. In its simplest form it would resemble the following.

```
.csv:@"name,age
Thomas Hansen,47
John Doe,67"

csv2lambda:x:@.csv
```

It can optionally take a type declaration through a **[\[types\]](/reference/slots/core/types/)** argument, which allows you to add typing support
to the slot.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.csv](/plugins/magic.lambda.csv/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `csv2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "csv2lambda",
  "description": "Transforms CSV into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "csv",
      "description": "CSV text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "types": {
        "type": "lambda",
        "kind": "csv-column-types",
        "description": "Column type conversions keyed by column name",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "DynamicMap",
        "projection": "StructuredTree",
        "children": {
          "*": {
            "type": "string",
            "kind": "csv-column-type",
            "description": "Type name for the column",
            "required": true,
            "mode": "ValueOrExpression",
            "cardinality": "OneOrMore",
            "role": "DynamicMap",
            "projection": "Value"
          }
        }
      },
      "null-value": {
        "type": "string",
        "kind": "null-value",
        "description": "String used to represent null values",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "[NULL]",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "element-kind": "csv-row,lambda-tree",
      "description": "Resolves to the parsed lambda hierarchy as child nodes; each child is one CSV row containing column-named values",
      "children": [
        {
          "type": "lambda",
          "kind": "row",
          "description": "One CSV record returned as a child node; column values appear as named children keyed by the header column name",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "StructuredObject",
          "projection": "StructuredTree",
          "children": {
            "*": {
              "type": "string",
              "kind": "column-value",
              "description": "CSV column value; child name is the header column name",
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

[&larr; `convert`](/reference/slots/core/convert/) | [all core slots](/reference/slots/core/) | [`default` &rarr;](/reference/slots/core/default/)

