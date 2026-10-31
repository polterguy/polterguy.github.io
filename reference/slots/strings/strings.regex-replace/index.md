---
title: "[strings.regex-replace]"
description: "strings.regex-replace is a slot in the strings namespace of Magic Cloud. Replaces text using a regular expression, bounded by the execution deadline when set."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.regex-replace/slot.json"
---

`strings.regex-replace` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Replaces text using a regular expression, bounded by the execution deadline when set.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after applying the regular-expression replacement

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Regular expression pattern to match. |
| _unnamed child node_ | string | yes | Replacement text. |

### Guide

<!-- guide -->
Replaces matches of the given regular expression with some static sequence of characters.

```
// Results in "FOO bar hansen"
strings.regex-replace:foo bar hansen
   .:fo+
   .:FOO
```

The first argument is what regular expression to match, the second argument is what to replace
all matches with.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.strings](/plugins/magic.lambda.strings/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `strings.regex-replace`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.regex-replace",
  "description": "Replaces text using a regular expression, bounded by the execution deadline when set",
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
        "kind": "regex-pattern",
        "description": "Regular expression pattern to match",
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
        "description": "Replacement text",
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
      "description": "Resolves to the string after applying the regular-expression replacement"
    }
  }
}
```

</details>

---

[&larr; `strings.mixin`](/reference/slots/strings/strings.mixin/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.replace` &rarr;](/reference/slots/strings/strings.replace/)

