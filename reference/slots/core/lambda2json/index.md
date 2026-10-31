---
title: "[lambda2json]"
description: "lambda2json is a core slot of Magic Cloud. Transforms a lambda hierarchy into JSON."
generated: true
llms: false
slot_json: "/reference/slots/core/lambda2json/slot.json"
---

`lambda2json` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into JSON.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated JSON string

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | bool | no | Whether to pretty-print the JSON output. Default: `false`. |

Guide: [How to use [lambda2json]](/plugins/magic.lambda.json/#how-to-use-json2lambda-and-lambda2json)

### JSON declaration

This is the complete declaration of `lambda2json`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2json",
  "description": "Transforms a lambda hierarchy into JSON",
  "signature": {
    "input": {
      "kind": "node-list,lambda-tree",
      "description": "Expression selecting the lambda hierarchy to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "format": {
        "type": "bool",
        "description": "Whether to pretty-print the JSON output",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "json,text",
      "description": "Resolves to the generated JSON string"
    }
  }
}
```

</details>

---

[&larr; `lambda2hyper`](/reference/slots/core/lambda2hyper/) | [all core slots](/reference/slots/core/) | [`lambda2xml` &rarr;](/reference/slots/core/lambda2xml/)

