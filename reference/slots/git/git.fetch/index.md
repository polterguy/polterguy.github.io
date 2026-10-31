---
title: "[git.fetch]"
description: "git.fetch is a slot in the git namespace of Magic Cloud. Fetches updates from a Git remote."
generated: true
llms: false
slot_json: "/reference/slots/git/git.fetch/slot.json"
---

`git.fetch` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Fetches updates from a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git fetch command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to fetch from. Default: `origin`. |
| `[refspec]` | string | no | Optional refspec to fetch. |

### Guide

[How to use `git.fetch`](/plugins/magic.lambda.git/git.fetch/)

### JSON declaration

This is the complete declaration of `git.fetch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.fetch",
  "description": "Fetches updates from a Git remote",
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
        "description": "Remote to fetch from",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "origin",
        "role": "Option",
        "projection": "Value"
      },
      "refspec": {
        "type": "string",
        "kind": "git-refspec",
        "description": "Optional refspec to fetch",
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
      "description": "Resolves to the git fetch command output"
    }
  }
}
```

</details>

---

[&larr; `git.diff`](/reference/slots/git/git.diff/) | [all `git.*` slots](/reference/slots/git/) | [`git.pull` &rarr;](/reference/slots/git/git.pull/)

