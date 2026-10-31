---
title: "[strings.substring]"
description: "strings.substring is a slot in the strings namespace of Magic Cloud. Extracts a portion of a string starting at the given offset and optional length; out-of-range bounds throw."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.substring/slot.json"
---

`strings.substring` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Extracts a portion of a string starting at the given offset and optional length; out-of-range bounds throw.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the extracted substring

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | int | yes | Start index. |
| _unnamed child node_ | int | no | Optional length. |

### Guide

[How to use `strings.substring`](/plugins/magic.lambda.strings/strings.substring/)

### JSON declaration

This is the complete declaration of `strings.substring`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.substring",
  "description": "Extracts a portion of a string starting at the given offset and optional length; out-of-range bounds throw",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "int",
        "kind": "substring-arg",
        "description": "Start index",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      },
      {
        "type": "int",
        "kind": "substring-arg",
        "description": "Optional length",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the extracted substring"
    }
  }
}
```

</details>

---

[&larr; `strings.starts-with`](/reference/slots/strings/strings.starts-with/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.to-lower` &rarr;](/reference/slots/strings/strings.to-lower/)

