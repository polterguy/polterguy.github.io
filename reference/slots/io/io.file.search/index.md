---
title: "[io.file.search]"
description: "io.file.search is a slot in the io namespace of Magic Cloud. Searches for files on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.search/slot.json"
---

`io.file.search` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Searches for files on the server.

* **Value** (`folder-path`), required: Folder path to search from
* **Returns**: Returns one child node per matching file, each containing [file] with the relative file path and [lines] with matching line numbers

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[pattern]` | string | yes | Text or regular expression pattern to search for. |
| `[regex]` | bool | no | Whether [pattern] should be interpreted as a regular expression. Default: `false`. |
| `[case-sensitive]` | bool | no | Whether matching should be case-sensitive. Default: `false`. |
| `[extensions]` | string | no | Optional comma-separated file extensions to include. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | Search result object for one matching file. Can be repeated. |
| _unnamed child node_ / `[file]` | string | yes | Relative path to the matching file. |
| _unnamed child node_ / `[lines]` | lambda | yes | Line numbers containing matches in the file. |
| _unnamed child node_ / `[lines]` / _unnamed child node_ | int | no | One matching line number. Can be repeated. |

### Guide

<!-- guide -->
Searches all files recursively inside the specified folder and returns filenames with line numbers
containing the specified pattern.

```
io.file.search:/modules/
   pattern:"TODO"
```

Optional arguments:

* __[regex]__ - Treats pattern as regular expression
* __[case-sensitive]__ - Enables case sensitive search
* __[extensions]__ - Comma-separated list of extensions (e.g. .cs,.hl)

Example with regex + extensions:

```
io.file.search:/modules/
   pattern:"class\\s+Git"
   regex:true
   extensions:.cs,.hl
```

Return value example:

```
io.file.search
   .
      file:/modules/foo/bar.cs
      lines
         .:12
         .:48
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.file.search`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `io.file.save.binary`](/reference/slots/io/io.file.save.binary/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.unzip` &rarr;](/reference/slots/io/io.file.unzip/)

