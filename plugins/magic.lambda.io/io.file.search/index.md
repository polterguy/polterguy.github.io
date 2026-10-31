---
title: "How to use [io.file.search]"
description: "How to use [io.file.search] - Searches all files recursively inside the specified folder and returns filenames with line numbers containing the specified pattern."
generated: true
guide: true
---

This is the guide to [`io.file.search`](/reference/slots/io/io.file.search/), whose reference page has its arguments, constraints and declaration.

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
