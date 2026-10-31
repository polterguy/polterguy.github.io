---
title: mime.* slots
description: The 4 slots named mime.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [mime.add]

Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses.

* **Value** (`content-type`), required: File extension or MIME type key to register

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | MIME type value for the extension/key. |

Guide: [How to use [mime.add]](/plugins/magic.endpoint/#how-to-use-mimeadd)

## [mime.create]

Builds a MIME message from headers and child [entity] nodes; useful for sending email or composing multipart payloads.

* **Value** (`content-type`), required: Primary MIME content type
* **Returns**: Resolves to the MIME message text in value or, when structured, MIME header and content nodes as children

| Argument | Type | Required | Description |
|---|---|---|---|
| `[content]` | string | no | Inline MIME part content. |
| `[entity]` | string | yes | Nested MIME entity content type; same leaf-vs-multipart shape as the parent [mime.create] value. |
| `[entity]` / `[content]` | string | no | Inline MIME part content. |
| `[entity]` / `[filename]` | string | no | File path to use as MIME part content. |
| `[entity]` / `[headers]` | lambda | no | MIME headers. |
| `[entity]` / `[headers]` / _any node name_ | string | no | Header name and value. Can be repeated. |
| `[filename]` | string | no | File path to use as MIME part content. |
| `[headers]` | lambda | no | MIME headers. |
| `[headers]` / _any node name_ | string | no | Header name and value. Can be repeated. |
| `[structured]` | bool | no | When true returns the MIME tree as [headers] and [content] children; when false (default) returns the serialized MIME message text in the slot value. Default: `false`. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[] | no | Decoded MIME part content; text parts return string content and binary parts return byte[] content. |
| `[entity]` | string | no | Nested parsed MIME entity; node value is the nested entity content type, and children carry headers, content, and any deeper entities. Can be repeated. |
| `[entity]` / `[content]` | string\|byte[] | no | Decoded MIME part content; text parts return string content and binary parts return byte[] content. |
| `[entity]` / `[headers]` | lambda | no | MIME headers from the parsed entity, excluding Content-Type because the entity content type is returned as the node value. |
| `[entity]` / `[headers]` / _any node name_ | string | no | Parsed MIME header value; child name is the header name. Can be repeated. |
| `[headers]` | lambda | no | MIME headers from the parsed entity, excluding Content-Type because the entity content type is returned as the node value. |
| `[headers]` / _any node name_ | string | no | Parsed MIME header value; child name is the header name. Can be repeated. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

* **Constraint** (Excludes): Binary MIME parts cannot carry inline [content] — reference the bytes via [filename] (`[content]`)
* **Constraint** (Excludes): Leaf MIME parts must not contain nested [entity] children (`[entity]`)
* **Constraint** (ExactlyOneOf): Leaf MIME parts require either [content] or [filename] (`[content]`, `[filename]`)
* **Constraint** (Excludes): Multipart MIME parts must not contain [content] or [filename] (`[content]`, `[filename]`)
* **Constraint** (AtLeastOneOf): Multipart MIME parts require two or more [entity] children (`[entity]`)

Guide: [How to use [mime.create]](/plugins/magic.lambda.mime/#how-to-use-mimecreate)

## [mime.list]

Lists registered MIME type mappings.

* **Returns**: Resolves to one named child node per registered MIME type mapping, where the child name is the file extension and the value is the MIME type

Guide: [How to use [mime.list]](/plugins/magic.endpoint/#how-to-use-mimelist)

## [mime.parse]

Parses a raw MIME message into a lambda tree of headers and body parts; commonly used for email or multipart payloads.

* **Value** (`mime-message`), required: Raw MIME message to parse
* **Returns**: Resolves to the parsed MIME entity content type as the node value, and headers, content, and nested entities as child nodes

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[] | no | Decoded MIME part content; text parts return string content and binary parts return byte[] content. |
| `[entity]` | string | no | Nested parsed MIME entity; node value is the nested entity content type, and children carry headers, content, and any deeper entities. Can be repeated. |
| `[entity]` / `[content]` | string\|byte[] | no | Decoded MIME part content; text parts return string content and binary parts return byte[] content. |
| `[entity]` / `[headers]` | lambda | no | MIME headers from the parsed entity, excluding Content-Type because the entity content type is returned as the node value. |
| `[entity]` / `[headers]` / _any node name_ | string | no | Parsed MIME header value; child name is the header name. Can be repeated. |
| `[headers]` | lambda | no | MIME headers from the parsed entity, excluding Content-Type because the entity content type is returned as the node value. |
| `[headers]` / _any node name_ | string | no | Parsed MIME header value; child name is the header name. Can be repeated. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

Guide: [How to use [mime.parse]](/plugins/magic.lambda.mime/#how-to-use-mimeparse)

