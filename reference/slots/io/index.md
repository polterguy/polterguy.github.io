---
title: "io.* slots"
description: "The 29 slots named io.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

29 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`io.content.zip-stream`](/reference/slots/io/io.content.zip-stream/) | Builds an in-memory zip stream from child entries; useful for returning an archive over HTTP without writing to disk. |
| [`io.file.copy`](/reference/slots/io/io.file.copy/) | Copies a file on the server. |
| [`io.file.delete`](/reference/slots/io/io.file.delete/) | Deletes a file on the server. |
| [`io.file.execute`](/reference/slots/io/io.file.execute/) | Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]. |
| [`io.file.exists`](/reference/slots/io/io.file.exists/) | Returns true if a file exists. |
| [`io.file.list`](/reference/slots/io/io.file.list/) | Lists files in the specified folder. |
| [`io.file.list-recursively`](/reference/slots/io/io.file.list-recursively/) | Lists files recursively in the specified folder. |
| [`io.file.load`](/reference/slots/io/io.file.load/) | Loads a text file from the server. Also known as `load-file`. |
| [`io.file.load-recursively`](/reference/slots/io/io.file.load-recursively/) | Loads files recursively from the specified folder. |
| [`io.file.load.binary`](/reference/slots/io/io.file.load.binary/) | Loads a binary file from the server. |
| [`io.file.mixin`](/reference/slots/io/io.file.mixin/) | Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result. |
| [`io.file.move`](/reference/slots/io/io.file.move/) | Moves a file on the server. |
| [`io.file.patch`](/reference/slots/io/io.file.patch/) | Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs. |
| [`io.file.save`](/reference/slots/io/io.file.save/) | Saves a text file to the server. Also known as `save-file`. |
| [`io.file.save.binary`](/reference/slots/io/io.file.save.binary/) | Saves a binary file to the server. |
| [`io.file.search`](/reference/slots/io/io.file.search/) | Searches for files on the server. |
| [`io.file.unzip`](/reference/slots/io/io.file.unzip/) | Extracts a zip archive on the server. |
| [`io.folder.copy`](/reference/slots/io/io.folder.copy/) | Copies a folder on the server. |
| [`io.folder.create`](/reference/slots/io/io.folder.create/) | Creates a folder on the server. |
| [`io.folder.delete`](/reference/slots/io/io.folder.delete/) | Deletes a folder on the server. |
| [`io.folder.exists`](/reference/slots/io/io.folder.exists/) | Returns true if a folder exists. |
| [`io.folder.list`](/reference/slots/io/io.folder.list/) | Lists folders in the specified folder. |
| [`io.folder.list-recursively`](/reference/slots/io/io.folder.list-recursively/) | Lists folders recursively in the specified folder. |
| [`io.folder.move`](/reference/slots/io/io.folder.move/) | Moves a folder on the server. |
| [`io.path.get-folder`](/reference/slots/io/io.path.get-folder/) | Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/'). |
| [`io.stream.close`](/reference/slots/io/io.stream.close/) | Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle. |
| [`io.stream.open-file`](/reference/slots/io/io.stream.open-file/) | Opens a file as a read-only stream so large files can be processed without loading them into memory; close with [io.stream.close]. |
| [`io.stream.read`](/reference/slots/io/io.stream.read/) | Reads from an open stream. |
| [`io.stream.save-file`](/reference/slots/io/io.stream.save-file/) | Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads. |

