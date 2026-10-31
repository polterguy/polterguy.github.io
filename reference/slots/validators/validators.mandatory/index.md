---
title: "[validators.mandatory]"
description: "validators.mandatory is a slot in the validators namespace of Magic Cloud. Validates that the input value or resolved expression result is present, throwing if validation fails."
generated: true
llms: "guide"
slot_json: "/reference/slots/validators/validators.mandatory/slot.json"
---

`validators.mandatory` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that the input value or resolved expression result is present, throwing if validation fails.

* **Value** (`validated-value`), required: Literal value or expression to validate as mandatory

### Guide

<!-- guide -->
This slot simply throws an exception if the specified argument is not supplied. Below is example
usage.

```
validators.mandatory:x:@.arguments/*/mandatory_arg
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `validators.mandatory`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.mandatory",
  "description": "Validates that the input value or resolved expression result is present, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "validated-value",
      "description": "Literal value or expression to validate as mandatory",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `validators.integer`](/reference/slots/validators/validators.integer/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.recaptcha` &rarr;](/reference/slots/validators/validators.recaptcha/)

