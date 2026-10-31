---
title: "[json2lambda]"
description: "json2lambda is a core slot of Magic Cloud. Transforms JSON into a lambda hierarchy."
generated: true
llms: false
slot_json: "/reference/slots/core/json2lambda/slot.json"
---

`json2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms JSON into a lambda hierarchy.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

Guide: [How to use [json2lambda]](/plugins/magic.lambda.json/#how-to-use-json2lambda-and-lambda2json)

### JSON declaration

This is the complete declaration of `json2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "json2lambda",
  "description": "Transforms JSON into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "json",
      "description": "JSON text to transform",
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

[&larr; `join`](/reference/slots/core/join/) | [all core slots](/reference/slots/core/) | [`json2lambda-stream` &rarr;](/reference/slots/core/json2lambda-stream/)

