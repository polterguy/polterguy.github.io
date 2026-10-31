---
title: "How to use [io.stream.close]"
description: "How to use [io.stream.close] - Closes a previously opened stream."
generated: true
guide: true
---

The reference page of [`io.stream.close`](/reference/slots/io/io.stream.close/) has its arguments, constraints and declaration.

Closes a previously opened stream.

**Notice** - You would rarely directly use streams from Hyperlambda, and not manipulate them
in any ways, but rather use for instance **[io.file.load]** and similar _"high level"_ slots -
And only use streams when you need to directly access the HTTP request stream, to persist a file
uploaded by a user, or return a file over the HTTP response object. Hence, directly opening
a stream for any other purpose but to return it over the HTTP response object is something you'd
probably never want to do. And if you return the stream over the HTTP response object, .Net takes
ownership over the stream, and ensures it is closed and disposed. However, for completeness we've
still provided the ability to explicitly close a stream using the **[io.stream.close]** - Even though
you would probably never really need to use it. Besides, opening streams for any other purpose but
to return them over the HTTP response object, might also create leaks, since there is no means to
guarantee that the stream is closed in case of exceptions, etc - Unless you explicitly take care
of such things manually.

```
io.stream.open-file:/foo/bar.txt
io.stream.close:x:-
```

After invoking the above, assuming the file exists, the stream previously opened
by **[io.stream.open-file]** will be explicitly closed.
