---
title: "How to use [io.file.save]"
description: "How to use [io.file.save] - Saves the specified content to the specified file on disc, overwriting any previous content if the file exists from before, creating a new file if no such file already exists."
generated: true
guide: true
---

The reference page of [`io.file.save`](/reference/slots/io/io.file.save/) has its arguments, constraints and declaration.

Saves the specified content to the specified file on disc, overwriting any previous content if the
file exists from before, creating a new file if no such file already exists. The value of the first
argument will be considered the content of the file.

Notice, the node itself will be evaluated, allowing you to have other slots evaluated before slot saves
the file, to return dynamically the content of your file.

```
io.file.save:/misc/README2.md
   .:This is new content for file
```

**Notice** - If you want to save binary content you should use the **[io.file.save.binary]** override.
