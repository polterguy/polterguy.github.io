---
title: "[mime.parse]"
description: "mime.parse is a slot in the mime namespace of Magic Cloud. Parses a raw MIME message into a lambda tree of headers and body parts; commonly used for email or multipart payloads."
generated: true
llms: "guide"
slot_json: "/reference/slots/mime/mime.parse/slot.json"
---

`mime.parse` is a slot in the `mime` namespace, in Hyperlambda, the language of Magic Cloud. Parses a raw MIME message into a lambda tree of headers and body parts; commonly used for email or multipart payloads.

* **Value** (`mime-message`), required: Raw MIME message to parse
* **Returns**: Resolves to the parsed MIME entity content type as the node value, and headers, content, and nested entities as child nodes

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

### Guide

<!-- guide -->
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
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.mime](/plugins/magic.lambda.mime/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mime.parse`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `mime.list`](/reference/slots/mime/mime.list/) | [all `mime.*` slots](/reference/slots/mime/)

