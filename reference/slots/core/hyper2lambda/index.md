---
title: "[hyper2lambda]"
description: "hyper2lambda is a core slot of Magic Cloud. Transforms Hyperlambda into a lambda hierarchy."
generated: true
llms: false
slot_json: "/reference/slots/core/hyper2lambda/slot.json"
---

`hyper2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms Hyperlambda into a lambda hierarchy.

* **Value** (`hyperlambda`), required: Hyperlambda text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[comments]` | bool | no | Whether parser comment nodes should be preserved as [..] nodes with the comment text as value. Default: `false`. |

### Guide

[How to use `hyper2lambda`](/plugins/magic.lambda.hyperlambda/hyper2lambda/)

### JSON declaration

This is the complete declaration of `hyper2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "hyper2lambda",
  "description": "Transforms Hyperlambda into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "hyperlambda",
      "description": "Hyperlambda text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "comments": {
        "type": "bool",
        "description": "Whether parser comment nodes should be preserved as [..] nodes with the comment text as value",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "lambda-tree",
      "description": "Resolves to the parsed lambda hierarchy as child nodes"
    }
  }
}
```

</details>

---

[&larr; `html2pdf`](/reference/slots/core/html2pdf/) | [all core slots](/reference/slots/core/) | [`if` &rarr;](/reference/slots/core/if/)

