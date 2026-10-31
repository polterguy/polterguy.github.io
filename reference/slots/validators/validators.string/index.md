---
title: "[validators.string]"
description: "validators.string is a slot in the validators namespace of Magic Cloud. Validates that a string value or resolved expression result is within the allowed length range, throwing if validation fails."
generated: true
llms: "guide"
slot_json: "/reference/slots/validators/validators.string/slot.json"
---

`validators.string` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a string value or resolved expression result is within the allowed length range, throwing if validation fails.

* **Value** (`text`), required: String value or expression selecting the node or nodes to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | int | no | Minimum accepted length. Default: `0`. |
| `[max]` | int | no | Maximum accepted length. Default: `int.MaxValue`. |

### Guide

<!-- guide -->
This works the same way as the **[validators.integer]** validator, except instead of being a min/max
_value_ the min/max arguments declares the minimum and maximum _length_ of the string, allowing you
to restrict string length of arguments to a min/max value for your Hyperlambda. Below is example
usage that will throw an exception unless the argument is between 5 and 15 characters in length.

```
validators.string:x:@.some-arg
   min:5
   max:15
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `validators.string`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.string",
  "description": "Validates that a string value or resolved expression result is within the allowed length range, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "text",
      "description": "String value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "min": {
        "type": "int",
        "kind": "validator-min-length",
        "description": "Minimum accepted length",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "max": {
        "type": "int",
        "kind": "validator-max-length",
        "description": "Maximum accepted length",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "int.MaxValue",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `validators.regex`](/reference/slots/validators/validators.regex/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.url` &rarr;](/reference/slots/validators/validators.url/)

