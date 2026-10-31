---
title: "[strings.replace]"
description: "strings.replace is a slot in the strings namespace of Magic Cloud. Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.replace/slot.json"
---

`strings.replace` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after replacing the specified substring

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Text or pattern to find. |
| _unnamed child node_ | string | no | Replacement text. |

### Guide

[How to use `strings.replace`](/plugins/magic.lambda.strings/strings.replace/)

### JSON declaration

This is the complete declaration of `strings.replace`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.replace",
  "description": "Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches",
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
        "kind": "text",
        "description": "Text or pattern to find",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      },
      {
        "type": "string",
        "kind": "text",
        "description": "Replacement text",
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
      "description": "Resolves to the string after replacing the specified substring"
    }
  }
}
```

</details>

---

[&larr; `strings.regex-replace`](/reference/slots/strings/strings.regex-replace/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.replace-not-of` &rarr;](/reference/slots/strings/strings.replace-not-of/)

