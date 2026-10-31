---
title: "How to use [io.stream.open-file]"
description: "How to use [io.stream.open-file] - Works similarly to [io.file.load] but instead of returning the file's content, it returns the raw stream back to caller."
generated: true
guide: true
---

This is the guide to [`io.stream.open-file`](/reference/slots/io/io.stream.open-file/), whose reference page has its arguments, constraints and declaration.

Works similarly to **[io.file.load]** but instead of returning the file's content,
it returns the raw stream back to caller.

```
io.stream.open-file:/foo/bar.txt
```

After invoking the above, assuming the file exists, a raw `Stream` object can be
found as the value of the **[io.stream.open-file]** node.
