---
title: "[git.merge]"
description: "git.merge is a slot in the git namespace of Magic Cloud. Merges a Git branch into the current branch, or aborts a merge that stopped on conflicts."
generated: true
llms: false
slot_json: "/reference/slots/git/git.merge/slot.json"
---

`git.merge` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Merges a Git branch into the current branch, or aborts a merge that stopped on conflicts.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git merge command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | no | Branch to merge into the current branch, required unless [abort] is true. |
| `[abort]` | bool | no | Abort a merge that stopped on conflicts. Default: `false`. |
| `[name]` | string | no | Author name of the merge commit. |
| `[email]` | string | no | Author email of the merge commit. |

### Guide

[How to use `git.merge`](/plugins/magic.lambda.git/git.merge/)

### JSON declaration

This is the complete declaration of `git.merge`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.merge",
  "description": "Merges a Git branch into the current branch, or aborts a merge that stopped on conflicts",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "branch": {
        "type": "string",
        "kind": "git-branch",
        "description": "Branch to merge into the current branch, required unless [abort] is true",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "abort": {
        "type": "bool",
        "description": "Abort a merge that stopped on conflicts",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "name": {
        "type": "string",
        "description": "Author name of the merge commit",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "email": {
        "type": "string",
        "description": "Author email of the merge commit",
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
      "description": "Resolves to the git merge command output"
    }
  }
}
```

</details>

---

[&larr; `git.log`](/reference/slots/git/git.log/) | [all `git.*` slots](/reference/slots/git/) | [`git.pull` &rarr;](/reference/slots/git/git.pull/)

