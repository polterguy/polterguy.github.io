---
title: "[crypto.encrypt]"
description: "crypto.encrypt is a slot in the crypto namespace of Magic Cloud. Encrypts data using the configured combination algorithm."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.encrypt/slot.json"
---

`crypto.encrypt` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Encrypts data using the configured combination algorithm.

* **Value** (`text,binary-content`), required: Content to sign and encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[encryption-key]` | string\|byte[] | yes | Public encryption key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |
| `[seed]` | string\|byte[] | no | Optional encryption seed. |
| `[signing-key]` | string\|byte[] | yes | Private signing key. |
| `[signing-key-fingerprint]` | string\|byte[] | yes | Fingerprint for the signing key. |

### JSON declaration

This is the complete declaration of `crypto.encrypt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.encrypt",
  "description": "Encrypts data using the configured combination algorithm",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "Content to sign and encrypt",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "signing-key": {
        "type": "string|byte[]",
        "kind": "crypto-private-key",
        "description": "Private signing key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "encryption-key": {
        "type": "string|byte[]",
        "kind": "crypto-public-key",
        "description": "Public encryption key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "signing-key-fingerprint": {
        "type": "string|byte[]",
        "kind": "crypto-key-fingerprint",
        "description": "Fingerprint for the signing key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "raw": {
        "type": "bool",
        "description": "Whether to return raw bytes instead of encoded text",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "seed": {
        "type": "string|byte[]",
        "kind": "crypto-seed",
        "description": "Optional encryption seed",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "crypto-encrypted-package,fingerprint-source",
      "description": "Resolves to the encrypted package as base64 text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.decrypt`](/reference/slots/crypto/crypto.decrypt/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.fingerprint` &rarr;](/reference/slots/crypto/crypto.fingerprint/)

