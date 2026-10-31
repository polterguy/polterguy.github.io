---
title: "[crypto.random]"
description: "crypto.random is a slot in the crypto namespace of Magic Cloud. Returns a cryptographically secure random string or random bytes."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.random/slot.json"
---

`crypto.random` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Returns a cryptographically secure random string or random bytes.

* **Returns**: Resolves to a random string, or random bytes when [raw] is true

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Maximum random length. |
| `[min]` | int | no | Minimum random length. Default: `10`. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |
| `[seed]` | string | no | Optional deterministic seed. |

Guide: [How to use [crypto.random]](/plugins/magic.lambda.crypto/#how-to-use-cryptorandom)

### JSON declaration

This is the complete declaration of `crypto.random`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.random",
  "description": "Returns a cryptographically secure random string or random bytes",
  "signature": {
    "children": {
      "min": {
        "type": "int",
        "description": "Minimum random length",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "10",
        "role": "Option",
        "projection": "Value"
      },
      "max": {
        "type": "int",
        "description": "Maximum random length",
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
      },
      "seed": {
        "type": "string",
        "kind": "crypto-seed",
        "description": "Optional deterministic seed",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "random-content,binary-content",
      "description": "Resolves to a random string, or random bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.password.verify`](/reference/slots/crypto/crypto.password.verify/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.random.int` &rarr;](/reference/slots/crypto/crypto.random.int/)

