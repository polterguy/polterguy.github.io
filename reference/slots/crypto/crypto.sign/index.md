---
title: "[crypto.sign]"
description: "crypto.sign is a slot in the crypto namespace of Magic Cloud. Signs data using the configured combination algorithm."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.sign/slot.json"
---

`crypto.sign` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Signs data using the configured combination algorithm.

* **Value** (`text,binary-content`), required: Content to sign
* **Returns**: Resolves to the signed package as base64 text or raw bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[signing-key]` | string\|byte[] | yes | Private signing key. |
| `[signing-key-fingerprint]` | string\|byte[] | yes | Fingerprint for the signing key. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.sign`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.sign",
  "description": "Signs data using the configured combination algorithm",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "Content to sign",
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
      }
    },
    "output": {
      "mode": "Value",
      "kind": "crypto-signature,fingerprint-source,text",
      "description": "Resolves to the signed package as base64 text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.seed`](/reference/slots/crypto/crypto.seed/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.verify` &rarr;](/reference/slots/crypto/crypto.verify/)

