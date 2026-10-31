---
title: "[github.repo.list]"
description: "github.repo.list is a slot in the github namespace of Magic Cloud. Lists GitHub repositories using child-node filters."
generated: true
llms: false
slot_json: "/reference/slots/github/github.repo.list/slot.json"
---

`github.repo.list` is a slot in the `github` namespace, in Hyperlambda, the language of Magic Cloud. Lists GitHub repositories using child-node filters.

* **Returns**: Returns one child node per GitHub repository with the projected repository metadata

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Organization owner; omit to list authenticated user repositories. |
| `[visibility]` | string | no | Repository visibility filter. |
| `[type]` | string | no | Repository type filter. |
| `[per-page]` | int | no | Number of repositories per page. |
| `[page]` | int | no | Page number. |

### Guide

[How to use `github.repo.list`](/plugins/magic.lambda.git/github.repo.list/)

### JSON declaration

This is the complete declaration of `github.repo.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "github.repo.list",
  "description": "Lists GitHub repositories using child-node filters",
  "signature": {
    "children": {
      "owner": {
        "type": "string",
        "kind": "github-owner",
        "description": "Organization owner; omit to list authenticated user repositories",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "visibility": {
        "type": "string",
        "kind": "repo-visibility",
        "description": "Repository visibility filter",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "type": {
        "type": "string",
        "kind": "repo-type",
        "description": "Repository type filter",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "per-page": {
        "type": "int",
        "description": "Number of repositories per page",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "page": {
        "type": "int",
        "description": "Page number",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "github-repository-list,node-list",
      "element-kind": "github-repository,lambda-tree",
      "description": "Returns one child node per GitHub repository with the projected repository metadata"
    }
  }
}
```

</details>

---

[&larr; `github.repo.delete`](/reference/slots/github/github.repo.delete/) | [all `github.*` slots](/reference/slots/github/)

