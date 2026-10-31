---
title: "How to use [io.file.list-recursively]"
description: "How to use [io.file.list-recursively] - This slot works like [io.file.list], except it also returns all files inside of nested folders, at any depth, and not only the files directly inside of the specified folder."
generated: true
guide: true
---

The reference page of [`io.file.list-recursively`](/reference/slots/io/io.file.list-recursively/) has its arguments, constraints and declaration.

This slot works like **[io.file.list]**, except it also returns all files inside of nested folders, at any depth, and
not only the files directly inside of the specified folder. It returns one unnamed child node per file, with the
file's path relative to the root folder of your backend, and accepts the following optional arguments.

* **[display-hidden]** - Boolean, defaults to false, which hides files starting with a `.`
* **[display-system]** - Boolean, defaults to true, and if false hides files inside of _"/system/"_, _"/misc/"_, _"/data/"_ and _"/config/"_

This slot lists every file in a folder and in all of its subfolders, as child nodes holding the path of each file. Hidden files and system folders are left out unless you set **[display-hidden]** or **[display-system]**. Below is an example.

```
io.file.list-recursively:/misc/
```
