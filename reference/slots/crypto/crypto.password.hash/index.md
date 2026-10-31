---
title: "[crypto.password.hash]"
description: "crypto.password.hash is a slot in the crypto namespace of Magic Cloud. Hashes a plaintext password with bcrypt and a per-user salt; check candidates later with [crypto.password.verify]."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.password.hash/slot.json"
---

`crypto.password.hash` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Hashes a plaintext password with bcrypt and a per-user salt; check candidates later with [crypto.password.verify].

* **Value** (`password,text`), required: Password to hash
* **Returns**: Resolves to the password hash

### Guide

[How to use `crypto.password.hash`](/plugins/magic.lambda.crypto/crypto.password.hash/)

### JSON declaration

This is the complete declaration of `crypto.password.hash`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.password.hash",
  "description": "Hashes a plaintext password with bcrypt and a per-user salt; check candidates later with [crypto.password.verify]",
  "signature": {
    "input": {
      "kind": "password,text",
      "description": "Password to hash",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "password-hash,text",
      "description": "Resolves to the password hash"
    }
  }
}
```

</details>

---

[&larr; `crypto.hash.sha512`](/reference/slots/crypto/crypto.hash.sha512/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.password.verify` &rarr;](/reference/slots/crypto/crypto.password.verify/)

