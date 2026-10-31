---
title: magic.lambda.image
moved_anchors: {"how-to-use-imagechart": "/plugins/magic.lambda.image/image.chart/", "how-to-use-imageconvert": "/plugins/magic.lambda.image/image.convert/", "how-to-use-imagecrop": "/plugins/magic.lambda.image/image.crop/", "how-to-use-imagegenerate-qr": "/plugins/magic.lambda.image/image.generate-qr/", "how-to-use-imageresize": "/plugins/magic.lambda.image/image.resize/"}
---

The magic.lambda.image project contains image manipulation functions for Hyperlambda, allowing you to do basic
manipulation of images, in addition to generating QR codes. More specifically this project contains the following slot.

* __[\[image.generate-qr\]](/reference/slots/image/image.generate-qr/)__ - Generate a QR code with the specified payload
* __[\[image.size\]](/reference/slots/image/image.size/)__ - Returns the width and height of the specified image
* __[\[image.resize\]](/reference/slots/image/image.resize/)__ - Resizes the specified image
* __[\[image.convert\]](/reference/slots/image/image.convert/)__ - Converts the specified image to another format
* __[\[image.crop\]](/reference/slots/image/image.crop/)__ - Crops the specified image
* __[\[image.chart\]](/reference/slots/image/image.chart/)__ - Creates a chart


## Transforming images

All image transformation slots works similarly. They can either be given a string being the relative filename
of the image you want to transform, or a stream from where to load the image. All transformation slots can
also be given a **[type]** argument, which is how to return the image after the transformation is done. Supported
types are as follows.

* png
* jpeg
* bmp
* gif
* tga
* pbm
* tiff
* webp

In addition you can provide a **[dest]** argument, which if specified, becomes the relative path of where to
save the image after transformation has been applied. If not specified, the image will be returned as a stream
to caller, otherwise the image will be saved to the specified file.
