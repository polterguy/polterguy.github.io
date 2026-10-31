---
title: "How to use [magic.io.file.load-recursively]"
description: "How to use [magic.io.file.load-recursively] - This slot loads all files recursively within the specified folder, and returns their filenames and their content."
guide: true
slots: ["magic.io.file.load-recursively"]
---

This slot loads _all_ files recursively within the specified folder, and returns their filenames _and_ their
content. The following example Hyperlambda illustrates its usage.

```
signal:magic.io.file.load-recursively
   .:/modules/
```

The above will result in something resembling the following. Notice, the result below has been _significantly_ snippet.

```
signal
   :/modules/README.md
      :"\n# Your modules folder\n\nThis ... snip ...\n"
   :/modules/magic/crypto_invocations-count.get.hl
      :@"..."
```

As you can see above the result is an array of filenames, where each filename has one child node, being the actual
content of the file. The slot is used when for instance a frontend application is being generated based upon a
template - In addition when you download a folder or something similar.
