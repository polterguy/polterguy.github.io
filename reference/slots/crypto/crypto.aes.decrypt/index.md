---
title: "[crypto.aes.decrypt]"
description: "crypto.aes.decrypt is a slot in the crypto namespace of Magic Cloud. Decrypts AES encrypted data."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.aes.decrypt/slot.json"
---

`crypto.aes.decrypt` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Decrypts AES encrypted data.

* **Value** (`aes-encrypted-package`), required: Encrypted package to decrypt
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[password]` | string\|byte[] | yes | Password or raw AES key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.aes.decrypt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.aes.decrypt",
  "description": "Decrypts AES encrypted data",
  "signature": {
    "input": {
      "kind": "aes-encrypted-package",
      "description": "Encrypted package to decrypt",
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
      "kind": "text,binary-content",
      "description": "Resolves to the decrypted content as text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.aes.encrypt` &rarr;](/reference/slots/crypto/crypto.aes.encrypt/)

