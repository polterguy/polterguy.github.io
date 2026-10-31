---
title: "[validators.enum]"
description: "validators.enum is a slot in the validators namespace of Magic Cloud. Validates that a value or resolved expression result is one of the allowed options, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.enum/slot.json"
---

`validators.enum` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a value or resolved expression result is one of the allowed options, throwing if validation fails.

* **Value** (`enum-value`), required: Value or expression selecting the node or nodes to validate

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Accepted enum value. Can be repeated. |

Guide: [How to use [validators.enum]](/plugins/magic.lambda.validators/#how-to-use-validatorsenum)

### JSON declaration

This is the complete declaration of `validators.enum`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.enum",
  "description": "Validates that a value or resolved expression result is one of the allowed options, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "enum-value",
      "description": "Value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "enum-value",
        "description": "Accepted enum value",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "OneOrMore",
        "role": "Option",
        "projection": "Value"
      }
    ]
  }
}
```

</details>

---

[&larr; `validators.email`](/reference/slots/validators/validators.email/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.integer` &rarr;](/reference/slots/validators/validators.integer/)

