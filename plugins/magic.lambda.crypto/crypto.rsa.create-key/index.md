---
title: "How to use [crypto.rsa.create-key]"
description: "How to use [crypto.rsa.create-key] - To encrypt a message, you can use something as follows."
generated: true
guide: true
---

The reference page of [`crypto.rsa.create-key`](/reference/slots/crypto/crypto.rsa.create-key/) has its arguments, constraints and declaration.

To encrypt a message, you can use something as follows.

```
.message:Some message you want to encrypt

crypto.rsa.create-key

crypto.rsa.encrypt:x:@.message
   public-key:x:@crypto.rsa.create-key/*/public

crypto.rsa.decrypt:x:@crypto.rsa.encrypt
   private-key:x:@crypto.rsa.create-key/*/private
```

Notice how the encryption above is using the *public key*, and the decryption is using the *private key*. The encrypt slot
will internally base64 encode the encrypted data for simplicity reasons, allowing you to immediately inspect it as text,
since encryption will result in a byte array, which is often inconvenient to handle.
You can override this by passing in a **[raw]** argument, and set its value to true, at which point a `byte[]` will be
returned.
You can also supply **[raw]** as you invoke **[crypto.rsa.decrypt]** if you know the content in the message is
not a string, but rather an array of `byte[]`. Base64 encoding a byte array normally makes it larger in size,
and also require CPU resources in both ends of the communication, implying it is sometimes important to have the
raw byte array, instead of its base64 encoded equivalent.
