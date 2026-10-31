---
title: "How to use [io.stream.save-file]"
description: "How to use [io.stream.save-file] - Works similarly to [io.file.save] but instead of taking source content of some kind, it assumes the source is an open Stream of some sort."
generated: true
guide: true
---

This is the guide to [`io.stream.save-file`](/reference/slots/io/io.stream.save-file/), whose reference page has its arguments, constraints and declaration.

Works similarly to **[io.file.save]** but instead of taking source content of some kind,
it assumes the source is an open `Stream` of some sort.

```
/*
 * [.stream] here is an open stream, from for instance the HTTP
 * request object, or something similar that somehow is able to open
 * a stream and pass around in Hyperlambda.
 */
.stream
io.stream.save-file:/foo/bar.txt
   get-value:x:@.stream
```

After invoking the above, assuming the **[.stream]** node contains a valid `Stream`
object, the file above will contain the content from the stream.

**Notice** - If the file exists from before the existing file will be deleted, unless you
pass in an **[overwrite]** argument and set its value to false, at which point an exception
will be thrown if the file exists from before.
