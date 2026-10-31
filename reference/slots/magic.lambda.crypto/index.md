---
title: magic.lambda.crypto slot reference
description: Every slot in magic.lambda.crypto with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.crypto](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.crypto). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.crypto](/plugins/magic.lambda.crypto/)._

## [crypto.aes.decrypt]

Decrypts AES encrypted data.

* **Value** (`aes-encrypted-package`), required: Encrypted package to decrypt
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.aes.encrypt]

Encrypts data using AES.

* **Value** (`text,binary-content`), required: Content to encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.decrypt]

Decrypts data using the configured combination algorithm.

* **Value** (`crypto-encrypted-package`), required: Encrypted package to decrypt and optionally verify
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.encrypt]

Encrypts data using the configured combination algorithm.

* **Value** (`text,binary-content`), required: Content to sign and encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.fingerprint]

Returns a SHA256 fingerprint of the input, formatted as colon-separated hex; useful for identifying public keys.

* **Value** (`fingerprint-source`), required: Base64 encoded content or raw byte[] content to fingerprint
* **Returns**: Resolves to the SHA256 hash of the supplied content formatted as a fingerprint

## [crypto.get-key]

Returns or derives a cryptographic key.

* **Value** (`crypto-encrypted-package`), required: Encrypted package to extract the key fingerprint from
* **Returns**: Resolves to the package key fingerprint as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.hash]

Hashes input using SHA256 by default, or the supplied [algorithm] child.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[algorithm]` | string | no | Hash algorithm: md5, sha1, sha256, sha384, or sha512 |
| `[filename]` | string | no | File to hash when no input content is supplied |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint |

Guide: [How to use [crypto.hash]](/plugins/magic.lambda.crypto/#how-to-use-cryptohash-and-cryptohashxxx)

## [crypto.hash.md5]

Hashes input using the MD5 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint |

## [crypto.hash.sha1]

Hashes input using the SHA1 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint |

## [crypto.hash.sha256]

Hashes input using the SHA256 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint |

## [crypto.hash.sha384]

Hashes input using the SHA384 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint |

## [crypto.hash.sha512]

Hashes input using the SHA512 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint |

## [crypto.password.hash]

Hashes a plaintext password with bcrypt and a per-user salt; check candidates later with [crypto.password.verify].

* **Value** (`password,text`), required: Password to hash
* **Returns**: Resolves to the password hash

## [crypto.password.verify]

Verifies a password against a hash.

* **Value** (`password,text`), required: Plaintext password to verify
* **Returns**: Returns true if the password matches the supplied hash

| Argument | Type | Required | Description |
|---|---|---|---|
| `[hash]` | string | yes | BCrypt password hash produced by [crypto.password.hash] |

## [crypto.random]

Returns a cryptographically secure random string or random bytes.

* **Returns**: Resolves to a random string, or random bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | int | no | Minimum random length |
| `[max]` | int | no | Maximum random length |
| `[seed]` | string | no | Optional deterministic seed |

Guide: [How to use [crypto.random]](/plugins/magic.lambda.crypto/#how-to-use-cryptorandom)

## [crypto.random.int]

Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound.

* **Returns**: Resolves to a random integer less than the optional [max] value

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Exclusive maximum integer |
| `[seed]` | string | no | Optional deterministic seed |

Guide: [How to use [crypto.random.int]](/plugins/magic.lambda.crypto/#how-to-use-cryptorandomint)

## [crypto.rsa.create-key]

Generates a fresh RSA key pair; returns the public key and private key as separate child nodes for storage or distribution.

* **Returns**: Resolves to the generated RSA key pair as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[strength]` | int | no | RSA key strength in bits |

## [crypto.rsa.decrypt]

Decrypts RSA encrypted data.

* **Value** (`rsa-encrypted-package`), required: Encrypted package to decrypt
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.rsa.encrypt]

Encrypts data using RSA.

* **Value** (`text,binary-content`), required: Content to encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.rsa.sign]

Signs data using RSA.

* **Value** (`text,binary-content`), required: Content to sign
* **Returns**: Resolves to the signature as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.rsa.verify]

Verifies an RSA signature.

* **Value** (`text,binary-content`), required: Content to verify against the supplied signature

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.seed]

Adds entropy to the secure random number generator; useful when supplying additional out-of-band randomness.

* **Value** (`crypto-seed,text`), required: Seed value for the random generator

Guide: [How to use [crypto.seed]](/plugins/magic.lambda.crypto/#how-to-use-cryptoseed)

## [crypto.sign]

Signs data using the configured combination algorithm.

* **Value** (`text,binary-content`), required: Content to sign
* **Returns**: Resolves to the signed package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

## [crypto.verify]

Verifies a signature using the configured combination algorithm.

* **Value** (`crypto-signature`), required: Signed package to verify
* **Returns**: Resolves to the verified content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text |

