---
title: "How to use [io.path.get-folder]"
description: "How to use [io.path.get-folder] - Strips the filename from a path and returns the folder part of it, always ending with a /."
generated: true
guide: true
---

The reference page of [`io.path.get-folder`](/reference/slots/io/io.path.get-folder/) has its arguments, constraints and declaration.

Strips the filename from a path and returns the folder part of it, always ending with a `/`. If the path already
ends with a `/` it is returned as it is. Below is an example.

```
io.path.get-folder:/foo/howdy/file.hl
```

The above returns `/foo/howdy/`, and the same is returned if you pass in `/foo/howdy/` instead.
