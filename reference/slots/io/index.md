---
title: io.* slots
description: The 29 slots named io.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [io.content.zip-stream]

Builds an in-memory zip stream from child entries; useful for returning an archive over HTTP without writing to disk.

* **Returns**: Resolves to a zip stream containing the supplied entries

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | ZIP entry path. Can be repeated. |
| _any node name_ / _any node name_ | string\|byte[] | yes | Entry content. |

Guide: [How to use [io.content.zip-stream]](/plugins/magic.lambda.io/#how-to-use-iocontentzip-stream)

## [io.file.copy]

Copies a file on the server.

* **Value** (`file-path`), required: Source file path

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

Guide: [How to use [io.file.copy]](/plugins/magic.lambda.io/#how-to-use-iofilecopy)

## [io.file.delete]

Deletes a file on the server.

* **Value** (`file-path`), required: File path to delete

Guide: [How to use [io.file.delete]](/plugins/magic.lambda.io/#how-to-use-iofiledelete)

## [io.file.execute]

Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments].

* **Value** (`hyperlambda-file`), required: File path to execute
* **Returns**: Resolves to the executed file's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the executed file as a child of [.arguments]. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the executed Hyperlambda file. Can be repeated. |

Guide: [How to use [io.file.execute]](/plugins/magic.lambda.io/#how-to-use-iofileexecute)

## [io.file.exists]

Returns true if a file exists.

* **Value** (`file-path`), required: File path to test
* **Returns**: Returns true if the file exists

Guide: [How to use [io.file.exists]](/plugins/magic.lambda.io/#how-to-use-iofileexists)

## [io.file.list]

Lists files in the specified folder.

* **Value** (`folder-path`), required: Folder path to list files from
* **Returns**: Returns one unnamed child node per relative file path

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

Guide: [How to use [io.file.list]](/plugins/magic.lambda.io/#how-to-use-iofilelist)

## [io.file.list-recursively]

Lists files recursively in the specified folder.

* **Value** (`folder-path`), required: Folder path to list files from
* **Returns**: Returns one unnamed child node per relative file path, recursively

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

Guide: [How to use [io.file.list-recursively]](/plugins/magic.lambda.io/#how-to-use-iofilelist-recursively)

## [io.file.load]

Loads a text file from the server.

Aliases: **[load-file]**

* **Value** (`file-path`), required: File path to load
* **Returns**: Resolves to the loaded file content

Guide: [How to use [io.file.load]](/plugins/magic.lambda.io/#how-to-use-iofileload)

## [io.file.load-recursively]

Loads files recursively from the specified folder.

* **Value** (`folder-path`), required: Folder path to load from
* **Returns**: Returns one unnamed child node per loaded file; each entry has a [name] child (relative file path) and a [content] child (file content as string)

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One loaded file entry; access fields via the [name] and [content] children. Can be repeated. |
| _unnamed child node_ / `[content]` | string | yes | Loaded file content as text. |
| _unnamed child node_ / `[name]` | string | yes | Relative file path of the loaded file. |

Guide: [How to use [io.file.load-recursively]](/plugins/magic.lambda.io/#how-to-use-iofileload-recursively)

## [io.file.load.binary]

Loads a binary file from the server.

* **Value** (`binary-file`), required: File path to load
* **Returns**: Resolves to the loaded binary file bytes

## [io.file.mixin]

Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result.

* **Value** (`file-path`), required: Path to the static file to mix with its same-named .hl codebehind file
* **Returns**: Resolves to the mixed file content in value and any codebehind-produced child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Optional argument available to codebehind lambda loaded for the mixed file. Can be repeated. |

Guide: [How to use [io.file.mixin]](/plugins/magic.lambda.io/#how-to-use-iofilemixin)

## [io.file.move]

Moves a file on the server.

* **Value** (`file-path`), required: Source file path

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

Guide: [How to use [io.file.move]](/plugins/magic.lambda.io/#how-to-use-iofilemove)

## [io.file.patch]

Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs.

* **Value** (`file-path`), required: File path to patch

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Unified diff patch content to apply. |

Guide: [How to use [io.file.patch]](/plugins/magic.lambda.io/#how-to-use-iofilepatch)

## [io.file.save]

Saves a text file to the server.

Aliases: **[save-file]**

* **Value** (`file-path`), required: File path to save

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Child node yielding the text content to save. |

Guide: [How to use [io.file.save]](/plugins/magic.lambda.io/#how-to-use-iofilesave)

## [io.file.save.binary]

Saves a binary file to the server.

* **Value** (`binary-file`), required: File path to save

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | byte[] | yes | Child node yielding the binary content to save. |

## [io.file.search]

Searches for files on the server.

* **Value** (`folder-path`), required: Folder path to search from
* **Returns**: Returns one child node per matching file, each containing [file] with the relative file path and [lines] with matching line numbers

| Argument | Type | Required | Description |
|---|---|---|---|
| `[case-sensitive]` | bool | no | Whether matching should be case-sensitive. Default: `false`. |
| `[extensions]` | string | no | Optional comma-separated file extensions to include. |
| `[pattern]` | string | yes | Text or regular expression pattern to search for. |
| `[regex]` | bool | no | Whether [pattern] should be interpreted as a regular expression. Default: `false`. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | Search result object for one matching file. Can be repeated. |
| _unnamed child node_ / `[file]` | string | yes | Relative path to the matching file. |
| _unnamed child node_ / `[lines]` | lambda | yes | Line numbers containing matches in the file. |
| _unnamed child node_ / `[lines]` / _unnamed child node_ | int | no | One matching line number. Can be repeated. |

Guide: [How to use [io.file.search]](/plugins/magic.lambda.io/#how-to-use-iofilesearch)

## [io.file.unzip]

Extracts a zip archive on the server.

* **Value** (`zip-file`), required: Zip archive path to extract

| Argument | Type | Required | Description |
|---|---|---|---|
| `[folder]` | string | no | Destination folder; defaults to the zip file's folder. |
| `[overwrite]` | bool | no | Whether existing extracted files should be overwritten. Default: `false`. |

Guide: [How to use [io.file.unzip]](/plugins/magic.lambda.io/#how-to-use-iofileunzip)

## [io.folder.copy]

Copies a folder on the server.

* **Value** (`folder-path`), required: Source folder path

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

Guide: [How to use [io.folder.copy]](/plugins/magic.lambda.io/#how-to-use-iofoldercopy)

## [io.folder.create]

Creates a folder on the server.

* **Value** (`folder-path`), required: Folder path to create

Guide: [How to use [io.folder.create]](/plugins/magic.lambda.io/#how-to-use-iofoldercreate)

## [io.folder.delete]

Deletes a folder on the server.

* **Value** (`folder-path`), required: Folder path to delete

Guide: [How to use [io.folder.delete]](/plugins/magic.lambda.io/#how-to-use-iofolderdelete)

## [io.folder.exists]

Returns true if a folder exists.

* **Value** (`folder-path`), required: Folder path to test
* **Returns**: Returns true if the folder exists

Guide: [How to use [io.folder.exists]](/plugins/magic.lambda.io/#how-to-use-iofolderexists)

## [io.folder.list]

Lists folders in the specified folder.

* **Value** (`folder-path`), required: Folder path to list subfolders from
* **Returns**: Returns one unnamed child node per relative folder path

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

Guide: [How to use [io.folder.list]](/plugins/magic.lambda.io/#how-to-use-iofolderlist)

## [io.folder.list-recursively]

Lists folders recursively in the specified folder.

* **Value** (`folder-path`), required: Folder path to list subfolders from
* **Returns**: Returns one unnamed child node per relative folder path, recursively

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

Guide: [How to use [io.folder.list-recursively]](/plugins/magic.lambda.io/#how-to-use-iofolderlist-recursively)

## [io.folder.move]

Moves a folder on the server.

* **Value** (`folder-path`), required: Source folder path

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

Guide: [How to use [io.folder.move]](/plugins/magic.lambda.io/#how-to-use-iofoldermove)

## [io.path.get-folder]

Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/').

* **Value** (`file-path`), required: Path to inspect
* **Returns**: Resolves to the folder portion of the supplied path

Guide: [How to use [io.path.get-folder]](/plugins/magic.lambda.io/#how-to-use-iopathget-folder)

## [io.stream.close]

Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle.

* **Value** (`stream`), required: Stream instance to close

Guide: [How to use [io.stream.close]](/plugins/magic.lambda.io/#how-to-use-iostreamclose)

## [io.stream.open-file]

Opens a file as a read-only stream so large files can be processed without loading them into memory; close with [io.stream.close].

* **Value** (`file-path`), required: File path to open as a stream
* **Returns**: Resolves to an open file stream

Guide: [How to use [io.stream.open-file]](/plugins/magic.lambda.io/#how-to-use-iostreamopen-file)

## [io.stream.read]

Reads from an open stream.

* **Value** (`stream`), required: Stream instance to read from
* **Returns**: Resolves to the bytes read from the stream

Guide: [How to use [io.stream.read]](/plugins/magic.lambda.io/#how-to-use-iostreamread)

## [io.stream.save-file]

Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads.

* **Value** (`file-path`), required: File path to save the stream to

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | Stream | yes | Child node yielding the stream to save. |
| `[overwrite]` | bool | no | Whether an existing file should be overwritten. Default: `true`. |

Guide: [How to use [io.stream.save-file]](/plugins/magic.lambda.io/#how-to-use-iostreamsave-file)

