---
title: "[crypto.seed]"
description: "crypto.seed is a slot in the crypto namespace of Magic Cloud. Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.seed/slot.json"
---

`crypto.seed` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness.

* **Value** (`crypto-seed,text`), required: Seed value for the random generator

### Guide

[How to use `crypto.seed`](/plugins/magic.lambda.crypto/crypto.seed/)

### JSON declaration

This is the complete declaration of `crypto.seed`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.seed",
  "description": "Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness",
  "signature": {
    "input": {
      "kind": "crypto-seed,text",
      "description": "Seed value for the random generator",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `crypto.rsa.verify`](/reference/slots/crypto/crypto.rsa.verify/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.sign` &rarr;](/reference/slots/crypto/crypto.sign/)

