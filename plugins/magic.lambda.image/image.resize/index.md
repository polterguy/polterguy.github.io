---
title: "How to use [image.resize]"
description: "How to use [image.resize] - Resizing an image can be done as follows."
generated: true
guide: true
---

The reference page of [`image.resize`](/reference/slots/image/image.resize/) has its arguments, constraints and declaration.

Resizing an image can be done as follows.

```
image.resize:/some-image.png
   height:250
   type:png
```

The above will resize the specified image to a width of 250 pixel, converting it to PNG, while keeping the
aspect ratio by calculating the new height automatically. You can provide either of.

* __[width]__ - New width, between 1 and 8192 pixels
* __[height]__ - New height, between 1 and 8192 pixels

You can provide both of the above, but at least one of the above _must_ be specified. If one of the values are
omitted, it will be calculated by keeping the aspect ratio of the image as is. The **[type]** argument is how
to return the image after the transformation has been applied, and can be any of the supported types as specified
above. Notice, the image might be stretched in one direction if you change the existing width and height ratio
during the transformation.
