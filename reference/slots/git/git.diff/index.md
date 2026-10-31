---
title: "[git.diff]"
description: "git.diff is a slot in the git namespace of Magic Cloud. Returns the unified diff between the working tree and HEAD, for the whole repository or one file."
generated: true
llms: "guide"
slot_json: "/reference/slots/git/git.diff/slot.json"
---

`git.diff` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Returns the unified diff between the working tree and HEAD, for the whole repository or one file.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns the unified diff text

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | no | Repository-relative path of one file to diff; omitted diffs the whole repository. |

### Guide

<!-- guide -->
Shows the unified diff between the working tree and HEAD. The repo path is the node value. By default the
whole repository is diffed, while providing a repo-relative `file` restricts the diff to that one file.
Untracked files have no diff, since git knows nothing about them yet.

```
git.diff:/modules/stripe/
```

```
git.diff:/modules/stripe/
   file:README.md
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.git](/plugins/magic.lambda.git/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `git.diff`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.diff",
  "description": "Returns the unified diff between the working tree and HEAD, for the whole repository or one file",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "file": {
        "type": "string",
        "kind": "git-file-path",
        "description": "Repository-relative path of one file to diff; omitted diffs the whole repository",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "git-diff,text",
      "description": "Returns the unified diff text"
    }
  }
}
```

</details>

---

[&larr; `git.delete-repo`](/reference/slots/git/git.delete-repo/) | [all `git.*` slots](/reference/slots/git/) | [`git.fetch` &rarr;](/reference/slots/git/git.fetch/)

