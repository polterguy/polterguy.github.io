---
title: "How to use [crypto.rsa.verify]"
description: "How to use [crypto.rsa.verify] - You can use a previously created private RSA key to cryptographically sign some data or message, intended to be passed over an insecure context, allowing the caller to use your public..."
generated: true
guide: true
---

The reference page of [`crypto.rsa.verify`](/reference/slots/crypto/crypto.rsa.verify/) has its arguments, constraints and declaration.

You can use a previously created private RSA key to cryptographically sign some data or message, intended to be passed
over an insecure context, allowing the caller to use your public key to verify the message was in fact created
by the owner of the private key. To sign some arbitrary content using your private key, and also verify the message
was correctly signed with a specific key, you can use something as follows.

```
// The message can also by byte arrays.
.message:Some message you wish to sign

crypto.rsa.create-key

// Notice, using PRIVATE key
crypto.rsa.sign:x:@.message
   private-key:x:@crypto.rsa.create-key/*/private

// Uncommenting these lines, will make the verify process throw an exception
// set-value:x:@.message
//    .:Some message you wish to sign - XXXX

// Notice, using PUBLIC key
crypto.rsa.verify:x:@.message
   signature:x:@crypto.rsa.sign
   public-key:x:@crypto.rsa.create-key/*/public
```

If somebody tampers with the content between the signing process and the verify process, an exception will
be thrown during the verify stage. Something you can verify yourself by uncommenting the above **[set-value]**
invocation. Throwing an exception is a conscious choice, due to the potential security breaches an error
in your code might have, creating a false positive if you erroneously invert an **[if]** statement. Even though
this is technically _"using exceptions for control flow"_, it has been a conscious design choice
as the library was created, to avoid false positives during the verification process of a signature.

Notice, if you want the signature back as raw bytes, you can supply a **[raw]** argument, and set its value to boolean
true, at which point the returned signature will be returned as a raw `byte[]`. This might be
useful, if you for instance need to persist the signature to disc, as a binary file, etc.
If you don't provide a raw argument, the returned value will be a base64 encoded byte array.
