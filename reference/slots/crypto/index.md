---
title: "crypto.* slots"
description: "The 24 slots named crypto.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

24 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`crypto.aes.decrypt`](/reference/slots/crypto/crypto.aes.decrypt/) | Decrypts AES encrypted data. |
| [`crypto.aes.encrypt`](/reference/slots/crypto/crypto.aes.encrypt/) | Encrypts data using AES. |
| [`crypto.decrypt`](/reference/slots/crypto/crypto.decrypt/) | Decrypts data using the configured combination algorithm. |
| [`crypto.encrypt`](/reference/slots/crypto/crypto.encrypt/) | Encrypts data using the configured combination algorithm. |
| [`crypto.fingerprint`](/reference/slots/crypto/crypto.fingerprint/) | Returns a SHA256 fingerprint of the input, formatted as colon-separated hex; useful for identifying public keys. |
| [`crypto.get-key`](/reference/slots/crypto/crypto.get-key/) | Returns or derives a cryptographic key. |
| [`crypto.hash`](/reference/slots/crypto/crypto.hash/) | Hashes input using SHA256 by default, or the supplied [algorithm] child. |
| [`crypto.hash.md5`](/reference/slots/crypto/crypto.hash.md5/) | Hashes input using the MD5 algorithm, which is broken for collision resistance and only here for legacy data; use [crypto.password.hash] for passwords. |
| [`crypto.hash.sha1`](/reference/slots/crypto/crypto.hash.sha1/) | Hashes input using the SHA1 algorithm, which is broken for collision resistance and only here for legacy data; use [crypto.password.hash] for passwords. |
| [`crypto.hash.sha256`](/reference/slots/crypto/crypto.hash.sha256/) | Hashes input using the SHA256 algorithm. |
| [`crypto.hash.sha384`](/reference/slots/crypto/crypto.hash.sha384/) | Hashes input using the SHA384 algorithm. |
| [`crypto.hash.sha512`](/reference/slots/crypto/crypto.hash.sha512/) | Hashes input using the SHA512 algorithm. |
| [`crypto.password.hash`](/reference/slots/crypto/crypto.password.hash/) | Hashes a plaintext password with bcrypt and a per-user salt; check candidates later with [crypto.password.verify]. |
| [`crypto.password.verify`](/reference/slots/crypto/crypto.password.verify/) | Verifies a password against a hash. |
| [`crypto.random`](/reference/slots/crypto/crypto.random/) | Returns a cryptographically secure random string or random bytes. |
| [`crypto.random.int`](/reference/slots/crypto/crypto.random.int/) | Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound. |
| [`crypto.rsa.create-key`](/reference/slots/crypto/crypto.rsa.create-key/) | Generates a fresh RSA key pair; returns the public key and private key as separate child nodes for storage or distribution. |
| [`crypto.rsa.decrypt`](/reference/slots/crypto/crypto.rsa.decrypt/) | Decrypts RSA encrypted data. |
| [`crypto.rsa.encrypt`](/reference/slots/crypto/crypto.rsa.encrypt/) | Encrypts data using RSA. |
| [`crypto.rsa.sign`](/reference/slots/crypto/crypto.rsa.sign/) | Signs data using RSA. |
| [`crypto.rsa.verify`](/reference/slots/crypto/crypto.rsa.verify/) | Verifies an RSA signature. |
| [`crypto.seed`](/reference/slots/crypto/crypto.seed/) | Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness. |
| [`crypto.sign`](/reference/slots/crypto/crypto.sign/) | Signs data using the configured combination algorithm. |
| [`crypto.verify`](/reference/slots/crypto/crypto.verify/) | Verifies a signature using the configured combination algorithm. |

