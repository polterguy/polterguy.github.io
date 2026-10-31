---
title: "[strings.split]"
description: "strings.split is a slot in the strings namespace of Magic Cloud. Splits a string at every occurrence of the separator and returns each segment as an unnamed child node."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.split/slot.json"
---

`strings.split` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Splits a string at every occurrence of the separator and returns each segment as an unnamed child node.

* **Value** (`text`), required: Text to split
* **Returns**: Returns one child node per split string item

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Separator to split on. |

Guide: [How to use [strings.split]](/plugins/magic.lambda.strings/#how-to-use-stringssplit)

### JSON declaration

This is the complete declaration of `strings.split`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.split",
  "description": "Splits a string at every occurrence of the separator and returns each segment as an unnamed child node",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to split",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "string-separator",
        "description": "Separator to split on",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    ],
    "output": {
      "mode": "Lambda",
      "kind": "string-list",
      "element-kind": "text",
      "description": "Returns one child node per split string item"
    }
  }
}
```

</details>

---

[&larr; `strings.replace-not-of`](/reference/slots/strings/strings.replace-not-of/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.starts-with` &rarr;](/reference/slots/strings/strings.starts-with/)

