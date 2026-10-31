---
title: "[git.status]"
description: "git.status is a slot in the git namespace of Magic Cloud. Returns Git repository status."
generated: true
llms: false
slot_json: "/reference/slots/git/git.status/slot.json"
---

`git.status` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Returns Git repository status.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns Git status text in value or, when structured, one child node per status line

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[porcelain]` | bool | no | Use porcelain status output. Default: `false`. |
| `[branch]` | bool | no | Include branch information. Default: `false`. |
| `[structured]` | bool | no | Return status lines as child nodes. Default: `false`. |

### Guide

[How to use `git.status`](/plugins/magic.lambda.git/git.status/)

### JSON declaration

This is the complete declaration of `git.status`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.status",
  "description": "Returns Git repository status",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "porcelain": {
        "type": "bool",
        "description": "Use porcelain status output",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "branch": {
        "type": "bool",
        "description": "Include branch information",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "structured": {
        "type": "bool",
        "description": "Return status lines as child nodes",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "git-status,text",
      "description": "Returns Git status text in value or, when structured, one child node per status line"
    }
  }
}
```

</details>

---

[&larr; `git.restore`](/reference/slots/git/git.restore/) | [all `git.*` slots](/reference/slots/git/)

