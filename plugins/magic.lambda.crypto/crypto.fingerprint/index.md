---
title: "How to use [crypto.fingerprint]"
description: "How to use [crypto.fingerprint] - This slot returns the SHA256 fingerprint of its input, formatted as colon separated hexadecimal, which is what you use to identify a public key."
generated: true
guide: true
---

The reference page of [`crypto.fingerprint`](/reference/slots/crypto/crypto.fingerprint/) has its arguments, constraints and declaration.

This slot returns the SHA256 fingerprint of its input, formatted as colon separated hexadecimal, which is what you use to identify a public key. Below is an example, fingerprinting a newly created public key.

```
crypto.rsa.create-key
   strength:512
crypto.fingerprint:x:@crypto.rsa.create-key/*/public
```
