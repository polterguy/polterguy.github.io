---
title: "[json2yaml]"
description: "json2yaml is a core slot of Magic Cloud. Transforms JSON into YAML."
generated: true
llms: false
slot_json: "/reference/slots/core/json2yaml/slot.json"
---

`json2yaml` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms JSON into YAML.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the generated YAML string

Guide: [How to use [json2yaml]](/plugins/magic.lambda.json/#how-to-use-yaml2json-and-json2yaml)

### JSON declaration

This is the complete declaration of `json2yaml`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "json2yaml",
  "description": "Transforms JSON into YAML",
  "signature": {
    "input": {
      "kind": "json",
      "description": "JSON text to transform",
      "required": true,
      "mode": "ValueOrExpression"
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

[&larr; `json2lambda-stream`](/reference/slots/core/json2lambda-stream/) | [all core slots](/reference/slots/core/) | [`lambda2csv` &rarr;](/reference/slots/core/lambda2csv/)

