---
title: "[crypto.random.int]"
description: "crypto.random.int is a slot in the crypto namespace of Magic Cloud. Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound."
generated: true
llms: "guide"
slot_json: "/reference/slots/crypto/crypto.random.int/slot.json"
---

`crypto.random.int` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Returns a cryptographically secure random integer; use the optional [max] to cap the upper bound.

* **Returns**: Resolves to a random integer less than the optional [max] value

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Exclusive maximum integer. Default: `int.MaxValue`. |
| `[seed]` | string | no | Optional deterministic seed. |

### Guide

<!-- guide -->
This slot create a random integer value for you using a CSRNG generator.
The slot can optionally take a **[max]** argument, which defines the maximum value it will return.
This slot is useful for creating random integers where you need cryptographically
secured random values. An example of generating a cryptographically secure random string integer
with a maximum value of 1024 can be found below.

```
crypto.random.int
   max:1024
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) plugin, which documents every slot it contains.

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

