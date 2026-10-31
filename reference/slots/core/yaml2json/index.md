---
title: "[yaml2json]"
description: "yaml2json is a core slot of Magic Cloud. Transforms YAML into JSON."
generated: true
llms: false
slot_json: "/reference/slots/core/yaml2json/slot.json"
---

`yaml2json` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms YAML into JSON.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the generated JSON string

### Guide

[How to use `yaml2json`](/plugins/magic.lambda.json/yaml2json/)

### JSON declaration

This is the complete declaration of `yaml2json`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "yaml2json",
  "description": "Transforms YAML into JSON",
  "signature": {
    "input": {
      "kind": "yaml",
      "description": "YAML text to transform",
      "required": true,
      "mode": "ValueOrExpression"
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

[&larr; `xml2lambda`](/reference/slots/core/xml2lambda/) | [all core slots](/reference/slots/core/) | [`yaml2lambda` &rarr;](/reference/slots/core/yaml2lambda/)

