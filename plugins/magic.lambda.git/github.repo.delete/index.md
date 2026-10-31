---
title: "How to use [github.repo.delete]"
description: "How to use [github.repo.delete] - Deletes a GitHub repository."
generated: true
guide: true
---

The reference page of [`github.repo.delete`](/reference/slots/github/github.repo.delete/) has its arguments, constraints and declaration.

Deletes a GitHub repository. The repository name is the node value. The `owner` argument is optional,
and defaults to the configured `magic:git:github:username`.

```
github.repo.delete:my-old-repo
```

```
github.repo.delete:my-old-repo
   owner:my-org
```
