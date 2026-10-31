---
title: magic.lambda.crypto
moved_anchors: {"combining-rsa-and-aes-cryptography": "/plugins/magic.lambda.crypto/combining-rsa-and-aes-cryptography/", "creating-an-rsa-keypair": "/plugins/magic.lambda.crypto/rsa/#creating-an-rsa-keypair", "cryptographically-signing-and-verifying-the-signature-of-a-message": "/plugins/magic.lambda.crypto/rsa/#cryptographically-signing-and-verifying-the-signature-of-a-message", "encrypting-and-decrypting-a-message-using-rsa": "/plugins/magic.lambda.crypto/rsa/#encrypting-and-decrypting-a-message-using-rsa", "how-to-use-cryptohash-and-cryptohashxxx": "/plugins/magic.lambda.crypto/crypto.hash/", "how-to-use-cryptorandom": "/plugins/magic.lambda.crypto/crypto.random/", "how-to-use-cryptorandomint": "/plugins/magic.lambda.crypto/crypto.random.int/", "how-to-use-cryptoseed": "/plugins/magic.lambda.crypto/crypto.seed/", "hyperlambda-and-cryptography": "/plugins/magic.lambda.crypto/hyperlambda-and-cryptography/", "rsa-cryptography-with-hyperlambda": "/plugins/magic.lambda.crypto/rsa/", "symmetric-cryptography-using-aes": "/plugins/magic.lambda.crypto/aes/", "the-encryption-format": "/plugins/magic.lambda.crypto/combining-rsa-and-aes-cryptography/#the-encryption-format"}
---

The magic.lambda.crypto project provides cryptography helper slots for Magic, allowing you to use both symmetric
and asymmetric cryptography operations in your Hyperlambda applications. The symmetric parts of the project is
using AES internally, and the asymmetric parts is using RSA. In addition to a bunch of _"low level slots"_, the
project also contains combination slots, combining RSA and AES, allowing you to both encrypt and sign a message,
using a single signal invocation. This project also allows you to create RSA key pairs, in addition to
cryptographically hashing files and payloads, etc. More specifically this project contains the following slots.

* __[\[crypto.rsa.create-key\]](/reference/slots/crypto/crypto.rsa.create-key/)__ - Creates a new RSA keypair
* __[\[crypto.rsa.encrypt\]](/reference/slots/crypto/crypto.rsa.encrypt/)__ - RSA encrypts a message
* __[\[crypto.rsa.decrypt\]](/reference/slots/crypto/crypto.rsa.decrypt/)__ - RSA decrypts a message
* __[\[crypto.rsa.sign\]](/reference/slots/crypto/crypto.rsa.sign/)__ - Cryptographically signs a message
* __[\[crypto.rsa.verify\]](/reference/slots/crypto/crypto.rsa.verify/)__ - Verifies a cryptographic signature of some message
* __[\[crypto.aes.encrypt\]](/reference/slots/crypto/crypto.aes.encrypt/)__ - AES encrypts a message
* __[\[crypto.aes.decrypt\]](/reference/slots/crypto/crypto.aes.decrypt/)__ - AES decrypts a message
* __[\[crypto.fingerprint\]](/reference/slots/crypto/crypto.fingerprint/)__ - Creates a fingerprint of something
* __[\[crypto.get-key\]](/reference/slots/crypto/crypto.get-key/)__ - Returns the fingerprint of the public key associated with message
* __[\[crypto.random\]](/reference/slots/crypto/crypto.random/)__ - CSRNG creating random seeds for you
* __[\[crypto.random.int\]](/reference/slots/crypto/crypto.random.int/)__ - CSRNG creating random integer value for you
* __[\[crypto.hash\]](/reference/slots/crypto/crypto.hash/)__ - Hash some message or payload using the specified **[algo]** or **[algorithm]**
* __[\[crypto.hash.md5\]](/reference/slots/crypto/crypto.hash.md5/)__ - MD5 hash some message or payload
* __[\[crypto.hash.sha1\]](/reference/slots/crypto/crypto.hash.sha1/)__ - SHA1 hash some message or payload
* __[\[crypto.hash.sha256\]](/reference/slots/crypto/crypto.hash.sha256/)__ - SHA256 hash some message or payload
* __[\[crypto.hash.sha384\]](/reference/slots/crypto/crypto.hash.sha384/)__ - SHA384 hash some message or payload
* __[\[crypto.hash.sha512\]](/reference/slots/crypto/crypto.hash.sha512/)__ - SHA512 hash some message or payload
* __[\[crypto.password.hash\]](/reference/slots/crypto/crypto.password.hash/)__ - Creates a Blowfish uniquely salted hash
* __[\[crypto.password.verify\]](/reference/slots/crypto/crypto.password.verify/)__ - Verifies a Blowfish uniquely salted hash
* __[\[crypto.encrypt\]](/reference/slots/crypto/crypto.encrypt/)__ - High level slot combining RSA and AES to encrypt some message
* __[\[crypto.decrypt\]](/reference/slots/crypto/crypto.decrypt/)__ - High level slot combining RSA and AES to decrypt some message
* __[\[crypto.sign\]](/reference/slots/crypto/crypto.sign/)__ - High level slot to sign some message
* __[\[crypto.verify\]](/reference/slots/crypto/crypto.verify/)__ - High level slot to verify a signature of some message
* __[\[crypto.seed\]](/reference/slots/crypto/crypto.seed/)__ - Allows you to explicitly seed the CSRNG instance using for instance a manually provided seed


## Blowfish password hashing

As a general security rule of thumb, passwords should never be stored in clear text, but persisted into for
instance a database as _"slowly hashed values with per record based salts"_. This prevents a whole range of
security issues, such as having adversaries creating Rainbow Dictionary attacks on your passwords. This
project contains two slots to implement this, and these are as follows.

* __[crypto.password.hash]__ - Creates a password hash
* __[crypto.password.verify]__ - Verifies a hashed password

Example usage can be found below.

```
crypto.password.hash:SomePasswordHere

crypto.password.verify:SomePasswordHere
   hash:x:@crypto.password.hash
```

The first slot invocation creates a Blowfish hash, while the second slot invocation verifies a previously
created Blowfish hash, given the password as its main argument. If you exchange the second password given
to **[crypto.password.verify]** by for instance adding one random character to it, the result will be
`false` from the second invocation.
Internally these are the slots Magic uses when it creates its JWT authentication database, and stores
passswords into your Magic database.



## Topics

* [RSA cryptography with Hyperlambda](/plugins/magic.lambda.crypto/rsa/) - Creating RSA keypairs, signing and verifying the signature of a message, and encrypting and decrypting with RSA, using the cryptography slots of Hyperlambda.
* [Symmetric cryptography using AES](/plugins/magic.lambda.crypto/aes/) - Encrypting and decrypting a message with a shared secret using AES, with the cryptography slots of Hyperlambda.
* [Hyperlambda and cryptography](/plugins/magic.lambda.crypto/hyperlambda-and-cryptography/) - The magic.lambda.crypto project supports several cryptographic functions, but first a bit of cryptography theory.
* [Combining RSA and AES cryptography](/plugins/magic.lambda.crypto/combining-rsa-and-aes-cryptography/) - AES and RSA are more useful when combined together.
