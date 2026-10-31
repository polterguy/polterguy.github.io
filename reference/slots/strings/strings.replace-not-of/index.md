---
title: "[strings.replace-not-of]"
description: "strings.replace-not-of is a slot in the strings namespace of Magic Cloud. Replaces characters not found in the supplied allow-list."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.replace-not-of/slot.json"
---

`strings.replace-not-of` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Replaces characters not found in the supplied allow-list.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after replacing characters not found in the allowed set

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Allowed characters; any character not in this set is replaced. |
| _unnamed child node_ | string | yes | Replacement text for non-matching characters. |

### Guide

[How to use `strings.replace-not-of`](/plugins/magic.lambda.strings/strings.replace-not-of/)

### JSON declaration

This is the complete declaration of `strings.replace-not-of`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.replace-not-of",
  "description": "Replaces characters not found in the supplied allow-list",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "character-set",
        "description": "Allowed characters; any character not in this set is replaced",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      },
      {
        "type": "string",
        "kind": "character-replacement",
        "description": "Replacement text for non-matching characters",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the string after replacing characters not found in the allowed set"
    }
  }
}
```

</details>

---

[&larr; `strings.replace`](/reference/slots/strings/strings.replace/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.split` &rarr;](/reference/slots/strings/strings.split/)

