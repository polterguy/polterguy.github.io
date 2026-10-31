---
title: "[validators.integer]"
description: "validators.integer is a slot in the validators namespace of Magic Cloud. Validates that an integer value or resolved expression result is within the allowed range, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.integer/slot.json"
---

`validators.integer` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that an integer value or resolved expression result is within the allowed range, throwing if validation fails.

* **Value** (`integer,number`), required: Integer value or expression selecting the node or nodes to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | long | no | Minimum accepted value. |
| `[max]` | long | no | Maximum accepted value. |

Guide: [How to use [validators.integer]](/plugins/magic.lambda.validators/#how-to-use-validatorsinteger)

### JSON declaration

This is the complete declaration of `validators.integer`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.integer",
  "description": "Validates that an integer value or resolved expression result is within the allowed range, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "integer,number",
      "description": "Integer value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "min": {
        "type": "long",
        "kind": "validator-min-integer",
        "description": "Minimum accepted value",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "max": {
        "type": "long",
        "kind": "validator-max-integer",
        "description": "Maximum accepted value",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `validators.enum`](/reference/slots/validators/validators.enum/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.mandatory` &rarr;](/reference/slots/validators/validators.mandatory/)

