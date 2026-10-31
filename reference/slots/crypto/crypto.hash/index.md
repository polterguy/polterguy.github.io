---
title: "[crypto.hash]"
description: "crypto.hash is a slot in the crypto namespace of Magic Cloud. Hashes input using SHA256 by default, or the supplied [algorithm] child."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.hash/slot.json"
---

`crypto.hash` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Hashes input using SHA256 by default, or the supplied [algorithm] child.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[algorithm]` | string | no | Hash algorithm: md5, sha1, sha256, sha384, or sha512. Default: `sha256`. |
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

### Constraints

* **ExactlyOneOf**: Provide either input content or [filename] (`[input]`, `[filename]`)

Guide: [How to use [crypto.hash]](/plugins/magic.lambda.crypto/#how-to-use-cryptohash-and-cryptohashxxx)

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

