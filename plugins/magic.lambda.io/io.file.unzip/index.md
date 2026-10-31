---
title: "How to use [io.file.unzip]"
description: "How to use [io.file.unzip] - Unzips a ZIP file. Notice, the [folder] argument is optional, and the current folder of the ZIP file you're unzipping will be used if no [folder] argument is given."
generated: true
guide: true
---

This is the guide to [`io.file.unzip`](/reference/slots/io/io.file.unzip/), whose reference page has its arguments, constraints and declaration.

Unzips a ZIP file. Notice, the **[folder]** argument is optional, and the current folder
of the ZIP file you're unzipping will be used if no **[folder]** argument is given.

```
io.file.unzip:/misc/foo.zip
   folder:/misc/backup/
```

Optionally provide **[overwrite]** argument and set its value to boolean true if you want the operation to
overwrite any existing files in the destination folder. Otherwise the operation will throw an exception
if any of the files exists from before.
