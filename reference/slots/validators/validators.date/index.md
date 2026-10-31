---
title: "[validators.date]"
description: "validators.date is a slot in the validators namespace of Magic Cloud. Validates that a date value or resolved expression result is within the allowed range, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.date/slot.json"
---

`validators.date` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a date value or resolved expression result is within the allowed range, throwing if validation fails.

* **Value** (`date`), required: Date value or expression selecting the node or nodes to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | date | no | Earliest accepted date. |
| `[max]` | date | no | Latest accepted date. |

### Guide

[How to use `validators.date`](/plugins/magic.lambda.validators/validators.date/)

### JSON declaration

This is the complete declaration of `validators.date`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.date",
  "description": "Validates that a date value or resolved expression result is within the allowed range, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "date",
      "description": "Date value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "min": {
        "type": "date",
        "kind": "validator-min-date",
        "description": "Earliest accepted date",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "max": {
        "type": "date",
        "kind": "validator-max-date",
        "description": "Latest accepted date",
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

[all `validators.*` slots](/reference/slots/validators/) | [`validators.default` &rarr;](/reference/slots/validators/validators.default/)

