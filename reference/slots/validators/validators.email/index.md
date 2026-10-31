---
title: "[validators.email]"
description: "validators.email is a slot in the validators namespace of Magic Cloud. Validates that a value or resolved expression result is an email address, throwing if validation fails."
generated: true
llms: "guide"
slot_json: "/reference/slots/validators/validators.email/slot.json"
---

`validators.email` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a value or resolved expression result is an email address, throwing if validation fails.

* **Value** (`email`), required: Email value or expression selecting the node or nodes to validate

### Guide

<!-- guide -->
This slot takes no arguments besides an expression, and will throw an exception unless the value of the node
the expression is leading to is a valid email address. Below is example usage.

```
.arg:foo@bar.com
validators.email:x:@.arg
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.validators](/plugins/magic.lambda.validators/) plugin, which documents every slot it contains.

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

