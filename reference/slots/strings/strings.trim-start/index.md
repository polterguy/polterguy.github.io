---
title: "[strings.trim-start]"
description: "strings.trim-start is a slot in the strings namespace of Magic Cloud. Trims characters from the start of the specified string."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.trim-start/slot.json"
---

`strings.trim-start` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Trims characters from the start of the specified string.

* **Value** (`text`), required: Text to trim
* **Returns**: Resolves to the string with leading characters removed

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | no | Optional characters to trim. |

### Guide

<!-- guide -->
This guide covers [`strings.trim-start`](/reference/slots/strings/strings.trim-start/), [`strings.trim`](/reference/slots/strings/strings.trim/), [`strings.trim-end`](/reference/slots/strings/strings.trim-end/) together.

Trims a string, either both sides, only the start of it, or only the end of it, for
occurrences of characters found in the sequence of characters provided as its argument.

```
strings.trim:09thomas12
   .:1234567890

// Results in "thomas"
```
<!-- /guide -->

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

