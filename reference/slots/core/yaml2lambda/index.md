---
title: "[yaml2lambda]"
description: "yaml2lambda is a core slot of Magic Cloud. Transforms YAML into a lambda hierarchy."
generated: true
llms: false
slot_json: "/reference/slots/core/yaml2lambda/slot.json"
---

`yaml2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms YAML into a lambda hierarchy.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

Guide: [How to use [yaml2lambda]](/plugins/magic.lambda.json/#how-to-use-yaml2lambda-and-lambda2yaml)

### JSON declaration

This is the complete declaration of `yaml2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "yaml2lambda",
  "description": "Transforms YAML into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "yaml",
      "description": "YAML text to transform",
      "required": true,
      "mode": "ValueOrExpression"
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

[&larr; `yaml2json`](/reference/slots/core/yaml2json/) | [all core slots](/reference/slots/core/) | [`yield` &rarr;](/reference/slots/core/yield/)

