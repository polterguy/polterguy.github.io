---
title: magic.lambda.image slot reference
description: Every slot in magic.lambda.image with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.image](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.image). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.image](/plugins/magic.lambda.image/)._

## [image.chart]

Renders a bar, stacked, or grouped chart from the supplied series data as a PNG image.

* **Value** (`chart-type`), required: Chart type to create, such as bars, stacked, or grouped
* **Returns**: Resolves to the generated chart image bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[width]` | int | yes | Chart width in pixels |
| `[height]` | int | yes | Chart height in pixels |
| `[filename]` | string | no | Optional destination filename |
| `[bars]` | lambda | yes | Chart values keyed by label; grouped and stacked charts use nested numeric values |
| `[legend]` | lambda | no | Legend labels required by grouped and stacked charts |

Guide: [How to use [image.chart]](/plugins/magic.lambda.image/#how-to-use-imagechart)

## [image.convert]

Re-encodes an image into a different format (e.g. PNG to JPEG) preserving its pixel content.

* **Value** (`image-file`), required: Source image filename or stream to convert
* **Returns**: Resolves to the converted image stream unless [dest] is supplied, in which case the converted image is saved to disk and nothing is returned

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | no | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp |
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream |

Guide: [How to use [image.convert]](/plugins/magic.lambda.image/#how-to-use-imageconvert)

## [image.crop]

Cuts a rectangular region out of an image at the given x, y, width, and height.

* **Value** (`image-file`), required: Source image filename or stream to crop
* **Returns**: Resolves to the cropped image stream unless [dest] is supplied, in which case the cropped image is saved to disk and nothing is returned

| Argument | Type | Required | Description |
|---|---|---|---|
| `[left]` | int | no | Pixels to crop from the left edge |
| `[top]` | int | no | Pixels to crop from the top edge |
| `[right]` | int | no | Pixels to crop from the right edge |
| `[bottom]` | int | no | Pixels to crop from the bottom edge |

Guide: [How to use [image.crop]](/plugins/magic.lambda.image/#how-to-use-imagecrop)

## [image.generate-qr]

Renders the supplied text or URL into a PNG QR code; commonly used for links and payment codes.

* **Value** (`qr-content,url,text`), required: Text or URL to encode in the QR code
* **Returns**: Resolves to the generated QR code image bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[size]` | int | no | QR module size |

Guide: [How to use [image.generate-qr]](/plugins/magic.lambda.image/#how-to-use-imagegenerate-qr)

## [image.resize]

Resizes an image to the specified width and height; useful for generating thumbnails or fitting screen sizes.

* **Value** (`image-file`), required: Source image filename or stream to resize
* **Returns**: Resolves to the resized image stream unless [dest] is supplied, in which case the resized image is saved to disk and nothing is returned

| Argument | Type | Required | Description |
|---|---|---|---|
| `[width]` | int | no | Target width in pixels |
| `[height]` | int | no | Target height in pixels |

Guide: [How to use [image.resize]](/plugins/magic.lambda.image/#how-to-use-imageresize)

## [image.size]

Returns the width and height of an image.

* **Value** (`image-file`), required: Image filename to inspect
* **Returns**: Returns [width:int] and [height:int] child nodes for the image dimensions

