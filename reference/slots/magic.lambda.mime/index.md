---
title: magic.lambda.mime slot reference
description: Every slot in magic.lambda.mime with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.mime](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.mime). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.mime](/plugins/magic.lambda.mime/)._

## [.mime.create]

Creates a MIME message without exposing the public wrapper slot.

* **Value** (`content-type`), required: Primary MIME content type
* **Returns**: Resolves to the created MimeKit MIME entity

## [.mime.parse]

Parses a MIME message without exposing the public wrapper slot.

* **Value** (`mime-entity`), required: MIME entity to parse
* **Returns**: Resolves to a MIME entity tree where the value is the entity content type and children contain headers, content, and nested entities

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | Parsed MIME header value; child name is the header name |

## [mime.create]

Builds a MIME message from headers and child [entity] nodes; useful for sending email or composing multipart payloads.

* **Value** (`content-type`), required: Primary MIME content type
* **Returns**: Resolves to the MIME message text in value or, when structured, MIME header and content nodes as children

| Argument | Type | Required | Description |
|---|---|---|---|
| `[structured]` | bool | no | When true returns the MIME tree as [headers] and [content] children; when false (default) returns the serialized MIME message text in the slot value |

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | Header name and value |

Guide: [How to use [mime.create]](/plugins/magic.lambda.mime/#how-to-use-mimecreate)

## [mime.parse]

Parses a raw MIME message into a lambda tree of headers and body parts; commonly used for email or multipart payloads.

* **Value** (`mime-message`), required: Raw MIME message to parse
* **Returns**: Resolves to the parsed MIME entity content type as the node value, and headers, content, and nested entities as child nodes

| Returned node | Type | Description |
|---|---|---|
| `[*]` |  | Parsed MIME header value; child name is the header name |

Guide: [How to use [mime.parse]](/plugins/magic.lambda.mime/#how-to-use-mimeparse)

