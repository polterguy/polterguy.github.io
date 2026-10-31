---
title: "[git.push]"
description: "git.push is a slot in the git namespace of Magic Cloud. Pushes changes to a Git remote."
generated: true
llms: false
slot_json: "/reference/slots/git/git.push/slot.json"
---

`git.push` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Pushes changes to a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git push command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to push to. Default: `origin`. |
| `[branch]` | string | no | Branch to push. |
| `[set-upstream]` | bool | no | Set upstream while pushing. Default: `false`. |

Guide: [How to use [git.push]](/plugins/magic.lambda.git/#how-to-use-gitpush)

### JSON declaration

This is the complete declaration of `git.push`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.push",
  "description": "Pushes changes to a Git remote",
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
        "description": "Remote to push to",
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
        "description": "Branch to push",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "set-upstream": {
        "type": "bool",
        "description": "Set upstream while pushing",
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
      "description": "Resolves to the git push command output"
    }
  }
}
```

</details>

---

[&larr; `git.pull`](/reference/slots/git/git.pull/) | [all `git.*` slots](/reference/slots/git/) | [`git.remote.add` &rarr;](/reference/slots/git/git.remote.add/)

