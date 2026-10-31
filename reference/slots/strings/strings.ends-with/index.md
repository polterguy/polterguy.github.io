---
title: "[strings.ends-with]"
description: "strings.ends-with is a slot in the strings namespace of Magic Cloud. Returns true if a string ends with the specified text."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.ends-with/slot.json"
---

`strings.ends-with` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if a string ends with the specified text.

* **Value** (`text`), required: Text to inspect
* **Returns**: Returns true if the string ends with the supplied text

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | String argument. |

### Guide

[How to use `strings.ends-with`](/plugins/magic.lambda.strings/strings.ends-with/)

### JSON declaration

This is the complete declaration of `strings.ends-with`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.ends-with",
  "description": "Returns true if a string ends with the specified text",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to inspect",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "text",
        "description": "String argument",
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
      "kind": "boolean",
      "description": "Returns true if the string ends with the supplied text"
    }
  }
}
```

</details>

---

[&larr; `strings.contains`](/reference/slots/strings/strings.contains/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.html-decode` &rarr;](/reference/slots/strings/strings.html-decode/)

