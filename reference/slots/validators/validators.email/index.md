---
title: "[validators.email]"
description: "validators.email is a slot in the validators namespace of Magic Cloud. Validates that a value or resolved expression result is an email address, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.email/slot.json"
---

`validators.email` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a value or resolved expression result is an email address, throwing if validation fails.

* **Value** (`email`), required: Email value or expression selecting the node or nodes to validate

Guide: [How to use [validators.email]](/plugins/magic.lambda.validators/#how-to-use-validatorsemail)

### JSON declaration

This is the complete declaration of `validators.email`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.email",
  "description": "Validates that a value or resolved expression result is an email address, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "email",
      "description": "Email value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `validators.default`](/reference/slots/validators/validators.default/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.enum` &rarr;](/reference/slots/validators/validators.enum/)

