---
title: "[mime.create]"
description: "mime.create is a slot in the mime namespace of Magic Cloud. Builds a MIME message from headers and child [entity] nodes; useful for sending email or composing multipart payloads."
generated: true
llms: "guide"
slot_json: "/reference/slots/mime/mime.create/slot.json"
---

`mime.create` is a slot in the `mime` namespace, in Hyperlambda, the language of Magic Cloud. Builds a MIME message from headers and child [entity] nodes; useful for sending email or composing multipart payloads.

* **Value** (`content-type`), required: Primary MIME content type
* **Returns**: Resolves to the MIME message text in value or, when structured, MIME header and content nodes as children

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[entity]` | string | yes | Nested MIME entity content type; same leaf-vs-multipart shape as the parent [mime.create] value. |
| `[entity]` / `[headers]` | lambda | no | MIME headers. |
| `[entity]` / `[headers]` / _any node name_ | string | no | Header name and value. Can be repeated. |
| `[entity]` / `[content]` | string | no | Inline MIME part content. |
| `[entity]` / `[filename]` | string | no | File path to use as MIME part content. |
| `[structured]` | bool | no | When true returns the MIME tree as [headers] and [content] children; when false (default) returns the serialized MIME message text in the slot value. Default: `false`. |
| `[headers]` | lambda | no | MIME headers. |
| `[headers]` / _any node name_ | string | no | Header name and value. Can be repeated. |
| `[content]` | string | no | Inline MIME part content. |
| `[filename]` | string | no | File path to use as MIME part content. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| `[headers]` | lambda | no | MIME headers from the parsed entity, excluding Content-Type because the entity content type is returned as the node value. |
| `[headers]` / _any node name_ | string | no | Parsed MIME header value; child name is the header name. Can be repeated. |
| `[content]` | string\|byte[] | no | Decoded MIME part content; text parts return string content and binary parts return byte[] content. |
| `[entity]` | string | no | Nested parsed MIME entity; node value is the nested entity content type, and children carry headers, content, and any deeper entities. Can be repeated. |
| `[entity]` / `[headers]` | lambda | no | MIME headers from the parsed entity, excluding Content-Type because the entity content type is returned as the node value. |
| `[entity]` / `[headers]` / _any node name_ | string | no | Parsed MIME header value; child name is the header name. Can be repeated. |
| `[entity]` / `[content]` | string\|byte[] | no | Decoded MIME part content; text parts return string content and binary parts return byte[] content. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Constraints

* **Excludes**: Binary MIME parts cannot carry inline [content] — reference the bytes via [filename] (`[content]`)
* **Excludes**: Leaf MIME parts must not contain nested [entity] children (`[entity]`)
* **ExactlyOneOf**: Leaf MIME parts require either [content] or [filename] (`[content]`, `[filename]`)
* **Excludes**: Multipart MIME parts must not contain [content] or [filename] (`[content]`, `[filename]`)
* **AtLeastOneOf**: Multipart MIME parts require two or more [entity] children (`[entity]`)

### Guide

<!-- guide -->
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

#### MIME headers

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

#### File attachments

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
<!-- /guide -->

### JSON declaration

This is the complete declaration of `mime.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `mime.add`](/reference/slots/mime/mime.add/) | [all `mime.*` slots](/reference/slots/mime/) | [`mime.list` &rarr;](/reference/slots/mime/mime.list/)

