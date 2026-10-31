---
title: "[git.commit]"
description: "git.commit is a slot in the git namespace of Magic Cloud. Stages all changes in the repo and creates a new commit with the supplied message and author."
generated: true
llms: false
slot_json: "/reference/slots/git/git.commit/slot.json"
---

`git.commit` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Stages all changes in the repo and creates a new commit with the supplied message and author.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git commit command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[message]` | string | yes | Commit message. |
| `[all]` | bool | no | Stage all changed files before committing. Default: `true`. |
| `[amend]` | bool | no | Amend the previous commit. Default: `false`. |
| `[name]` | string | no | Author name for the commit; omitted falls back to git's configured identity. |
| `[email]` | string | no | Author email for the commit; omitted falls back to git's configured identity. |

### Guide

[How to use `git.commit`](/plugins/magic.lambda.git/git.commit/)

### JSON declaration

This is the complete declaration of `git.commit`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.commit",
  "description": "Stages all changes in the repo and creates a new commit with the supplied message and author",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "message": {
        "type": "string",
        "kind": "commit-message",
        "description": "Commit message",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "all": {
        "type": "bool",
        "description": "Stage all changed files before committing",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      },
      "amend": {
        "type": "bool",
        "description": "Amend the previous commit",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "name": {
        "type": "string",
        "description": "Author name for the commit; omitted falls back to git's configured identity",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "email": {
        "type": "string",
        "description": "Author email for the commit; omitted falls back to git's configured identity",
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
      "description": "Resolves to the git commit command output"
    }
  }
}
```

</details>

---

[&larr; `git.clone-repo`](/reference/slots/git/git.clone-repo/) | [all `git.*` slots](/reference/slots/git/) | [`git.create-repo` &rarr;](/reference/slots/git/git.create-repo/)

