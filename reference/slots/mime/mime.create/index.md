---
title: "[mime.create]"
description: "mime.create is a slot in the mime namespace of Magic Cloud. Builds a MIME message from headers and child [entity] nodes; useful for sending email or composing multipart payloads."
generated: true
llms: false
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

[How to use `mime.create`](/plugins/magic.lambda.mime/mime.create/)

### JSON declaration

This is the complete declaration of `mime.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `mime.add`](/reference/slots/mime/mime.add/) | [all `mime.*` slots](/reference/slots/mime/) | [`mime.list` &rarr;](/reference/slots/mime/mime.list/)

