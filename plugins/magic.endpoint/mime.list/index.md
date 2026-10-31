---
title: "How to use [mime.list]"
description: "How to use [mime.list] - This slot lists all MIME type mappings registered in the current installation, including those added with [mime.add]."
generated: true
guide: true
---

This is the guide to [`mime.list`](/reference/slots/mime/mime.list/), whose reference page has its arguments, constraints and declaration.

This slot lists all MIME type mappings registered in the current installation, including those added with **[mime.add]**.
It returns one child node for each mapping, where the name of the child node is the file extension and its value is the MIME type.
It takes no arguments.
