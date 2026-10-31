---
title: "How to use [mime.create]"
description: "How to use [mime.create] - The [mime.create] slot is logically the exact opposite of the [mime.parse] slot, and can take (almost) the exact same input as its sibling produces as output."
generated: true
guide: true
---

The reference page of [`mime.create`](/reference/slots/mime/mime.create/) has its arguments, constraints and declaration.

The **[mime.create]** slot is logically the exact opposite of the **[mime.parse]** slot, and can take (almost) the exact
same input as its sibling produces as output. Below is an example.

```
mime.create:multipart/mixed
   structured:false
   entity:text/plain
      content:this is the body text     
   entity:text/plain
      content:this is another body text
```

Which of course wil result in something resembling the following after evaluation.

```
mime.create:"Content-Type: multipart/mixed; boundary=\"=-7+NI+p6PuOyQUzW5ihnXvw==\"\n\n--=-7+NI+p6PuOyQUzW5ihnXvw==\nContent-Type: text/plain\n\nthis is the body text\n--=-7+NI+p6PuOyQUzW5ihnXvw==\nContent-Type: text/plain\n\nthis is another body text\n--=-7+NI+p6PuOyQUzW5ihnXvw==--\n"
```

**Notice** - If you set its **[structured]** argument to boolean `true`, the slot will return the MIME envelope headers
for the outermost MIME entity _"detached"_ from the rest of the message. This is useful when you for some reasons don't want
the headers for the outermost entity to be a part of the actual message, such as for instance when creating `multipart/form-data`
types of messages you need to transmit to some HTTP endpoint. If you do this, the return after executing the slot will
resemble the following.

```
mime.create
   Content-Type:"multipart/mixed; boundary=\"=-EbMBZ3eHrSrMqtB2KHSv+A==\""
   content:"--=-EbMBZ3eHrSrMqtB2KHSv+A==\nContent-Type: text/plain\n\nthis is the body text\n--=-EbMBZ3eHrSrMqtB2KHSv+A==\nContent-Type: text/plain\n\nthis is another body text\n--=-EbMBZ3eHrSrMqtB2KHSv+A==--\n"
```

This is useful if you for some reasons don't want the `Content-Type` to be a part of the MIME message itself, which is useful when creating HTTP envelopes and content for instance, where the Content-Type parts needs to be submitted separately as an HTTP header.

## MIME headers

To supply MIME headers for individual MIME entites, you can add a **[headers]** section as a child to your **[entity]** node. Below is an example of how to construct a MIME text entity with an attachement, wrapped inside a multipart/mixed parent.

```
mime.create:multipart/mixed
   entity:text/plain
      content:Some text content
   entity:text/markdown
      headers
         Content-Disposition:attachment; filename=README.md
      content:Some Markdown content here
```

The above will create one multipart MIME entity with two children, where one of its children are declaring itself as an attachment, with the filename of _"README.md"_ due to its `Content-Disposition` header. If you parse the resulting MIME message using **[mime.parse]**, you will end up with roughly what you started with.

You can add any headers you wish into individual MIME entities using the above syntax. The `Content-Type` header will be ignored though, since it's assumed to be the value of your **[entity]** node.

## File attachments

If you want to attach physical files, it's probably smart to attach these using **[filename]** as an alternative to loading the entire file into memory first. This will transmit the file directly from your file system to the socket, and never load the file into memory. This obviously preserves a lot of memoery for you, especially for large file.

If we're to change the above code to illustrate how this ends up looking like, it would become something resembling the following.

```
mime.create:multipart/mixed
   entity:text/plain
      content:Some text content
   entity:text/markdown
      filename:/etc/README.md
```

Notice, if you supply a **[filename]** argument, then the library will automatically associate the correct `Content-Disposition` header with your MIME entity, unless explicitly overridden by your code.
