---
title: "[crypto.verify]"
description: "crypto.verify is a slot in the crypto namespace of Magic Cloud. Verifies a signature using the configured combination algorithm."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.verify/slot.json"
---

`crypto.verify` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Verifies a signature using the configured combination algorithm.

* **Value** (`crypto-signature`), required: Signed package to verify
* **Returns**: Resolves to the verified content as text or raw bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[verification-key]` | string\|byte[] | yes | Public key used to verify the signature. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.verify`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.verify",
  "description": "Verifies a signature using the configured combination algorithm",
  "signature": {
    "input": {
      "kind": "crypto-signature",
      "description": "Signed package to verify",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
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
      "description": "Resolves to the verified content as text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.sign`](/reference/slots/crypto/crypto.sign/) | [all `crypto.*` slots](/reference/slots/crypto/)

