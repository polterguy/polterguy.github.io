---
title: "How to use [crypto.decrypt]"
description: "How to use [crypto.decrypt] - The [crypto.encrypt] slot requires some message/content, a signing key, an encryption key, and your signing key's fingerprint."
generated: true
guide: true
---

The reference page of [`crypto.decrypt`](/reference/slots/crypto/crypto.decrypt/) has its arguments, constraints and declaration.

The **[crypto.encrypt]** slot requires some message/content, a signing key, an encryption key, and your signing
key's fingerprint. This slot will first cryptographically sign your message using the private key. Then it
will use the public key supplied to encrypt the message, while injecting the fingerprint for the signing key
and the cryptography key into the package. Below is an example.

```
// Recipient's key.
crypto.rsa.create-key
   strength:512

// Sender's key.
crypto.rsa.create-key
   strength:512

// Encrypting some message.
crypto.encrypt:Some super secret message
   encryption-key:x:././*/crypto.rsa.create-key/[0,1]/*/public
   signing-key:x:././*/crypto.rsa.create-key/[1,2]/*/private
   signing-key-fingerprint:x:././*/crypto.rsa.create-key/[1,2]/*/fingerprint

// Decrypting the above encrypted message.
crypto.decrypt:x:-
   decryption-key:x:././*/crypto.rsa.create-key/[0,1]/*/private
   verify-key:x:././*/crypto.rsa.create-key/[1,2]/*/public
```
