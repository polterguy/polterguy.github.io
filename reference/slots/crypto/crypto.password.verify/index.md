---
title: "[crypto.password.verify]"
description: "crypto.password.verify is a slot in the crypto namespace of Magic Cloud. Verifies a password against a hash."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.password.verify/slot.json"
---

`crypto.password.verify` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Verifies a password against a hash.

* **Value** (`password,text`), required: Plaintext password to verify
* **Returns**: Returns true if the password matches the supplied hash

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[hash]` | string | yes | BCrypt password hash produced by [crypto.password.hash]. |

### Guide

[How to use `crypto.password.verify`](/plugins/magic.lambda.crypto/crypto.password.verify/)

### JSON declaration

This is the complete declaration of `crypto.password.verify`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.password.verify",
  "description": "Verifies a password against a hash",
  "signature": {
    "input": {
      "kind": "password,text",
      "description": "Plaintext password to verify",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "hash": {
        "type": "string",
        "kind": "password-hash",
        "description": "BCrypt password hash produced by [crypto.password.hash]",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the password matches the supplied hash"
    }
  }
}
```

</details>

---

[&larr; `crypto.password.hash`](/reference/slots/crypto/crypto.password.hash/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.random` &rarr;](/reference/slots/crypto/crypto.random/)

