---
title: "[git.pull]"
description: "git.pull is a slot in the git namespace of Magic Cloud. Pulls updates from a Git remote."
generated: true
llms: false
slot_json: "/reference/slots/git/git.pull/slot.json"
---

`git.pull` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Pulls updates from a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git pull command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to pull from. Default: `origin`. |
| `[branch]` | string | no | Branch to pull. |
| `[rebase]` | bool | no | Use rebase while pulling. Default: `false`. |
| `[ff-only]` | bool | no | Only allow fast-forward pulls. Default: `false`. |

### Guide

[How to use `git.pull`](/plugins/magic.lambda.git/git.pull/)

### JSON declaration

This is the complete declaration of `git.pull`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.pull",
  "description": "Pulls updates from a Git remote",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "remote": {
        "type": "string",
        "kind": "git-remote",
        "description": "Remote to pull from",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "origin",
        "role": "Option",
        "projection": "Value"
      },
      "branch": {
        "type": "string",
        "kind": "git-branch",
        "description": "Branch to pull",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "rebase": {
        "type": "bool",
        "description": "Use rebase while pulling",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "ff-only": {
        "type": "bool",
        "description": "Only allow fast-forward pulls",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "git-response,text",
      "description": "Resolves to the git pull command output"
    }
  }
}
```

</details>

---

[&larr; `git.fetch`](/reference/slots/git/git.fetch/) | [all `git.*` slots](/reference/slots/git/) | [`git.push` &rarr;](/reference/slots/git/git.push/)

