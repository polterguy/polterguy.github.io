---
title: "[git.create-repo]"
description: "git.create-repo is a slot in the git namespace of Magic Cloud. Initializes a Git repository."
generated: true
llms: "guide"
slot_json: "/reference/slots/git/git.create-repo/slot.json"
---

`git.create-repo` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Initializes a Git repository.

* **Value** (`folder-path`), required: Folder path to initialize as a repository
* **Returns**: Resolves to the git init command output

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | no | Initial branch name. |
| `[bare]` | bool | no | Create a bare repository. Default: `false`. |

### Guide

<!-- guide -->
Initializes a folder as a repository. The folder path is the node value.

```
git.create-repo:/modules/new-repo/
```

Optional arguments:

* __[branch]__ - Initial branch name
* __[bare]__ - Boolean, creates a bare repo

```
git.create-repo:/modules/new-repo/
   branch:main
   bare:false
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `git.create-repo`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.create-repo",
  "description": "Initializes a Git repository",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to initialize as a repository",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "branch": {
        "type": "string",
        "kind": "git-branch",
        "description": "Initial branch name",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "bare": {
        "type": "bool",
        "description": "Create a bare repository",
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
      "description": "Resolves to the git init command output"
    }
  }
}
```

</details>

---

[&larr; `git.commit`](/reference/slots/git/git.commit/) | [all `git.*` slots](/reference/slots/git/) | [`git.delete-repo` &rarr;](/reference/slots/git/git.delete-repo/)

