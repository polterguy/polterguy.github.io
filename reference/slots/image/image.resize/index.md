---
title: "[image.resize]"
description: "image.resize is a slot in the image namespace of Magic Cloud. Resizes an image to the specified width and height; useful for generating thumbnails or fitting screen sizes."
generated: true
llms: false
slot_json: "/reference/slots/image/image.resize/slot.json"
---

`image.resize` is a slot in the `image` namespace, in Hyperlambda, the language of Magic Cloud. Resizes an image to the specified width and height; useful for generating thumbnails or fitting screen sizes.

* **Value** (`image-file`), required: Source image filename or stream to resize
* **Returns**: Resolves to the resized image stream unless [dest] is supplied, in which case the resized image is saved to disk and nothing is returned

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream. |
| `[height]` | int | no | Target height in pixels. |
| `[type]` | string | no | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp. Default: `png`. |
| `[width]` | int | no | Target width in pixels. |

Guide: [How to use [image.resize]](/plugins/magic.lambda.image/#how-to-use-imageresize)

### JSON declaration

This is the complete declaration of `image.resize`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "image.resize",
  "description": "Resizes an image to the specified width and height; useful for generating thumbnails or fitting screen sizes",
  "signature": {
    "input": {
      "kind": "image-file",
      "description": "Source image filename or stream to resize",
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
      "width": {
        "type": "int",
        "kind": "image-dimensions",
        "description": "Target width in pixels",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "height": {
        "type": "int",
        "kind": "image-dimensions",
        "description": "Target height in pixels",
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
      "description": "Resolves to the resized image stream unless [dest] is supplied, in which case the resized image is saved to disk and nothing is returned"
    }
  }
}
```

</details>

---

[&larr; `image.generate-qr`](/reference/slots/image/image.generate-qr/) | [all `image.*` slots](/reference/slots/image/) | [`image.size` &rarr;](/reference/slots/image/image.size/)

