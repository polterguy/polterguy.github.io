---
title: "[validators.enum]"
description: "validators.enum is a slot in the validators namespace of Magic Cloud. Validates that a value or resolved expression result is one of the allowed options, throwing if validation fails."
generated: true
llms: "guide"
slot_json: "/reference/slots/validators/validators.enum/slot.json"
---

`validators.enum` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a value or resolved expression result is one of the allowed options, throwing if validation fails.

* **Value** (`enum-value`), required: Value or expression selecting the node or nodes to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Accepted enum value. Can be repeated. |

### Guide

<!-- guide -->
This validator will throw an exception unless the specified string argument is one of the legal values. Usage
could be as follows.

```
validators.enum:x:@.arguments/*/enum_value
   .:val1
   .:val2
```

If the above **[enum_value]** is not either `val1` or `val2` the validator will throw an exception.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.validators](/plugins/magic.lambda.validators/) plugin, which documents every slot it contains.

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

