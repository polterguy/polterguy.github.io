---
title: "How to use [io.file.load-recursively]"
description: "How to use [io.file.load-recursively] - This slot loads the content of all files inside of the specified folder, including all nested folders, as text, and takes no arguments besides the folder as its value."
generated: true
guide: true
---

The reference page of [`io.file.load-recursively`](/reference/slots/io/io.file.load-recursively/) has its arguments, constraints and declaration.

This slot loads the content of all files inside of the specified folder, including all nested folders, as text, and
takes no arguments besides the folder as its value. It returns one unnamed child node per file, and each of these nodes
has the following two children.

* **[name]** - Path of the file relative to the root folder of your backend
* **[content]** - Content of the file as a string, decoded as UTF-8

As with **[io.file.load]**, you should not use this slot on binary files.

This slot loads every file in a folder and its subfolders, and returns one child node per file, holding its path and content. Below is an example.

```
io.file.load-recursively:/misc/snippets/
```
