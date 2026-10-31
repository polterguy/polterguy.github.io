---
title: "[git.restore]"
description: "git.restore is a slot in the git namespace of Magic Cloud. Discards uncommitted changes by restoring one file from HEAD, or resets the whole working tree to HEAD including removal of untracked files."
generated: true
llms: false
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

[How to use `git.restore`](/plugins/magic.lambda.git/git.restore/)

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

