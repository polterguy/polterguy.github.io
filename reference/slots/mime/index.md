---
title: "mime.* slots"
description: "The 4 slots named mime.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

4 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`mime.add`](/reference/slots/mime/mime.add/) | Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses. |
| [`mime.create`](/reference/slots/mime/mime.create/) | Builds a MIME message from headers and child [entity] nodes; useful for sending email or composing multipart payloads. |
| [`mime.list`](/reference/slots/mime/mime.list/) | Lists registered MIME type mappings. |
| [`mime.parse`](/reference/slots/mime/mime.parse/) | Parses a raw MIME message into a lambda tree of headers and body parts; commonly used for email or multipart payloads. |

