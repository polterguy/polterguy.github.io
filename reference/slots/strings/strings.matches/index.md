---
title: "[strings.matches]"
description: "strings.matches is a slot in the strings namespace of Magic Cloud. Returns regular expression matches, bounded by the execution deadline when set."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.matches/slot.json"
---

`strings.matches` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns regular expression matches, bounded by the execution deadline when set.

* **Value** (`text`), required: Text to match against the regular expression
* **Returns**: Returns one child node per regular expression match

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Regular expression pattern to match against the source string. |

Guide: [How to use [strings.matches]](/plugins/magic.lambda.strings/#how-to-use-stringsmatches)

### JSON declaration

This is the complete declaration of `strings.matches`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.matches",
  "description": "Returns regular expression matches, bounded by the execution deadline when set",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to match against the regular expression",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "regex-pattern",
        "description": "Regular expression pattern to match against the source string",
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
      "kind": "regex-match-list,string-list",
      "element-kind": "regex-match,text",
      "description": "Returns one child node per regular expression match"
    }
  }
}
```

</details>

---

[&larr; `strings.length`](/reference/slots/strings/strings.length/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.mixin` &rarr;](/reference/slots/strings/strings.mixin/)

