---
title: "How to use [io.folder.list-recursively]"
description: "How to use [io.folder.list-recursively] - This slot works like [io.folder.list], except it also returns all folders nested inside of the specified folder, at any depth, and not only its direct sub folders."
generated: true
guide: true
---

This is the guide to [`io.folder.list-recursively`](/reference/slots/io/io.folder.list-recursively/), whose reference page has its arguments, constraints and declaration.

This slot works like **[io.folder.list]**, except it also returns all folders nested inside of the specified folder,
at any depth, and not only its direct sub folders. It returns one unnamed child node per folder, with the folder's
path relative to the root folder of your backend, and accepts the following optional arguments.

* **[display-hidden]** - Boolean, defaults to false, which hides folders starting with a `.`
* **[display-system]** - Boolean, defaults to true, and if false hides folders inside of _"/system/"_, _"/misc/"_, _"/data/"_ and _"/config/"_
