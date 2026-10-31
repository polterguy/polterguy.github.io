---
title: "[git.remote.add]"
description: "git.remote.add is a slot in the git namespace of Magic Cloud. Adds a Git remote."
generated: true
llms: false
slot_json: "/reference/slots/git/git.remote.add/slot.json"
---

`git.remote.add` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Adds a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git remote add command output

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[name]` | string | no | Remote name. Default: `origin`. |
| `[url]` | string | yes | Remote URL. |

Guide: [How to use [git.remote.add]](/plugins/magic.lambda.git/#how-to-use-gitremoteadd)

### JSON declaration

This is the complete declaration of `git.remote.add`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.remote.add",
  "description": "Adds a Git remote",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "name": {
        "type": "string",
        "kind": "git-remote",
        "description": "Remote name",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "origin",
        "role": "Option",
        "projection": "Value"
      },
      "url": {
        "type": "string",
        "kind": "git-url",
        "description": "Remote URL",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "git-response,text",
      "description": "Resolves to the git remote add command output"
    }
  }
}
```

</details>

---

[&larr; `git.push`](/reference/slots/git/git.push/) | [all `git.*` slots](/reference/slots/git/) | [`git.restore` &rarr;](/reference/slots/git/git.restore/)

