---
title: "[crypto.aes.encrypt]"
description: "crypto.aes.encrypt is a slot in the crypto namespace of Magic Cloud. Encrypts data using AES."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.aes.encrypt/slot.json"
---

`crypto.aes.encrypt` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Encrypts data using AES.

* **Value** (`text,binary-content`), required: Content to encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[password]` | string\|byte[] | yes | Password or raw AES key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.aes.encrypt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.aes.encrypt",
  "description": "Encrypts data using AES",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "Content to encrypt",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "password": {
        "type": "string|byte[]",
        "kind": "password,aes-key",
        "description": "Password or raw AES key",
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
      }
    },
    "output": {
      "mode": "Value",
      "kind": "aes-encrypted-package,fingerprint-source",
      "description": "Resolves to the encrypted package as base64 text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.aes.decrypt`](/reference/slots/crypto/crypto.aes.decrypt/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.decrypt` &rarr;](/reference/slots/crypto/crypto.decrypt/)

