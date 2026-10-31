---
title: "[lambda2yaml]"
description: "lambda2yaml is a core slot of Magic Cloud. Transforms a lambda hierarchy into YAML."
generated: true
llms: false
slot_json: "/reference/slots/core/lambda2yaml/slot.json"
---

`lambda2yaml` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into YAML.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the generated YAML string

Guide: [How to use [lambda2yaml]](/plugins/magic.lambda.json/#how-to-use-yaml2lambda-and-lambda2yaml)

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
      "required": true,
      "mode": "Expression"
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

