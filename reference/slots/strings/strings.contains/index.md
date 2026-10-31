---
title: "[strings.contains]"
description: "strings.contains is a slot in the strings namespace of Magic Cloud. Returns true if a string contains the specified text."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.contains/slot.json"
---

`strings.contains` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if a string contains the specified text.

* **Value** (`text`), required: Text to search
* **Returns**: Returns true if the string contains the supplied text

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | String argument. |

Guide: [How to use [strings.contains]](/plugins/magic.lambda.strings/#how-to-use-stringscontains)

### JSON declaration

This is the complete declaration of `strings.contains`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.contains",
  "description": "Returns true if a string contains the specified text",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to search",
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
      "description": "Returns true if the string contains the supplied text"
    }
  }
}
```

</details>

---

[&larr; `strings.concat`](/reference/slots/strings/strings.concat/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.ends-with` &rarr;](/reference/slots/strings/strings.ends-with/)

