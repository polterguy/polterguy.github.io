---
title: "[crypto.rsa.decrypt]"
description: "crypto.rsa.decrypt is a slot in the crypto namespace of Magic Cloud. Decrypts RSA encrypted data."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.rsa.decrypt/slot.json"
---

`crypto.rsa.decrypt` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Decrypts RSA encrypted data.

* **Value** (`rsa-encrypted-package`), required: Encrypted package to decrypt
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[private-key]` | string\|byte[] | yes | Private key for the RSA operation. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.rsa.decrypt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.rsa.decrypt",
  "description": "Decrypts RSA encrypted data",
  "signature": {
    "input": {
      "kind": "rsa-encrypted-package",
      "description": "Encrypted package to decrypt",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "private-key": {
        "type": "string|byte[]",
        "kind": "rsa-private-key",
        "description": "Private key for the RSA operation",
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

[&larr; `crypto.rsa.create-key`](/reference/slots/crypto/crypto.rsa.create-key/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.rsa.encrypt` &rarr;](/reference/slots/crypto/crypto.rsa.encrypt/)

