---
title: "[git.checkout]"
description: "git.checkout is a slot in the git namespace of Magic Cloud. Checks out a Git branch."
generated: true
llms: "guide"
slot_json: "/reference/slots/git/git.checkout/slot.json"
---

`git.checkout` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Checks out a Git branch.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git checkout command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | yes | Branch to check out. |
| `[create]` | bool | no | Create the branch while checking it out. Default: `false`. |

### Guide

<!-- guide -->
Switches branches in a repo. The repo path is the node value. The `branch` child node is required.

```
git.checkout:/modules/stripe/
   branch:feature-x
```

Optional argument:

* __[create]__ - Boolean, creates the branch

```
git.checkout:/modules/stripe/
   branch:feature-x
   create:true
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.git](/plugins/magic.lambda.git/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `git.checkout`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.checkout",
  "description": "Checks out a Git branch",
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
        "description": "Branch to check out",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "create": {
        "type": "bool",
        "description": "Create the branch while checking it out",
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
      "description": "Resolves to the git checkout command output"
    }
  }
}
```

</details>

---

[&larr; `git.branch.list`](/reference/slots/git/git.branch.list/) | [all `git.*` slots](/reference/slots/git/) | [`git.clone-repo` &rarr;](/reference/slots/git/git.clone-repo/)

