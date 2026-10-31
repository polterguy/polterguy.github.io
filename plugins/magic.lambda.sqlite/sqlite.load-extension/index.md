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

The path in **[file]** is a plain file system path, resolved relative to the working directory of your backend, and _not_ relative to
your cloudlet's root folder, which means a leading `/` makes it an absolute path on the server. It can point into a folder, and you should leave out the
file extension, since SQLite adds the one your operating system uses, such as _".so"_, _".dylib"_ or _".dll"_. On ARM processors the slot first appends
`-arm64` or `-arm` to the filename, unless **[append-platform]** is false. Magic ships the vector extension in the _"sqlite-plugins"_ folder, and
below is how Magic itself loads it, using **[proc]** to name the extension's entry point.

```
sqlite.connect:[generic|magic]
   sqlite.load-extension
      file:sqlite-plugins/vector
      proc:sqlite3_vector_init
```
