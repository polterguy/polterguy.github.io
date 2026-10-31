---
title: "[io.stream.close]"
description: "io.stream.close is a slot in the io namespace of Magic Cloud. Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.stream.close/slot.json"
---

`io.stream.close` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle.

* **Value** (`stream`), required: Stream instance to close

### Guide

<!-- guide -->
Closes a previously opened stream.

**Notice** - You would rarely directly use streams from Hyperlambda, and not manipulate them
in any ways, but rather use for instance **[\[io.file.load\]](/reference/slots/io/io.file.load/)** and similar _"high level"_ slots -
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
by **[\[io.stream.open-file\]](/reference/slots/io/io.stream.open-file/)** will be explicitly closed.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.stream.close`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.stream.close",
  "description": "Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle",
  "signature": {
    "input": {
      "kind": "stream",
      "description": "Stream instance to close",
      "required": true,
      "mode": "Expression"
    }
  }
}
```

</details>

---

[&larr; `io.path.get-folder`](/reference/slots/io/io.path.get-folder/) | [all `io.*` slots](/reference/slots/io/) | [`io.stream.open-file` &rarr;](/reference/slots/io/io.stream.open-file/)

