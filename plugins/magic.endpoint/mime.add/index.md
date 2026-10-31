---
title: "How to use [mime.add]"
description: "How to use [mime.add] - This slot associates a file extension with a MIME type."
generated: true
guide: true
---

This is the guide to [`mime.add`](/reference/slots/mime/mime.add/), whose reference page has its arguments, constraints and declaration.

This slot associates a file extension with a MIME type. Notice, it will override previous associations if existing.
Example usage can be found below.

```
mime.add:py
   .:application/python
```

Then later when the endpoint resolver is returning files ending with _".py"_, it will return these with
a `Content-Type` of _"application/python"_.
