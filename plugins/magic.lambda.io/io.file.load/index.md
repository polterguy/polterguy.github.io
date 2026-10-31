---
title: "How to use [io.file.load]"
description: "How to use [io.file.load] - Loads the specified text file from disc."
generated: true
guide: true
---

The reference page of [`io.file.load`](/reference/slots/io/io.file.load/) has its arguments, constraints and declaration.

Loads the specified text file from disc. This slot can _only load text files_. Or to be specific,
there are no ways you can change binary files, hence loading a binary file is for the most parts
not something you should do. Although there _might_ exist exceptions to this.

```
io.file.load:/misc/README.md
```

**Notice** - If you want to load binary content you should use the **[io.file.load.binary]** override.
