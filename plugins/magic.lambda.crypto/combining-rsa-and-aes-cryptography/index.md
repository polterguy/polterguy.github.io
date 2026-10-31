---
title: "Combining RSA and AES cryptography"
description: "Combining RSA and AES cryptography - AES and RSA are more useful when combined together."
generated: true
---

This page is part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) documentation.

AES and RSA are more useful when combined together. Hence, this project contains the following convenience slots, that combines
these two cryptography functions together.

* __[\[crypto.encrypt\]](/reference/slots/crypto/crypto.encrypt/)__ - Encrypts some message using AES + RSA, and signs the message in the process
* __[\[crypto.decrypt\]](/reference/slots/crypto/crypto.decrypt/)__ - Decrypts some message using AES + RSA, optionally verifying a signature in the process
* __[\[crypto.sign\]](/reference/slots/crypto/crypto.sign/)__ - Cryptographically signs a message using RSA and creates a package containing both signature, signing key's fingerprint, and the content that was signed
* __[\[crypto.verify\]](/reference/slots/crypto/crypto.verify/)__ - The opposite of the above, that verifies the integrity of a package created with **[\[crypto.sign\]](/reference/slots/crypto/crypto.sign/)**
* __[\[crypto.get-key\]](/reference/slots/crypto/crypto.get-key/)__ - Returns the fingerprint of the RSA key that was used to encrypt some message using **[\[crypto.encrypt\]](/reference/slots/crypto/crypto.encrypt/)** or sign some message using **[\[crypto.sign\]](/reference/slots/crypto/crypto.sign/)**

The **[\[crypto.encrypt\]](/reference/slots/crypto/crypto.encrypt/)** slot requires some message/content, a signing key, an encryption key, and your signing
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

**Notice** - We're using only 512 bit strength in the above example. Make sure you (at least) use
2048, preferably 4096 in real world usage. The **[\[crypto.encrypt\]](/reference/slots/crypto/crypto.encrypt/)** slot can also optionally handle
a **[seed]** argument, which will seed the CSRNG that's used to generate a symmetric AES encryption
key. To understand what occurs in the above Hyperlambda example, let's walk through it step by step,
starting from the **[\[crypto.encrypt\]](/reference/slots/crypto/crypto.encrypt/)** invocation.

1. The message _"Some super secret message"_ is first cryptographically signed using the private **[signing-key]**
2. The signed message is then AES encrypted using a CSRNG generated random key
3. The AES key from the above is then encrypted using the **[encryption-key]**, that's assumed to be the recipient's public key
4. The signing key's fingerprint is stored inside of the encrypted content, such that when the message is decrypted, the other party can verify that the signature originated from some trusted party
5. The encryption key's fingerprint is stored as bytes, prepended before the encrypted message, which allows the other party to retrieve the correct decryption key, according to what encryption key the caller encrypted the message with. To retrieve a cryptography operation key fingerprint, you can use **[\[crypto.get-key\]](/reference/slots/crypto/crypto.get-key/)**

Hence, the *only* thing that is in plain sight in the above encrypted message, is the fingerprint of the public
key that was used to encrypt the message. Only after the message is decrypted, the signature for the message
can be retrieved, together with the fingerprint of the key that was used to sign the message. Hence, what would
normally be a more complete process, is that after the receiver decrypts the message, he should also verify that
the signature originates from some trusted party. This can be done by simply *omitting* the **[verify-key]** argument
as you invoke **[\[crypto.decrypt\]](/reference/slots/crypto/crypto.decrypt/)**, and then invoke **[\[crypto.get-key\]](/reference/slots/crypto/crypto.get-key/)** on the result of the decryption process,
for then to use the result of **[\[crypto.get-key\]](/reference/slots/crypto/crypto.get-key/)** to lookup the public key used to *verify* the signature of the
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

Only after the message is verified, the actual content of the message is possible to read, as the
value of the **[\[crypto.verify\]](/reference/slots/crypto/crypto.verify/)** slot - Unless you pass in a **[verify-key]** during the invocation
to **[\[crypto.decrypt\]](/reference/slots/crypto/crypto.decrypt/)**, at which point that key will be used to verify the signature of the message,
after the package has been decrypted.
If the above invocation to **[\[crypto.verify\]](/reference/slots/crypto/crypto.verify/)** does not throw an exception, we know for a fact that
the message was cryptographically signed with the private key that matches its **[public-key]** argument.
Normally the fingerprint of the sender's key is asssociated with some sort of _"authorization object"_
to elevate the rights of the user, only *after* having verified the message originated from a trusted
party.

Hence, from the caller's perspective it's *one* invocation to encrypt and sign a message. From the receiver's
perspective it's normally *two* steps to both decrypt and verify the integrity of a message, unless you know who
the message originated from, and you've already loaded the correct public key to verify the signature of
the message.

**Notice** - We're using only 512 bit strength in the above example. Make sure you (at least) use
2048, preferably 4096 in real world usage.

## The encryption format

The encrypted package has the following format.

1. Signing key's fingerprint in SHA256 `byte[]` format, 32 bytes long
2. The length of the signature as `int`, 4 bytes long
3. The actual signature of the message
4. The content of the message in UTF encoded `byte[]` format

Afterwards the result from the above steps is encrypted using AES, with a random generated session key 
that is 32 bytes long. And another package is created, which is the final package, intended for being sent
to the recipient. The final encryption package has a structure as follows.

1. Encryption key's fingerprint in SHA256 `byte[]` format, 32 bytes long
2. The length of the encrypted session key as `int`, 4 bytes long
3. The encrypted session key, encrypted using the recipient's public RSA key
4. The AES encrypted content from the above signing step

Hence, only when *both* of the above lists are done, you have a final encryption package to send
to some recipient.

The other party can retrieve the encryption key used for encrypting the package, using for instance
the **[\[crypto.get-key\]](/reference/slots/crypto/crypto.get-key/)** slot on the package. Then the receiver can use his private RSA key to decrypt
the AES key, and use the decrypted AES key to decrypt the rest of the package - Which will result in getting the
fingerprint of the RSA key used to sign the package, then the signature, and only *then* the content of
the message. However, all of these steps are done automatically if you use the **[\[crypto.decrypt\]](/reference/slots/crypto/crypto.decrypt/)** slot,
except the signature verification process, unless you provide a **[verify-key]** argument to the decryption
process.

The AES key is generated using Bouncy Castle's `SecureRandom` implementation, resulting in a 256 bit
cryptography key. This key again is encrypted using whatever bit strength you selected as you created
your RSA key pair. Hence, the message as a whole, is not stronger than whatever key strength you use
as you supply a **[strength]** argument to the **[\[crypto.rsa.create-key\]](/reference/slots/crypto/crypto.rsa.create-key/)**.

The above format results in that the only _"meta information"_ an adversary can possibly pick up, is
the fingerprint of the public RSA key used to encrypt the AES key, in addition to also the bit strength
of this RSA key, since the bit strength of an RSA key will result in differences in the length of the
encrypted AES key. An adversary will not have access to who encrypted/transmitted the package, he will
not know who, if any signed the package - Or any other parts of the message - Assuming he is not able
to somehow crack the AES encryption, and/or somehow retrieve the private RSA key the AES package's
encryption key was encrypted with.

---

[&larr; Hyperlambda and cryptography](/plugins/magic.lambda.crypto/hyperlambda-and-cryptography/) | [all of magic.lambda.crypto](/plugins/magic.lambda.crypto/)
