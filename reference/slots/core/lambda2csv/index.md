---
title: "[lambda2csv]"
description: "lambda2csv is a core slot of Magic Cloud. Transforms a lambda hierarchy into CSV."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/lambda2csv/slot.json"
---

`lambda2csv` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into CSV.

* **Value** (`node-list`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the CSV content in value and column type nodes as children

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[null-value]` | string | no | String used to represent null values. Default: `[NULL]`. |

### Guide

<!-- guide -->
This slot converts the specified lambda object to a CSV string. Below is an example of usage.

```
.data
   .
      name:Thomas Hansen
      age:int:47
   .
      name:John Doe
      age:int:67

lambda2csv:x:-/*
```

The slot will return type information as children of your **[lambda2csv]** invocation.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.csv](/plugins/magic.lambda.csv/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `lambda2csv`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2csv",
  "description": "Transforms a lambda hierarchy into CSV",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes (rows) to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
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
      "mode": "Both",
      "kind": "csv,text",
      "description": "Resolves to the CSV content in value and column type nodes as children"
    }
  }
}
```

</details>

---

[&larr; `json2yaml`](/reference/slots/core/json2yaml/) | [all core slots](/reference/slots/core/) | [`lambda2html` &rarr;](/reference/slots/core/lambda2html/)

