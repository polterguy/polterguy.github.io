---
title: "[crypto.rsa.create-key]"
description: "crypto.rsa.create-key is a slot in the crypto namespace of Magic Cloud. Generates a fresh RSA key pair; returns the public key and private key as separate child nodes for storage or distribution."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.rsa.create-key/slot.json"
---

`crypto.rsa.create-key` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Generates a fresh RSA key pair; returns the public key and private key as separate child nodes for storage or distribution.

* **Returns**: Resolves to the generated RSA key pair as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[strength]` | int | no | RSA key strength in bits. Default: `2048`. |
| `[seed]` | string\|byte[] | no | Optional deterministic seed. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### JSON declaration

This is the complete declaration of `crypto.rsa.create-key`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.rsa.create-key",
  "description": "Generates a fresh RSA key pair; returns the public key and private key as separate child nodes for storage or distribution",
  "signature": {
    "children": {
      "strength": {
        "type": "int",
        "kind": "rsa-key-strength",
        "description": "RSA key strength in bits",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "2048",
        "role": "Option",
        "projection": "Value"
      },
      "seed": {
        "type": "string|byte[]",
        "kind": "crypto-seed",
        "description": "Optional deterministic seed",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
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
      "mode": "Lambda",
      "kind": "rsa-key-pair,lambda-tree",
      "description": "Resolves to the generated RSA key pair as child nodes"
    }
  }
}
```

</details>

---

[&larr; `crypto.random.int`](/reference/slots/crypto/crypto.random.int/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.rsa.decrypt` &rarr;](/reference/slots/crypto/crypto.rsa.decrypt/)

