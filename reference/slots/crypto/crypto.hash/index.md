---
title: "[crypto.hash]"
description: "crypto.hash is a slot in the crypto namespace of Magic Cloud. Hashes input using SHA256 by default, or the supplied [algorithm] child."
generated: true
llms: "guide"
slot_json: "/reference/slots/crypto/crypto.hash/slot.json"
---

`crypto.hash` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Hashes input using SHA256 by default, or the supplied [algorithm] child.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[algorithm]` | string | no | Hash algorithm: md5, sha1, sha256, sha384, or sha512. Default: `sha256`. |
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

### Constraints

* **ExactlyOneOf**: Provide either input content or [filename] (`[input]`, `[filename]`)

### Guide

<!-- guide -->
The **[crypto.hash]** slot can be used to generate hash values. When you invoke it, you can choose
between having the hash returned as raw a `byte[]`, as a _"fingerprint"_ or as its bit encoded hex
version. Below is an example of all three of these formats.

```
.data:Some data to hash

crypto.hash:x:@.data
   format:fingerprint

crypto.hash:x:@.data
   format:text

crypto.hash:x:@.data
   format:raw
```

To override the hashing algorithm used when creating hash values, apply an **[algorithm]** argument, and
set its value to the hashing algorithm you want to use. You can choose between the following hashing
algorithms as you consume the above slot.

* sha1
* md5
* sha256
* sha384
* sha512

**Notice** - sha1 and md5 is supported _only_ for legacy reasons, and _should not be used_ unless you have
a legacy system depending upon it. Sha1 and md5 are considered weak today due to the statistical probability
of that they can result in what's commonly referred to as _"hash collision"_.
This project also contains convenience overloads with the hashing algorithm being a part of the name of the
invocation, such as illustrated below.

* __[crypto.hash.sha1]__
* __[crypto.hash.md5]__
* __[crypto.hash.sha256]__
* __[crypto.hash.sha384]__
* __[crypto.hash.sha512]__

In addition you can hash a file directly, without having to load it first, by providing a **[filename]** argument
to it, such as illustrated below.

```
crypto.hash.sha256
   filename:/README.md
```

#### About cryptography fingerprints

The fingerprint format resulting from a hash invocation is useful due to being much more easily read by
humans, and in such a regard better suited for being stored as a key reference into for instance a database,
and/or transmitted as a key reference over the network to other machines.

A fingerprint is actually just a cryptographic hash of your data, such as for instance your public key,
payload, etc.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `crypto.hash`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.hash",
  "description": "Hashes input using SHA256 by default, or the supplied [algorithm] child",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "String or byte[] content to hash when [filename] is not supplied",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "algorithm": {
        "type": "string",
        "kind": "hash-algorithm",
        "description": "Hash algorithm: md5, sha1, sha256, sha384, or sha512",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "sha256",
        "role": "Option",
        "projection": "Value"
      },
      "filename": {
        "type": "string",
        "kind": "file-path",
        "description": "File to hash when no input content is supplied",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "format": {
        "type": "string",
        "kind": "hash-format",
        "description": "Hash output format: text, raw, or fingerprint",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "text",
        "role": "Option",
        "projection": "Value"
      }
    },
    "constraints": [
      {
        "description": "Provide either input content or [filename]",
        "values": [
          "input",
          "filename"
        ],
        "kind": "ExactlyOneOf"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "hash,fingerprint,hash-bytes,text",
      "description": "Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]"
    }
  }
}
```

</details>

---

[&larr; `crypto.get-key`](/reference/slots/crypto/crypto.get-key/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.hash.md5` &rarr;](/reference/slots/crypto/crypto.hash.md5/)

