---
title: "How to use [crypto.decrypt]"
description: "How to use [crypto.decrypt] - The encrypted package has the following format."
generated: true
guide: true
---

The reference page of [`crypto.decrypt`](/reference/slots/crypto/crypto.decrypt/) has its arguments, constraints and declaration.

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
the **[crypto.get-key]** slot on the package. Then the receiver can use his private RSA key to decrypt
the AES key, and use the decrypted AES key to decrypt the rest of the package - Which will result in getting the
fingerprint of the RSA key used to sign the package, then the signature, and only *then* the content of
the message. However, all of these steps are done automatically if you use the **[crypto.decrypt]** slot,
except the signature verification process, unless you provide a **[verify-key]** argument to the decryption
process.

The AES key is generated using Bouncy Castle's `SecureRandom` implementation, resulting in a 256 bit
cryptography key. This key again is encrypted using whatever bit strength you selected as you created
your RSA key pair. Hence, the message as a whole, is not stronger than whatever key strength you use
as you supply a **[strength]** argument to the **[crypto.rsa.create-key]**.

The above format results in that the only _"meta information"_ an adversary can possibly pick up, is
the fingerprint of the public RSA key used to encrypt the AES key, in addition to also the bit strength
of this RSA key, since the bit strength of an RSA key will result in differences in the length of the
encrypted AES key. An adversary will not have access to who encrypted/transmitted the package, he will
not know who, if any signed the package - Or any other parts of the message - Assuming he is not able
to somehow crack the AES encryption, and/or somehow retrieve the private RSA key the AES package's
encryption key was encrypted with.
