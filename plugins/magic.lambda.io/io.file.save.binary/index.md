---
title: "How to use [io.file.save.binary]"
description: "How to use [io.file.save.binary] - This slot saves raw bytes as a file."
generated: true
guide: true
---

The reference page of [`io.file.save.binary`](/reference/slots/io/io.file.save.binary/) has its arguments, constraints and declaration.

This slot saves raw bytes as a file. The first child node supplies the content, which must be bytes. Below is an example, copying an image.

```
io.file.load.binary:/misc/logo.png
io.file.save.binary:/misc/logo-copy.png
   .:x:@io.file.load.binary
```
