---
title: "How to use [crypto.seed]"
description: "How to use [crypto.seed] - No cryptography operation is more secure than the CSRNG instance used to generate random numbers and characters."
generated: true
guide: true
---

The reference page of [`crypto.seed`](/reference/slots/crypto/crypto.seed/) has its arguments, constraints and declaration.

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
