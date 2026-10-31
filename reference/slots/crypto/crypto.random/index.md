---
title: "[crypto.random]"
description: "crypto.random is a slot in the crypto namespace of Magic Cloud. Returns a cryptographically secure random string or random bytes."
generated: true
llms: "guide"
slot_json: "/reference/slots/crypto/crypto.random/slot.json"
---

`crypto.random` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Returns a cryptographically secure random string or random bytes.

* **Returns**: Resolves to a random string, or random bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | int | no | Minimum random length. Default: `10`. |
| `[max]` | int | no | Maximum random length. |
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |
| `[seed]` | string | no | Optional deterministic seed. |

### Guide

<!-- guide -->
This slot create a bunch of random characters, or bytes for you.
The slot can optionally take a **[min]** and **[max]** argument, which defines the min/max length of the
random bytes/characters returned. If not supplied, the default values for these arguments are respectively 10 and 20.
This slot is useful for creating random secrets, and similar types of random strings, where you need cryptographically
secured random strings or byte arrays. An example of generating a cryptographically secure random string of text
between 50 and 100 characters in length can be found below.

```
crypto.random
   min:50
   max:100
```

Notice, the **[crypto.random]** slot will _only_ return characters from a-z, A-Z and 0-9. Which makes
it easily traversed using any string library. However, you can provide a **[raw]** argument, and set its
value to boolean true, at which point the slot will return the raw bytes as a `byte[]`. This has a much
larger amount of entropy than simply using alphanumeric characters for the same size - Which is
important as you start creating keys for AES cryptography operations etc.
<!-- /guide -->

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

