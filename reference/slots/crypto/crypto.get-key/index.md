---
title: "[crypto.get-key]"
description: "crypto.get-key is a slot in the crypto namespace of Magic Cloud. Returns or derives a cryptographic key."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.get-key/slot.json"
---

`crypto.get-key` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Returns or derives a cryptographic key.

* **Value** (`crypto-encrypted-package`), required: Encrypted package to extract the key fingerprint from
* **Returns**: Resolves to the package key fingerprint as text or raw bytes when [raw] is true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to return raw bytes instead of encoded text. Default: `false`. |

### Guide

[How to use `crypto.get-key`](/plugins/magic.lambda.crypto/crypto.get-key/)

### JSON declaration

This is the complete declaration of `crypto.get-key`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.get-key",
  "description": "Returns or derives a cryptographic key",
  "signature": {
    "input": {
      "kind": "crypto-encrypted-package",
      "description": "Encrypted package to extract the key fingerprint from",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
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
      "kind": "crypto-key-fingerprint",
      "description": "Resolves to the package key fingerprint as text or raw bytes when [raw] is true"
    }
  }
}
```

</details>

---

[&larr; `crypto.fingerprint`](/reference/slots/crypto/crypto.fingerprint/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.hash` &rarr;](/reference/slots/crypto/crypto.hash/)

