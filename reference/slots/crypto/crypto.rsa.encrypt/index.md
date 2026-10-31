---
title: "[crypto.rsa.encrypt]"
description: "crypto.rsa.encrypt is a slot in the crypto namespace of Magic Cloud. Encrypts data using RSA."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.rsa.encrypt/slot.json"
---

`crypto.rsa.encrypt` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Encrypts data using RSA.

* **Value** (`text,binary-content`), required: Content to encrypt
* **Returns**: Resolves to the encrypted package as base64 text or raw bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[public-key]` | string\|byte[] | yes | Public key for the RSA operation. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### Related documentation

* Part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) plugin, which documents every slot it contains.
* Discussed in [RSA cryptography with Hyperlambda](/plugins/magic.lambda.crypto/rsa/).

### JSON declaration

This is the complete declaration of `crypto.rsa.encrypt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.rsa.encrypt",
  "description": "Encrypts data using RSA",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "Content to encrypt",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "public-key": {
        "type": "string|byte[]",
        "kind": "rsa-public-key",
        "description": "Public key for the RSA operation",
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
      "kind": "rsa-encrypted-package,fingerprint-source",
      "description": "Resolves to the encrypted package as base64 text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.rsa.decrypt`](/reference/slots/crypto/crypto.rsa.decrypt/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.rsa.sign` &rarr;](/reference/slots/crypto/crypto.rsa.sign/)

