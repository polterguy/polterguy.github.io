---
title: "[strings.trim]"
description: "strings.trim is a slot in the strings namespace of Magic Cloud. Trims characters from both ends of the specified string."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.trim/slot.json"
---

`strings.trim` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Trims characters from both ends of the specified string.

* **Value** (`text`), required: Text to trim
* **Returns**: Resolves to the trimmed string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | no | Optional characters to trim. |

### Guide

<!-- guide -->
This guide covers [`strings.trim`](/reference/slots/strings/strings.trim/), [`strings.trim-start`](/reference/slots/strings/strings.trim-start/), [`strings.trim-end`](/reference/slots/strings/strings.trim-end/) together.

Trims a string, either both sides, only the start of it, or only the end of it, for
occurrences of characters found in the sequence of characters provided as its argument.

```
strings.trim:09thomas12
   .:1234567890

// Results in "thomas"
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.strings](/plugins/magic.lambda.strings/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `strings.trim`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.trim",
  "description": "Trims characters from both ends of the specified string",
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
      "description": "Resolves to the trimmed string"
    }
  }
}
```

</details>

---

[&larr; `strings.to-upper`](/reference/slots/strings/strings.to-upper/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.trim-end` &rarr;](/reference/slots/strings/strings.trim-end/)

