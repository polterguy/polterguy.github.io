---
title: "[crypto.random.int]"
description: "crypto.random.int is a slot in the crypto namespace of Magic Cloud. Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.random.int/slot.json"
---

`crypto.random.int` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound.

* **Returns**: Resolves to a random integer less than the optional [max] value

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Exclusive maximum integer. Default: `int.MaxValue`. |
| `[seed]` | string | no | Optional deterministic seed. |

Guide: [How to use [crypto.random.int]](/plugins/magic.lambda.crypto/#how-to-use-cryptorandomint)

### JSON declaration

This is the complete declaration of `crypto.random.int`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.random.int",
  "description": "Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound",
  "signature": {
    "children": {
      "max": {
        "type": "int",
        "description": "Exclusive maximum integer",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "int.MaxValue",
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
      "kind": "random-number,integer,number",
      "description": "Resolves to a random integer less than the optional [max] value"
    }
  }
}
```

</details>

---

[&larr; `crypto.random`](/reference/slots/crypto/crypto.random/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.rsa.create-key` &rarr;](/reference/slots/crypto/crypto.rsa.create-key/)

