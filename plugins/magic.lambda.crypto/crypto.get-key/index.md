---
title: "How to use [crypto.get-key]"
description: "How to use [crypto.get-key] - Hence, the only thing that is in plain sight in the above encrypted message, is the fingerprint of the public key that was used to encrypt the message."
generated: true
guide: true
---

The reference page of [`crypto.get-key`](/reference/slots/crypto/crypto.get-key/) has its arguments, constraints and declaration.

Hence, the *only* thing that is in plain sight in the above encrypted message, is the fingerprint of the public
key that was used to encrypt the message. Only after the message is decrypted, the signature for the message
can be retrieved, together with the fingerprint of the key that was used to sign the message. Hence, what would
normally be a more complete process, is that after the receiver decrypts the message, he should also verify that
the signature originates from some trusted party. This can be done by simply *omitting* the **[verify-key]** argument
as you invoke **[crypto.decrypt]**, and then invoke **[crypto.get-key]** on the result of the decryption process,
for then to use the result of **[crypto.get-key]** to lookup the public key used to *verify* the signature of the
package.

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
   
// Uncomment this line to retrieve signing key's fingerprint
// That you can use to lookup the public key needed to verify
// the signature
// crypto.get-key:x:-

// Verifying signature of encrypted message.
crypto.verify:x:@crypto.decrypt
   public-key:x:././*/crypto.rsa.create-key/[1,2]/*/public
```
