---
title: "[json2lambda-stream]"
description: "json2lambda-stream is a core slot of Magic Cloud. Transforms JSON stream content into a lambda hierarchy."
generated: true
llms: false
slot_json: "/reference/slots/core/json2lambda-stream/slot.json"
---

`json2lambda-stream` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms JSON stream content into a lambda hierarchy.

* **Value** (`stream`), required: JSON stream to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[encoding]` | string | no | Text encoding used to read the JSON stream. Default: `utf-8`. |

Guide: [How to use [json2lambda-stream]](/plugins/magic.lambda.json/#how-to-use-json2lambda-stream)

### JSON declaration

This is the complete declaration of `json2lambda-stream`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "json2lambda-stream",
  "description": "Transforms JSON stream content into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "stream",
      "description": "JSON stream to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "encoding": {
        "type": "string",
        "kind": "text-encoding",
        "description": "Text encoding used to read the JSON stream",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "utf-8",
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

[&larr; `json2lambda`](/reference/slots/core/json2lambda/) | [all core slots](/reference/slots/core/) | [`json2yaml` &rarr;](/reference/slots/core/json2yaml/)

