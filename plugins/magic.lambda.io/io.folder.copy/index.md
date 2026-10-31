---
title: "How to use [io.folder.copy]"
description: "How to use [io.folder.copy] - Copies the specified source folder to its specified destination folder."
generated: true
guide: true
---

This is the guide to [`io.folder.copy`](/reference/slots/io/io.folder.copy/), whose reference page has its arguments, constraints and declaration.

Copies the specified source folder to its specified destination folder. Notice, this slot doesn't copy
the folder itself, but rather the folder's content. Below is an example.

```
io.folder.copy:/misc/source-folder/
   .:/misc/destination-folder/
```

After invocation of the above, every single file and folder inside your _"source-folder"_ can now
be found as a copy inside your _"destination-folder"_.
