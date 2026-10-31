---
title: image.* slots
description: The 6 slots named image.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [image.chart]

Renders a bar, stacked, or grouped chart from the supplied series data as a PNG image.

* **Value** (`chart-type`), required: Chart type to create, such as bars, stacked, or grouped
* **Returns**: Resolves to the generated chart image bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[width]` | int | yes | Chart width in pixels. |
| `[height]` | int | yes | Chart height in pixels. |
| `[filename]` | string | no | Optional destination filename. |
| `[bars]` | lambda | yes | Chart values keyed by label; grouped and stacked charts use nested numeric values. |
| `[bars]` / _any node name_ | double\|lambda | yes | Bar value or grouped/stacked bar value collection. Can be repeated. |
| `[legend]` | lambda | no | Legend labels required by grouped and stacked charts. |
| `[legend]` / _unnamed child node_ | string | no | Legend label. Can be repeated. |

Guide: [How to use [image.chart]](/plugins/magic.lambda.image/#how-to-use-imagechart)

## [image.convert]

Re-encodes an image into a different format (e.g. PNG to JPEG) preserving its pixel content.

* **Value** (`image-file`), required: Source image filename or stream to convert
* **Returns**: Resolves to the converted image stream unless [dest] is supplied, in which case the converted image is saved to disk and nothing is returned

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | yes | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp. Default: `png`. |
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream. |

Guide: [How to use [image.convert]](/plugins/magic.lambda.image/#how-to-use-imageconvert)

## [image.crop]

Cuts a rectangular region out of an image at the given x, y, width, and height.

* **Value** (`image-file`), required: Source image filename or stream to crop
* **Returns**: Resolves to the cropped image stream unless [dest] is supplied, in which case the cropped image is saved to disk and nothing is returned

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | no | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp. Default: `png`. |
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream. |
| `[left]` | int | no | Pixels to crop from the left edge. Default: `0`. |
| `[top]` | int | no | Pixels to crop from the top edge. Default: `0`. |
| `[right]` | int | no | Pixels to crop from the right edge. Default: `0`. |
| `[bottom]` | int | no | Pixels to crop from the bottom edge. Default: `0`. |

Guide: [How to use [image.crop]](/plugins/magic.lambda.image/#how-to-use-imagecrop)

## [image.generate-qr]

Renders the supplied text or URL into a PNG QR code; commonly used for links and payment codes.

* **Value** (`qr-content,url,text`), required: Text or URL to encode in the QR code
* **Returns**: Resolves to the generated QR code image bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[size]` | int | no | QR module size. Default: `4`. |

Guide: [How to use [image.generate-qr]](/plugins/magic.lambda.image/#how-to-use-imagegenerate-qr)

## [image.resize]

Resizes an image to the specified width and height; useful for generating thumbnails or fitting screen sizes.

* **Value** (`image-file`), required: Source image filename or stream to resize
* **Returns**: Resolves to the resized image stream unless [dest] is supplied, in which case the resized image is saved to disk and nothing is returned

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | no | Output image format: png, jpeg, bmp, gif, tga, pbm, tiff, or webp. Default: `png`. |
| `[dest]` | string | no | Optional destination filename; when supplied, the image is saved to disk instead of returned as a stream. |
| `[width]` | int | no | Target width in pixels. |
| `[height]` | int | no | Target height in pixels. |

Guide: [How to use [image.resize]](/plugins/magic.lambda.image/#how-to-use-imageresize)

## [image.size]

Returns the width and height of an image.

* **Value** (`image-file`), required: Image filename to inspect
* **Returns**: Returns [width:int] and [height:int] child nodes for the image dimensions

