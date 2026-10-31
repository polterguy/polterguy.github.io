---
title: "How to use [sqlite.load-extension]"
description: "How to use [sqlite.load-extension] - Loads a SQLite extension into the connection opened by [sqlite.connect]."
generated: true
guide: true
---

The reference page of [`sqlite.load-extension`](/reference/slots/sqlite/sqlite.load-extension/) has its arguments, constraints and declaration.

Loads a SQLite extension into the connection opened by **[sqlite.connect]**. The slot takes its arguments as children.

* __[file]__ - Filename of the extension to load. Mandatory, the slot throws an exception if it is missing.
* __[proc]__ - Optional entry point of the extension.
* __[append-platform]__ - Boolean, defaults to `true`. If true, the slot appends `-arm64` or `-arm` to the filename when running on an ARM64 or ARM processor.

Below is an example, loading an extension from the _"/data/extensions/"_ folder into a connection.

```
sqlite.connect:sakila
   sqlite.load-extension
      file:/data/extensions/vec0
```
