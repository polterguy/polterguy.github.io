---
title: "[lambda2yaml]"
description: "lambda2yaml is a core slot of Magic Cloud. Transforms a lambda hierarchy into YAML."
generated: true
llms: false
slot_json: "/reference/slots/core/lambda2yaml/slot.json"
---

`lambda2yaml` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into YAML.

* **Value** (`node-list,lambda-tree`), optional: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the generated YAML string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Nodes to convert, used when the slot has no value. Can be repeated. |

### Guide

[How to use `lambda2yaml`](/plugins/magic.lambda.json/yaml2lambda/)

### JSON declaration

This is the complete declaration of `lambda2yaml`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2yaml",
  "description": "Transforms a lambda hierarchy into YAML",
  "signature": {
    "input": {
      "kind": "node-list,lambda-tree",
      "description": "Expression selecting the nodes (rows) to transform",
      "required": false,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Nodes to convert, used when the slot has no value",
        "required": false,
        "mode": "SourceLambda",
        "cardinality": "ZeroOrMore",
        "role": "Payload",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "yaml,text",
      "description": "Resolves to the generated YAML string"
    }
  }
}
```

</details>

---

[&larr; `lambda2xml`](/reference/slots/core/lambda2xml/) | [all core slots](/reference/slots/core/) | [`lt` &rarr;](/reference/slots/core/lt/)

