---
title: "[io.file.patch]"
description: "io.file.patch is a slot in the io namespace of Magic Cloud. Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.patch/slot.json"
---

`io.file.patch` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs.

* **Value** (`file-path`), required: File path to patch

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Unified diff patch content to apply. |

### Guide

<!-- guide -->
Applies a unified diff patch to the specified file on disc. The patch is provided as the first child argument.
This slot evaluates its children before applying the patch, which allows you to dynamically create the patch
using other slots.

```
io.file.patch:/misc/README2.md
   .:@"
@@ -1,3 +1,4 @@
 This is line 1
 This is line 2
 This is line 3
+This is line 4
"
```

#### Patch format rules

The patch parser accepts standard unified diff format, but still enforces some rules and will throw if the patch deviates.

* The patch must target **exactly one file**.
* Each hunk must start with a header line in this format: `@@ -a,b +c,d @@`.
* Every line inside a hunk must begin with one of these characters:
  * ` ` (space) for context lines
  * `-` for deletions
  * `+` for additions
  * `\` for the `\ No newline at end of file` marker
* Empty lines inside a hunk are allowed and treated as context lines.
* Hunks must appear in the same order as the parts of the file they change.
* Hunk line counts are not enforced, and a hunk carrying no context lines at all is legal.

#### How a hunk is located

A hunk's header says where the hunk belonged in the file the patch was created against, and that
position is used as a starting point rather than as a requirement. Since the file may have drifted
since the patch was created, the parser begins at the position the header declares and widens
outwards, applying the hunk at the nearest position whose content matches. The search reaches at
most 250 lines in either direction, and never backwards past a hunk that was already applied.

Two things follow from this. The context does **not** have to be unique within the file, so repeated
lines such as a closing brace, a blank line or a bare `return` are perfectly fine. And the header's
line numbers are allowed to be stale.

What still has to hold is that the context lines and the deleted lines match the file at the
position the parser settles on, which is verified before anything is written. Locating a hunk is
forgiving; applying one is not.

Lines are first compared exactly. Only if nowhere in the file matches that way is the search
repeated comparing lines while ignoring trailing whitespace. This lets a patch apply to formats
where trailing whitespace is significant but invisible to whoever wrote the patch, most notably
Markdown, where two trailing spaces denote a hard line break. A hunk located this way still leaves
the file's own trailing whitespace untouched.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `io.file.patch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.patch",
  "description": "Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to patch",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "unified-diff",
        "description": "Unified diff patch content to apply",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne"
      }
    }
  }
}
```

</details>

---

[&larr; `io.file.move`](/reference/slots/io/io.file.move/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.save` &rarr;](/reference/slots/io/io.file.save/)

