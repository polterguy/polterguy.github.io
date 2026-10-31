---
title: "How to use [crypto.sign]"
description: "How to use [crypto.sign] - This slot signs its input with a private key, and is the high level companion of [crypto.verify]."
generated: true
guide: true
---

The reference page of [`crypto.sign`](/reference/slots/crypto/crypto.sign/) has its arguments, constraints and declaration.

This slot signs its input with a private key, and is the high level companion of **[crypto.verify]**. It needs the private **[signing-key]**, and the **[signing-key-fingerprint]** identifying it. Below is an example.

```
crypto.rsa.create-key
   strength:512
crypto.sign:Some message to sign
   signing-key:x:@crypto.rsa.create-key/*/private
   signing-key-fingerprint:x:@crypto.rsa.create-key/*/fingerprint
```
