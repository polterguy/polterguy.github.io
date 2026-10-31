---
title: crypto.* slots
description: The 24 slots named crypto.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [crypto.aes.decrypt]

Decrypts AES encrypted data.

* **Value** (`aes-encrypted-package`), required: Encrypted package to decrypt
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[password]` | string\|byte[] | yes | Password or raw AES key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.aes.encrypt]

Encrypts data using AES.

* **Value** (`text,binary-content`), required: Content to encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[password]` | string\|byte[] | yes | Password or raw AES key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.decrypt]

Decrypts data using the configured combination algorithm.

* **Value** (`crypto-encrypted-package`), required: Encrypted package to decrypt and optionally verify
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[decryption-key]` | string\|byte[] | yes | Private decryption key. |
| `[verification-key]` | string\|byte[] | yes | Public key used to verify the signature. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.encrypt]

Encrypts data using the configured combination algorithm.

* **Value** (`text,binary-content`), required: Content to sign and encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[signing-key]` | string\|byte[] | yes | Private signing key. |
| `[encryption-key]` | string\|byte[] | yes | Public encryption key. |
| `[signing-key-fingerprint]` | string\|byte[] | yes | Fingerprint for the signing key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |
| `[seed]` | string\|byte[] | no | Optional encryption seed. |

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
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.hash]

Hashes input using SHA256 by default, or the supplied [algorithm] child.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[algorithm]` | string | no | Hash algorithm: md5, sha1, sha256, sha384, or sha512. Default: `sha256`. |
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

* **Constraint** (ExactlyOneOf): Provide either input content or [filename] (`[input]`, `[filename]`)

Guide: [How to use [crypto.hash]](/plugins/magic.lambda.crypto/#how-to-use-cryptohash-and-cryptohashxxx)

## [crypto.hash.md5]

Hashes input using the MD5 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

* **Constraint** (ExactlyOneOf): Provide either input content or [filename] (`[input]`, `[filename]`)

## [crypto.hash.sha1]

Hashes input using the SHA1 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

* **Constraint** (ExactlyOneOf): Provide either input content or [filename] (`[input]`, `[filename]`)

## [crypto.hash.sha256]

Hashes input using the SHA256 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

* **Constraint** (ExactlyOneOf): Provide either input content or [filename] (`[input]`, `[filename]`)

## [crypto.hash.sha384]

Hashes input using the SHA384 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

* **Constraint** (ExactlyOneOf): Provide either input content or [filename] (`[input]`, `[filename]`)

## [crypto.hash.sha512]

Hashes input using the SHA512 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

* **Constraint** (ExactlyOneOf): Provide either input content or [filename] (`[input]`, `[filename]`)

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
| `[hash]` | string | yes | BCrypt password hash produced by [crypto.password.hash]. |

## [crypto.random]

Returns a cryptographically secure random string or random bytes.

* **Returns**: Resolves to a random string, or random bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | int | no | Minimum random length. Default: `10`. |
| `[max]` | int | no | Maximum random length. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |
| `[seed]` | string | no | Optional deterministic seed. |

Guide: [How to use [crypto.random]](/plugins/magic.lambda.crypto/#how-to-use-cryptorandom)

## [crypto.random.int]

Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound.

* **Returns**: Resolves to a random integer less than the optional [max] value

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Exclusive maximum integer. Default: `int.MaxValue`. |
| `[seed]` | string | no | Optional deterministic seed. |

Guide: [How to use [crypto.random.int]](/plugins/magic.lambda.crypto/#how-to-use-cryptorandomint)

## [crypto.rsa.create-key]

Generates a fresh RSA key pair; returns the public key and private key as separate child nodes for storage or distribution.

* **Returns**: Resolves to the generated RSA key pair as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[strength]` | int | no | RSA key strength in bits. Default: `2048`. |
| `[seed]` | string\|byte[] | no | Optional deterministic seed. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.rsa.decrypt]

Decrypts RSA encrypted data.

* **Value** (`rsa-encrypted-package`), required: Encrypted package to decrypt
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[private-key]` | string\|byte[] | yes | Private key for the RSA operation. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.rsa.encrypt]

Encrypts data using RSA.

* **Value** (`text,binary-content`), required: Content to encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[public-key]` | string\|byte[] | yes | Public key for the RSA operation. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.rsa.sign]

Signs data using RSA.

* **Value** (`text,binary-content`), required: Content to sign
* **Returns**: Resolves to the signature as base64 text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[private-key]` | string\|byte[] | yes | Private key for the RSA operation. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.rsa.verify]

Verifies an RSA signature.

* **Value** (`text,binary-content`), required: Content to verify against the supplied signature

| Argument | Type | Required | Description |
|---|---|---|---|
| `[signature]` | string\|byte[] | yes | RSA signature to verify. |
| `[public-key]` | string\|byte[] | yes | Public key used to verify the signature. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

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
| `[signing-key]` | string\|byte[] | yes | Private signing key. |
| `[signing-key-fingerprint]` | string\|byte[] | yes | Fingerprint for the signing key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

## [crypto.verify]

Verifies a signature using the configured combination algorithm.

* **Value** (`crypto-signature`), required: Signed package to verify
* **Returns**: Resolves to the verified content as text or raw bytes when [raw] is true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[verification-key]` | string\|byte[] | yes | Public key used to verify the signature. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

