---
title: "[validators.recaptcha]"
description: "validators.recaptcha is a slot in the validators namespace of Magic Cloud. Validates a reCAPTCHA response token, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.recaptcha/slot.json"
---

`validators.recaptcha` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates a reCAPTCHA response token, throwing if validation fails.

* **Value** (`recaptcha-token`), required: reCAPTCHA response token to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[site-key]` | string | yes | reCAPTCHA site key. |
| `[secret]` | string | yes | reCAPTCHA secret key. |
| `[min]` | decimal | yes | Minimum acceptable reCAPTCHA score. |

### Guide

[How to use `validators.recaptcha`](/plugins/magic.lambda.validators/validators.recaptcha/)

### JSON declaration

This is the complete declaration of `validators.recaptcha`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.recaptcha",
  "description": "Validates a reCAPTCHA response token, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "recaptcha-token",
      "description": "reCAPTCHA response token to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "site-key": {
        "type": "string",
        "kind": "recaptcha-site-key",
        "description": "reCAPTCHA site key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "secret": {
        "type": "string",
        "kind": "recaptcha-secret",
        "description": "reCAPTCHA secret key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "min": {
        "type": "decimal",
        "description": "Minimum acceptable reCAPTCHA score",
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

[&larr; `validators.mandatory`](/reference/slots/validators/validators.mandatory/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.regex` &rarr;](/reference/slots/validators/validators.regex/)

