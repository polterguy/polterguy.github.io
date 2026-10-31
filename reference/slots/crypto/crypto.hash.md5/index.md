---
title: "[crypto.hash.md5]"
description: "crypto.hash.md5 is a slot in the crypto namespace of Magic Cloud. Hashes input using the MD5 algorithm."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.hash.md5/slot.json"
---

`crypto.hash.md5` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Hashes input using the MD5 algorithm.

* **Value** (`text,binary-content`), optional: String or byte[] content to hash when [filename] is not supplied
* **Returns**: Resolves to the computed hash as text, raw bytes, or fingerprint according to [format]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | no | File to hash when no input content is supplied. |
| `[format]` | string | no | Hash output format: text, raw, or fingerprint. Default: `text`. |

### Constraints

* **ExactlyOneOf**: Provide either input content or [filename] (`[input]`, `[filename]`)

### JSON declaration

This is the complete declaration of `crypto.hash.md5`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.hash.md5",
  "description": "Hashes input using the MD5 algorithm",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "String or byte[] content to hash when [filename] is not supplied",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
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

[&larr; `crypto.hash`](/reference/slots/crypto/crypto.hash/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.hash.sha1` &rarr;](/reference/slots/crypto/crypto.hash.sha1/)

