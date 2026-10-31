---
title: "[github.repo.delete]"
description: "github.repo.delete is a slot in the github namespace of Magic Cloud. Deletes a GitHub repository."
generated: true
llms: false
slot_json: "/reference/slots/github/github.repo.delete/slot.json"
---

`github.repo.delete` is a slot in the `github` namespace, in Hyperlambda, the language of Magic Cloud. Deletes a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Returns true after the repository has been deleted

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Repository owner; omit to delete from the authenticated user. |

Guide: [How to use [github.repo.delete]](/plugins/magic.lambda.git/#how-to-use-githubrepodelete)

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

