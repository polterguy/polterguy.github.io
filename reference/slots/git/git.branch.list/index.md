---
title: "[git.branch.list]"
description: "git.branch.list is a slot in the git namespace of Magic Cloud. Returns every branch in the local repository, marking which one is currently checked out."
generated: true
llms: "guide"
slot_json: "/reference/slots/git/git.branch.list/slot.json"
---

`git.branch.list` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Returns every branch in the local repository, marking which one is currently checked out.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns one unnamed child node per git branch name

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | bool | no | List remote branches. Default: `false`. |
| `[all]` | bool | no | List all branches. Default: `false`. |

### Guide

<!-- guide -->
Lists branches. The repo path is the node value. Each branch is returned as a `.` node.

```
git.branch.list:/modules/stripe/
```

```
git.branch.list:/modules/stripe/
   remote:true
```

```
git.branch.list:/modules/stripe/
   all:true
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `git.branch.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.branch.list",
  "description": "Returns every branch in the local repository, marking which one is currently checked out",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "remote": {
        "type": "bool",
        "description": "List remote branches",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "all": {
        "type": "bool",
        "description": "List all branches",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "git-branch-list,string-list",
      "element-kind": "git-branch,text",
      "description": "Returns one unnamed child node per git branch name"
    }
  }
}
```

</details>

---

[all `git.*` slots](/reference/slots/git/) | [`git.checkout` &rarr;](/reference/slots/git/git.checkout/)

