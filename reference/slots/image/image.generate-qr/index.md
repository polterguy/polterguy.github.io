---
title: "[image.generate-qr]"
description: "image.generate-qr is a slot in the image namespace of Magic Cloud. Renders the supplied text or URL into a PNG QR code; commonly used for links and payment codes."
generated: true
llms: false
slot_json: "/reference/slots/image/image.generate-qr/slot.json"
---

`image.generate-qr` is a slot in the `image` namespace, in Hyperlambda, the language of Magic Cloud. Renders the supplied text or URL into a PNG QR code; commonly used for links and payment codes.

* **Value** (`qr-content,url,text`), required: Text or URL to encode in the QR code
* **Returns**: Resolves to the generated QR code image bytes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[size]` | int | no | QR module size. Default: `4`. |

Guide: [How to use [image.generate-qr]](/plugins/magic.lambda.image/#how-to-use-imagegenerate-qr)

### JSON declaration

This is the complete declaration of `image.generate-qr`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "image.generate-qr",
  "description": "Renders the supplied text or URL into a PNG QR code; commonly used for links and payment codes",
  "signature": {
    "input": {
      "kind": "qr-content,url,text",
      "description": "Text or URL to encode in the QR code",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "size": {
        "type": "int",
        "description": "QR module size",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "4",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "image,binary-content",
      "description": "Resolves to the generated QR code image bytes"
    }
  }
}
```

</details>

---

[&larr; `image.crop`](/reference/slots/image/image.crop/) | [all `image.*` slots](/reference/slots/image/) | [`image.resize` &rarr;](/reference/slots/image/image.resize/)

