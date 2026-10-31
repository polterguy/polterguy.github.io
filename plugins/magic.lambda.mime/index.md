---
title: magic.lambda.mime
moved_anchors: {"how-to-use-mimecreate": "/plugins/magic.lambda.mime/mime.create/", "how-to-use-mimeparse": "/plugins/magic.lambda.mime/mime.parse/"}
---

magic.lambda.mime gives you the ability to parse and create MIME messages from Hyperlambda.
This project contains the following slots.

* __[\[mime.parse\]](/plugins/magic.lambda.mime/mime.parse/)__ - Parses a MIME message, and returns it as a lambda object
* __[\[mime.create\]](/plugins/magic.lambda.mime/mime.create/)__ - Creates a MIME message for you, and returns the entire message as text, being the MIME entity
* __[.mime.parse]__ - Parses a native MimeEntity for you, and returns it as a lambda object (not for usage directly from Hyperlambda code)
* __[.mime.create]__ - Creates a MIME message for you, and returns it as a native MimeEntity object (not for usage directly from Hyperlambda code)
