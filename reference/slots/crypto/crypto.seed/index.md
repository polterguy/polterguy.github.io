---
title: "[crypto.seed]"
description: "crypto.seed is a slot in the crypto namespace of Magic Cloud. Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness."
generated: true
llms: "guide"
slot_json: "/reference/slots/crypto/crypto.seed/slot.json"
---

`crypto.seed` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness.

* **Value** (`crypto-seed,text`), required: Seed value for the random generator

### Guide

<!-- guide -->
No cryptography operation is more secure than the CSRNG instance used to generate random numbers and characters.
This project accommodates for that, by explicitly allowing you to add to its CSRNG seed with something resembling
the following.

```
crypto.seed:Foo Bar Whatever Some Random Seed
```

Internally this is used in Magic by invoking the above slot with the value of its auth secret during
startup and setup. Since this value can be manually edited by the end user, this provides you with
a _"super paranoid"_ solution to ensure extremely large amounts of entropy in its internal CSRNG
instance. If you wish to further seed the CSRNG, you can invoke at any point in time, with some random
humanly provided gibberish, further adding to its entropy, which later will be used when ever
some cryptographically secured random strings or bytes are required, such as when generating key pairs,
using combination cryptography, etc. Such seed invocations are _"cummulative"_ and _adds_ to the existing
entropy, implying for each invocation to **[crypto.seed]**, the CSRNG engine of Magic becomes more
unpredictable.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) plugin, which documents every slot it contains.

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

