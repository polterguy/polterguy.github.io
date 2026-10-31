---
title: "How to use [io.folder.list-recursively]"
description: "How to use [io.folder.list-recursively] - This slot works like [io.folder.list], except it also returns all folders nested inside of the specified folder, at any depth, and not only its direct sub folders."
generated: true
guide: true
---

The reference page of [`io.folder.list-recursively`](/reference/slots/io/io.folder.list-recursively/) has its arguments, constraints and declaration.

This slot works like **[io.folder.list]**, except it also returns all folders nested inside of the specified folder,
at any depth, and not only its direct sub folders. It returns one unnamed child node per folder, with the folder's
path relative to the root folder of your backend, and accepts the following optional arguments.

* **[display-hidden]** - Boolean, defaults to false, which hides folders starting with a `.`
* **[display-system]** - Boolean, defaults to true, and if false hides folders inside of _"/system/"_, _"/misc/"_, _"/data/"_ and _"/config/"_

This slot lists every folder below a folder, at any depth, as child nodes holding the path of each folder. Folders whose names start with a dot are left out unless you set **[display-hidden]** to true, and you can leave out the _"/system/"_, _"/misc/"_, _"/data/"_ and _"/config/"_ folders by setting **[display-system]** to false. Below is an example.

```
io.folder.list-recursively:/misc/
```
