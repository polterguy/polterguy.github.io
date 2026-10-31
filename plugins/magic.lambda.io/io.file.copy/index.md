---
title: "How to use [io.file.copy]"
description: "How to use [io.file.copy] - Copies the specified file to the specified destination folder and file."
generated: true
guide: true
---

The reference page of [`io.file.copy`](/reference/slots/io/io.file.copy/) has its arguments, constraints and declaration.

Copies the specified file to the specified destination folder and file.
Notice, requires the destination folder to exist from before, and the source
file to exist from before. This slot will delete any previously existing destination
file, before starting the copying process. Just like the save slot, this will evaluate
the lambda children before it executes the copying of your file, allowing you to use
the results of slots as the destination path for your file.

```
io.file.copy:/misc/README.md
   .:/misc/backup/README-backup.md
```

Notice, the folder parts of the destination folder is _optional_, and if you don't supply a folder
as a part of the path, the source folder will be used by default.
