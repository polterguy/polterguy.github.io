---
title: "How to use [image.crop]"
description: "How to use [image.crop] - To crop an image you specify the following arguments."
generated: true
guide: true
---

The reference page of [`image.crop`](/reference/slots/image/image.crop/) has its arguments, constraints and declaration.

To crop an image you specify the following arguments.

* __[left]__ - Pixels to remove from the left parts of image
* __[top]__ - Pixels to remove from the top parts of image
* __[right]__ - Pixels to remove from the right parts of image
* __[bottom]__ - Pixels to remove from the bottom parts of image

Notice, left + right must be smaller than the total width of the image, and top + bottom must be smaller
than the total height of the image. All arguments are optional, allowing you to only crop an image at one
side, such as for instance illustrated below.

```
image.crop:/modules/test/qr.png
   right:50
```
