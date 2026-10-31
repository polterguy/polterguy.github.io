---
title: "[git.delete-repo]"
description: "git.delete-repo is a slot in the git namespace of Magic Cloud. Deletes a local Git repository."
generated: true
llms: false
slot_json: "/reference/slots/git/git.delete-repo/slot.json"
---

`git.delete-repo` is a slot in the `git` namespace, in Hyperlambda, the language of Magic Cloud. Deletes a local Git repository.

* **Value** (`git-repo-path`), required: Repository path to delete

Guide: [How to use [git.delete-repo]](/plugins/magic.lambda.git/#how-to-use-gitdelete-repo)

### JSON declaration

This is the complete declaration of `git.delete-repo`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "git.delete-repo",
  "description": "Deletes a local Git repository",
  "signature": {
    "input": {
      "kind": "git-repo-path",
      "description": "Repository path to delete",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `git.create-repo`](/reference/slots/git/git.create-repo/) | [all `git.*` slots](/reference/slots/git/) | [`git.diff` &rarr;](/reference/slots/git/git.diff/)

