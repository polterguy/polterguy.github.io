---
title: "[image.convert]"
description: "image.convert is a slot in the image namespace of Magic Cloud. Re-encodes an image into a different format (e.g. PNG to JPEG) preserving its pixel content."
generated: true
llms: false
slot_json: "/reference/slots/image/image.convert/slot.json"
---

`image.convert` is a slot in the `image` namespace, in Hyperlambda, the language of Magic Cloud. Re-encodes an image into a different format (e.g. PNG to JPEG) preserving its pixel content.

* **Value** (`image-file`), required: Source image filename or stream to convert
* **Returns**: Resolves to the converted image stream unless [dest] is supplied, in which case the converted image is saved to disk and nothing is returned

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream. |
| `[type]` | string | yes | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp. Default: `png`. |

Guide: [How to use [image.convert]](/plugins/magic.lambda.image/#how-to-use-imageconvert)

### JSON declaration

This is the complete declaration of `image.convert`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "image.convert",
  "description": "Re-encodes an image into a different format (e.g. PNG to JPEG) preserving its pixel content",
  "signature": {
    "input": {
      "kind": "image-file",
      "description": "Source image filename or stream to convert",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "type": {
        "type": "string",
        "kind": "image-format",
        "description": "Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "default": "png",
        "role": "Option",
        "projection": "Value"
      },
      "dest": {
        "type": "string",
        "kind": "image-file",
        "description": "Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "image",
      "description": "Resolves to the converted image stream unless [dest] is supplied, in which case the converted image is saved to disk and nothing is returned"
    }
  }
}
```

</details>

---

[&larr; `image.chart`](/reference/slots/image/image.chart/) | [all `image.*` slots](/reference/slots/image/) | [`image.crop` &rarr;](/reference/slots/image/image.crop/)

