---
title: "[git.restore]"
description: "git.restore is a slot in the git namespace of Magic Cloud. Discards uncommitted changes by restoring one file from HEAD, or resets the whole working tree to HEAD including removal of untracked files."
generated: true
llms: "guide"
slot_json: "/reference/slots/git/git.restore/slot.json"
---

`git.restore` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Discards uncommitted changes by restoring one file from HEAD, or resets the whole working tree to HEAD including removal of untracked files.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | no | Repository-relative path of one file to restore from HEAD; omitted resets the whole working tree to HEAD and removes untracked files. |

### Guide

<!-- guide -->
Discards uncommitted changes. The repo path is the node value. With a repo-relative `file`, that one file is
restored from HEAD in both index and working tree. Without `file`, the whole working tree is reset to HEAD
**and untracked files and folders are removed**, leaving the folder identical to the last commit.

```
git.restore:/modules/stripe/
   file:README.md
```

```
git.restore:/modules/stripe/
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.git](/plugins/magic.lambda.git/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `git.restore`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.restore",
  "description": "Discards uncommitted changes by restoring one file from HEAD, or resets the whole working tree to HEAD including removal of untracked files",
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
        "description": "Repository-relative path of one file to restore from HEAD; omitted resets the whole working tree to HEAD and removes untracked files",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "git-response,text",
      "description": "Resolves to the git command output"
    }
  }
}
```

</details>

---

[&larr; `git.remote.add`](/reference/slots/git/git.remote.add/) | [all `git.*` slots](/reference/slots/git/) | [`git.status` &rarr;](/reference/slots/git/git.status/)

