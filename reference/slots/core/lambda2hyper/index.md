---
title: "[lambda2hyper]"
description: "lambda2hyper is a core slot of Magic Cloud. Transforms a lambda hierarchy into Hyperlambda."
generated: true
llms: false
slot_json: "/reference/slots/core/lambda2hyper/slot.json"
---

`lambda2hyper` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into Hyperlambda.

* **Value** (`lambda-tree,node-list`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated Hyperlambda source

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[comments]` | bool | no | Whether generated Hyperlambda should include comments. Default: `false`. |

### Guide

[How to use `lambda2hyper`](/plugins/magic.lambda.hyperlambda/lambda2hyper/)

### JSON declaration

This is the complete declaration of `lambda2hyper`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2hyper",
  "description": "Transforms a lambda hierarchy into Hyperlambda",
  "signature": {
    "input": {
      "kind": "lambda-tree,node-list",
      "description": "Expression selecting the lambda hierarchy to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "comments": {
        "type": "bool",
        "description": "Whether generated Hyperlambda should include comments",
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
      "kind": "hyperlambda,text",
      "description": "Resolves to the generated Hyperlambda source"
    }
  }
}
```

</details>

---

[&larr; `lambda2html`](/reference/slots/core/lambda2html/) | [all core slots](/reference/slots/core/) | [`lambda2json` &rarr;](/reference/slots/core/lambda2json/)

