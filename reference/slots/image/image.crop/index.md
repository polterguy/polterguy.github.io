---
title: "[image.crop]"
description: "image.crop is a slot in the image namespace of Magic Cloud. Cuts a rectangular region out of an image at the given x, y, width, and height."
generated: true
llms: false
slot_json: "/reference/slots/image/image.crop/slot.json"
---

`image.crop` is a slot in the `image` namespace, in Hyperlambda, the language of Magic Cloud. Cuts a rectangular region out of an image at the given x, y, width, and height.

* **Value** (`image-file`), required: Source image filename or stream to crop
* **Returns**: Resolves to the cropped image stream unless [dest] is supplied, in which case the cropped image is saved to disk and nothing is returned

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | no | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp. Default: `png`. |
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream. |
| `[left]` | int | no | Pixels to crop from the left edge. Default: `0`. |
| `[top]` | int | no | Pixels to crop from the top edge. Default: `0`. |
| `[right]` | int | no | Pixels to crop from the right edge. Default: `0`. |
| `[bottom]` | int | no | Pixels to crop from the bottom edge. Default: `0`. |

### Guide

[How to use `image.crop`](/plugins/magic.lambda.image/image.crop/)

### JSON declaration

This is the complete declaration of `image.crop`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "image.crop",
  "description": "Cuts a rectangular region out of an image at the given x, y, width, and height",
  "signature": {
    "input": {
      "kind": "image-file",
      "description": "Source image filename or stream to crop",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "type": {
        "type": "string",
        "kind": "image-format",
        "description": "Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
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
      },
      "left": {
        "type": "int",
        "kind": "image-crop-pixels",
        "description": "Pixels to crop from the left edge",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "top": {
        "type": "int",
        "kind": "image-crop-pixels",
        "description": "Pixels to crop from the top edge",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "right": {
        "type": "int",
        "kind": "image-crop-pixels",
        "description": "Pixels to crop from the right edge",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "bottom": {
        "type": "int",
        "kind": "image-crop-pixels",
        "description": "Pixels to crop from the bottom edge",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "image",
      "description": "Resolves to the cropped image stream unless [dest] is supplied, in which case the cropped image is saved to disk and nothing is returned"
    }
  }
}
```

</details>

---

[&larr; `image.convert`](/reference/slots/image/image.convert/) | [all `image.*` slots](/reference/slots/image/) | [`image.generate-qr` &rarr;](/reference/slots/image/image.generate-qr/)

