---
title: "[floatArray2bytes]"
description: "floatArray2bytes is a core slot of Magic Cloud. Serializes a sequence of float values into raw bytes; useful for embedding vectors or feeding binary APIs."
generated: true
llms: false
slot_json: "/reference/slots/core/floatArray2bytes/slot.json"
---

`floatArray2bytes` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Serializes a sequence of float values into raw bytes; useful for embedding vectors or feeding binary APIs.

* **Value** (`float-list`), required: Float values to convert to bytes
* **Returns**: Resolves to the float array converted to bytes

Guide: [How to use [floatArray2bytes]](/plugins/magic.lambda/types/#how-to-use-floatarray2bytes)

### JSON declaration

This is the complete declaration of `floatArray2bytes`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "floatArray2bytes",
  "description": "Serializes a sequence of float values into raw bytes; useful for embedding vectors or feeding binary APIs",
  "signature": {
    "input": {
      "kind": "float-list",
      "description": "Float values to convert to bytes",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "binary-content",
      "description": "Resolves to the float array converted to bytes"
    }
  }
}
```

</details>

---

[&larr; `filter`](/reference/slots/core/filter/) | [all core slots](/reference/slots/core/) | [`for-each` &rarr;](/reference/slots/core/for-each/)

