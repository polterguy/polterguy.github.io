---
title: "How to use [mime.parse]"
description: "How to use [mime.parse] - Below is an example of how parsing a MIME message might look like using [mime.parse]."
generated: true
guide: true
---

This is the guide to [`mime.parse`](/reference/slots/mime/mime.parse/), whose reference page has its arguments, constraints and declaration.

Below is an example of how parsing a MIME message might look like using **[mime.parse]**.

```
// Actual message
.msg:"Content-Type: multipart/mixed; boundary=\"=-3O9TzEjuVDwt7d5uGDkV/Q==\"\n\n--=-3O9TzEjuVDwt7d5uGDkV/Q==\nContent-Type: text/plain\nContent-Disposition: attachment; filename=README.md\n\n# Your dynamic files folder\n\nSome README.md file\n\n--=-3O9TzEjuVDwt7d5uGDkV/Q==\nContent-Type: text/plain\n\nBar\n--=-3O9TzEjuVDwt7d5uGDkV/Q==--\n"

// Parsing the above message
mime.parse:x:@.msg
```

After evaluating the above, you'll end up with something resembling the following.

```
mime.parse:multipart/mixed
   entity:text/plain
      headers
         Content-Disposition:attachment; filename=README.md
      content:"# Your dynamic files folder\n\nSome README.md file\n"
   entity:text/plain
      content:Bar
```

Notice how the slot creates a tree structure, perfectly resembling your original MIME message. It will also take care of
MIME headers for you, adding these into a **[headers]** collection, on a per MIME entity basis, depending upon whether or not
your message actually contains headers or not.
