---
title: "[github.repo.delete]"
description: "github.repo.delete is a slot in the github namespace of Magic Cloud. Deletes a GitHub repository."
generated: true
llms: "guide"
slot_json: "/reference/slots/github/github.repo.delete/slot.json"
---

`github.repo.delete` is a slot in the `github` namespace, in Hyperlambda, the language of Magic Cloud. Deletes a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Returns true after the repository has been deleted

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Repository owner; omit to delete from the authenticated user. |

### Guide

<!-- guide -->
Deletes a GitHub repository. The repository name is the node value. The `owner` argument is optional,
and defaults to the configured `magic:git:github:username`.

```
github.repo.delete:my-old-repo
```

```
github.repo.delete:my-old-repo
   owner:my-org
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `github.repo.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "github.repo.delete",
  "description": "Deletes a GitHub repository",
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
        "description": "Repository owner; omit to delete from the authenticated user",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true after the repository has been deleted"
    }
  }
}
```

</details>

---

[&larr; `github.repo.create`](/reference/slots/github/github.repo.create/) | [all `github.*` slots](/reference/slots/github/) | [`github.repo.list` &rarr;](/reference/slots/github/github.repo.list/)

