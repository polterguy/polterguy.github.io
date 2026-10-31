---
title: "[strings.starts-with]"
description: "strings.starts-with is a slot in the strings namespace of Magic Cloud. Returns true if a string starts with the specified text."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.starts-with/slot.json"
---

`strings.starts-with` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if a string starts with the specified text.

* **Value** (`text`), required: Text to inspect
* **Returns**: Returns true if the string starts with the supplied text

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | String argument. |

### Guide

<!-- guide -->
Returns true if the specified string starts with some sequence of characters.

```
// Returns true
strings.starts-with:Thomas Hansen Is Cool
   .:Thomas

// Returns false
strings.starts-with:Thomas Hansen Is Cool
   .:Hansen
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.strings](/plugins/magic.lambda.strings/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `strings.starts-with`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.starts-with",
  "description": "Returns true if a string starts with the specified text",
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
      "description": "Returns true if the string starts with the supplied text"
    }
  }
}
```

</details>

---

[&larr; `strings.split`](/reference/slots/strings/strings.split/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.substring` &rarr;](/reference/slots/strings/strings.substring/)

