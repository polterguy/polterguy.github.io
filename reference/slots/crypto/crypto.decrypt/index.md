---
title: "[crypto.decrypt]"
description: "crypto.decrypt is a slot in the crypto namespace of Magic Cloud. Decrypts data using the configured combination algorithm."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.decrypt/slot.json"
---

`crypto.decrypt` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Decrypts data using the configured combination algorithm.

* **Value** (`crypto-encrypted-package`), required: Encrypted package to decrypt and optionally verify
* **Returns**: Resolves to the decrypted content as text or raw bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[decryption-key]` | string\|byte[] | yes | Private decryption key. |
| `[verification-key]` | string\|byte[] | yes | Public key used to verify the signature. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### Related documentation

* Part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) plugin, which documents every slot it contains.
* Discussed in [Combining RSA and AES cryptography](/plugins/magic.lambda.crypto/combining-rsa-and-aes-cryptography/).

### JSON declaration

This is the complete declaration of `crypto.decrypt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.decrypt",
  "description": "Decrypts data using the configured combination algorithm",
  "signature": {
    "input": {
      "kind": "crypto-encrypted-package",
      "description": "Encrypted package to decrypt and optionally verify",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "decryption-key": {
        "type": "string|byte[]",
        "kind": "crypto-private-key",
        "description": "Private decryption key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "verification-key": {
        "type": "string|byte[]",
        "kind": "crypto-public-key",
        "description": "Public key used to verify the signature",
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

[&larr; `crypto.aes.encrypt`](/reference/slots/crypto/crypto.aes.encrypt/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.encrypt` &rarr;](/reference/slots/crypto/crypto.encrypt/)

