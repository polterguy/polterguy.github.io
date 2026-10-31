---
title: "[crypto.fingerprint]"
description: "crypto.fingerprint is a slot in the crypto namespace of Magic Cloud. Returns a SHA256 fingerprint of the input, formatted as colon-separated hex; useful for identifying public keys."
generated: true
llms: false
slot_json: "/reference/slots/crypto/crypto.fingerprint/slot.json"
---

`crypto.fingerprint` is a slot in the `crypto` namespace, in Hyperlambda, the language of Magic Cloud. Returns a SHA256 fingerprint of the input, formatted as colon-separated hex; useful for identifying public keys.

* **Value** (`fingerprint-source`), required: Base64 encoded content or raw byte[] content to fingerprint
* **Returns**: Resolves to the SHA256 hash of the supplied content formatted as a fingerprint

### Related documentation

* Part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `crypto.fingerprint`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "crypto.fingerprint",
  "description": "Returns a SHA256 fingerprint of the input, formatted as colon-separated hex; useful for identifying public keys",
  "signature": {
    "input": {
      "kind": "fingerprint-source",
      "description": "Base64 encoded content or raw byte[] content to fingerprint",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "fingerprint,text",
      "description": "Resolves to the SHA256 hash of the supplied content formatted as a fingerprint"
    }
  }
}
```

</details>

---

[&larr; `crypto.encrypt`](/reference/slots/crypto/crypto.encrypt/) | [all `crypto.*` slots](/reference/slots/crypto/) | [`crypto.get-key` &rarr;](/reference/slots/crypto/crypto.get-key/)

