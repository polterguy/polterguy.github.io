---
title: "[validators.regex]"
description: "validators.regex is a slot in the validators namespace of Magic Cloud. Validates that a value or resolved expression result matches a regular expression, bounded by the execution deadline when set, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.regex/slot.json"
---

`validators.regex` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a value or resolved expression result matches a regular expression, bounded by the execution deadline when set, throwing if validation fails.

* **Value** (`text`), required: Value or expression selecting the node or nodes to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[regex]` | string | yes | Regular expression pattern the value must match. |

Guide: [How to use [validators.regex]](/plugins/magic.lambda.validators/#how-to-use-validatorsregex)

### JSON declaration

This is the complete declaration of `validators.regex`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.regex",
  "description": "Validates that a value or resolved expression result matches a regular expression, bounded by the execution deadline when set, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "regex": {
        "type": "string",
        "kind": "regex",
        "description": "Regular expression pattern the value must match",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `validators.recaptcha`](/reference/slots/validators/validators.recaptcha/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.string` &rarr;](/reference/slots/validators/validators.string/)

