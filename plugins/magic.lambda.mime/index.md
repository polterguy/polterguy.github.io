---
title: magic.lambda.mime
moved_anchors: {"how-to-use-mimecreate": "/reference/slots/mime/mime.create/#guide", "how-to-use-mimeparse": "/reference/slots/mime/mime.parse/#guide"}
---

magic.lambda.mime gives you the ability to parse and create MIME messages from Hyperlambda.
This project contains the following slots.

* __[\[mime.parse\]](/reference/slots/mime/mime.parse/)__ - Parses a MIME message, and returns it as a lambda object
* __[\[mime.create\]](/reference/slots/mime/mime.create/)__ - Creates a MIME message for you, and returns the entire message as text, being the MIME entity
* __[.mime.parse]__ - Parses a native MimeEntity for you, and returns it as a lambda object (not for usage directly from Hyperlambda code)
* __[.mime.create]__ - Creates a MIME message for you, and returns it as a native MimeEntity object (not for usage directly from Hyperlambda code)
