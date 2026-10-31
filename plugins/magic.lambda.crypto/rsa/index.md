---
title: "RSA cryptography with Hyperlambda"
description: "Creating RSA keypairs, signing and verifying the signature of a message, and encrypting and decrypting with RSA, using the cryptography slots of Hyperlambda."
generated: true
---

This page is part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) documentation.

## Creating an RSA keypair

To create an RSA keypair that you can use for other cryptographic services later, you can use something as follows.

```
crypto.rsa.create-key
   strength:2048
   seed:some random jibberish text
```

The above will return 4 nodes to you as you invoke it.

* __[private]__ - Base64 encoded private key in DER format
* __[public]__ - Base 64 encoded public key in DER format
* __[fingerprint]__ - Fingerprint encoded SHA256 hash of your _public_ key
* __[fingerprint-raw]__ - Raw SHA256 hash of your public key

Both the **[strength]** and **[seed]** is optional above. Strength will default to 2048, which might be too weak
for serious cryptography, but increasing your strength too much, might result in that the above function spends several
seconds, possibly minutes to return if you set it too high - In addition to that your key pair becomes very large.
The **[seed]** is optional, and even if you don't provide a seed argument, the default seed should still be strong
enough to avoid predictions. Depending upon your paranoia level, you might want to manually seed the above
slot by having users type in random text as they generate keys. A major security concern in cryptography is CSRNG,
or what's referred to as _"Cryptographically Secure Random Number Generators"_, which aren't always as cryptographically
secure as we might think, since if its seed is predictable, the random bytes it generates can easily be _"replayed"_.

A good strength for an RSA key, is considered to be 4096, which developers around the world feels are secure enough
to avoid brute force _"guessing"_ of your private key. According to what we know about cryptography, all other concerns
set aside, a 4096 bit strength key pair, *should* be impossible to break. If you're just playing around with cryptography
to learn, 1024 is probably more than enough.

Notice, if you want the key back as raw bytes, you can supply a **[raw]** argument, and set its value to boolean
true, at which point the returned key(s) will only be DER encoded, and returned as a raw `byte[]`. This might be
useful, if you for instance need to persist the key to disc, as a binary file, etc. All the RSA slots can return
their results as `byte[]` values, if you provide a **[raw]** argument to them, and set its value to true.
If you don't provide a raw argument, the returned value will be base64 encoded DER format.

This slot will also return the fingerprint of your public key, which is useful to keep around somewhere,
since it's used in other cryptographic operations to identify keys used in operation, etc. The public key's
fingerprint is usually used to identify a specific key somehow.


## Cryptographically signing and verifying the signature of a message

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
be thrown during the verify stage. Something you can verify yourself by uncommenting the above **[\[set-value\]](/reference/slots/core/set-value/)**
invocation. Throwing an exception is a conscious choice, due to the potential security breaches an error
in your code might have, creating a false positive if you erroneously invert an **[\[if\]](/reference/slots/core/if/)** statement. Even though
this is technically _"using exceptions for control flow"_, it has been a conscious design choice
as the library was created, to avoid false positives during the verification process of a signature.

Notice, if you want the signature back as raw bytes, you can supply a **[raw]** argument, and set its value to boolean
true, at which point the returned signature will be returned as a raw `byte[]`. This might be
useful, if you for instance need to persist the signature to disc, as a binary file, etc.
If you don't provide a raw argument, the returned value will be a base64 encoded byte array.


## Encrypting and decrypting a message using RSA

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
You can also supply **[raw]** as you invoke **[\[crypto.rsa.decrypt\]](/reference/slots/crypto/crypto.rsa.decrypt/)** if you know the content in the message is
not a string, but rather an array of `byte[]`. Base64 encoding a byte array normally makes it larger in size,
and also require CPU resources in both ends of the communication, implying it is sometimes important to have the
raw byte array, instead of its base64 encoded equivalent.

---

[all of magic.lambda.crypto](/plugins/magic.lambda.crypto/) | [Symmetric cryptography using AES &rarr;](/plugins/magic.lambda.crypto/aes/)
