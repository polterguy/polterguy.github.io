---
title: "How to use [io.content.zip-stream]"
description: "How to use [io.content.zip-stream] - Creates a memory based ZIP stream you can return over the HTTP response object."
generated: true
guide: true
---

This is the guide to [`io.content.zip-stream`](/reference/slots/io/io.content.zip-stream/), whose reference page has its arguments, constraints and declaration.

Creates a memory based ZIP stream you can return over the HTTP response object. Notice,
this doesn't create a zip file, but rather a zip stream, which you can manipulate using other
slots. This slot is useful if you need to return zipped content as your HTTP response for instance.

Notice, both the root arguments (lambda children) of this slot will be evaluated, in addition to
its content nodes, evaluated once for each file declaration node. Notice also that the stream is
a memory based stream, and hence closing it, even in case of an exception, is not necessary.

```
io.content.zip-stream
   .:/foo/x.txt
      .:content of file
```
