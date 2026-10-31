---
title: "[github.repo.create]"
description: "github.repo.create is a slot in the github namespace of Magic Cloud. Creates a GitHub repository."
generated: true
llms: false
slot_json: "/reference/slots/github/github.repo.create/slot.json"
---

`github.repo.create` is a slot in the `github` namespace, in Hyperlambda, the language of Magic Cloud. Creates a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Resolves to the created GitHub repository as child nodes projected from the API response

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Organization owner; omit to create under the authenticated user. |
| `[private]` | bool | no | Whether the repository is private. Default: `false`. |
| `[description]` | string | no | Repository description. |
| `[homepage]` | string | no | Repository homepage URL. |
| `[auto-init]` | bool | no | Initialize the repository. Default: `false`. |
| `[default-branch]` | string | no | Default branch name. |
| `[gitignore-template]` | string | no | GitHub gitignore template. |
| `[license-template]` | string | no | GitHub license template. |

### Guide

[How to use `github.repo.create`](/plugins/magic.lambda.git/github.repo.create/)

### JSON declaration

This is the complete declaration of `github.repo.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "github.repo.create",
  "description": "Creates a GitHub repository",
  "signature": {
    "input": {
      "kind": "github-repo-name",
      "description": "GitHub repository name",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "owner": {
        "type": "string",
        "kind": "github-owner",
        "description": "Organization owner; omit to create under the authenticated user",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "private": {
        "type": "bool",
        "description": "Whether the repository is private",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "description": {
        "type": "string",
        "kind": "git-repo-description",
        "description": "Repository description",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "homepage": {
        "type": "string",
        "kind": "url",
        "description": "Repository homepage URL",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "auto-init": {
        "type": "bool",
        "description": "Initialize the repository",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "default-branch": {
        "type": "string",
        "kind": "git-branch",
        "description": "Default branch name",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "gitignore-template": {
        "type": "string",
        "kind": "gitignore-template",
        "description": "GitHub gitignore template",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "license-template": {
        "type": "string",
        "kind": "license-template",
        "description": "GitHub license template",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "github-repository,lambda-tree",
      "description": "Resolves to the created GitHub repository as child nodes projected from the API response"
    }
  }
}
```

</details>

---

[all `github.*` slots](/reference/slots/github/) | [`github.repo.delete` &rarr;](/reference/slots/github/github.repo.delete/)

