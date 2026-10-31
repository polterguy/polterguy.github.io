---
title: "[git.clone-repo]"
description: "git.clone-repo is a slot in the git namespace of Magic Cloud. Clones a Git repository."
generated: true
llms: false
slot_json: "/reference/slots/git/git.clone-repo/slot.json"
---

`git.clone-repo` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Clones a Git repository.

* **Value** (`git-url`), required: Repository URL to clone
* **Returns**: Resolves to the git clone command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[path]` | string | no | Destination repository folder. |
| `[branch]` | string | no | Branch to clone. |
| `[depth]` | int | no | Shallow clone depth. |

Guide: [How to use [git.clone-repo]](/plugins/magic.lambda.git/#how-to-use-gitclone-repo)

### JSON declaration

This is the complete declaration of `git.clone-repo`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.clone-repo",
  "description": "Clones a Git repository",
  "signature": {
    "input": {
      "kind": "git-url",
      "description": "Repository URL to clone",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "path": {
        "type": "string",
        "kind": "git-repo-path",
        "description": "Destination repository folder",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "branch": {
        "type": "string",
        "kind": "git-branch",
        "description": "Branch to clone",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "depth": {
        "type": "int",
        "description": "Shallow clone depth",
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
      "description": "Resolves to the git clone command output"
    }
  }
}
```

</details>

---

[&larr; `git.checkout`](/reference/slots/git/git.checkout/) | [all `git.*` slots](/reference/slots/git/) | [`git.commit` &rarr;](/reference/slots/git/git.commit/)

