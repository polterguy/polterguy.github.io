---
title: "[strings.trim-start]"
description: "strings.trim-start is a slot in the strings namespace of Magic Cloud. Trims characters from the start of the specified string."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.trim-start/slot.json"
---

`strings.trim-start` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Trims characters from the start of the specified string.

* **Value** (`text`), required: Text to trim
* **Returns**: Resolves to the string with leading characters removed

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | no | Optional characters to trim. |

Guide: [How to use [strings.trim-start]](/plugins/magic.lambda.strings/#how-to-use-stringstrim-stringstrim-start-stringstrim-end)

### JSON declaration

This is the complete declaration of `strings.trim-start`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.trim-start",
  "description": "Trims characters from the start of the specified string",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to trim",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "trim-characters",
        "description": "Optional characters to trim",
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
      "description": "Resolves to the string with leading characters removed"
    }
  }
}
```

</details>

---

[&larr; `strings.trim-end`](/reference/slots/strings/strings.trim-end/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.url-decode` &rarr;](/reference/slots/strings/strings.url-decode/)

