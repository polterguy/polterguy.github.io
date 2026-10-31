---
title: "How to use [io.stream.read]"
description: "How to use [io.stream.read] - Works similarly to [io.file.load] but instead of taking a source filename of some kind, it assumes the source is an open Stream of some sort."
generated: true
guide: true
---

The reference page of [`io.stream.read`](/reference/slots/io/io.stream.read/) has its arguments, constraints and declaration.

Works similarly to **[io.file.load]** but instead of taking a source filename of some kind,
it assumes the source is an open `Stream` of some sort.

```
/*
 * [.stream] here is an open stream, from for instance the HTTP
 * request object, or something similar.
 */
.stream
io.stream.read:x:@.stream
```
