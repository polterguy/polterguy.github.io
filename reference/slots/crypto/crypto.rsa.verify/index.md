---
title: "[crypto.rsa.verify]"
description: "crypto.rsa.verify is a slot in the crypto namespace of Magic Cloud. Verifies an RSA signature."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.rsa.verify/slot.json"
---

`crypto.rsa.verify` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Verifies an RSA signature.

* **Value** (`text,binary-content`), required: Content to verify against the supplied signature

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[signature]` | string\|byte[] | yes | RSA signature to verify. |
| `[public-key]` | string\|byte[] | yes | Public key used to verify the signature. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.rsa.verify`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.rsa.verify",
  "description": "Verifies an RSA signature",
  "signature": {
    "input": {
      "kind": "text,binary-content",
      "description": "Content to verify against the supplied signature",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "signature": {
        "type": "string|byte[]",
        "kind": "rsa-signature",
        "description": "RSA signature to verify",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "public-key": {
        "type": "string|byte[]",
        "kind": "rsa-public-key",
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
    }
  }
}
```

</details>

---

[&larr; `crypto.rsa.sign`](/reference/slots/crypto/crypto.rsa.sign/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.seed` &rarr;](/reference/slots/crypto/crypto.seed/)

