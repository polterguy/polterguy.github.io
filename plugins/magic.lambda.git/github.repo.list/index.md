---
title: "How to use [github.repo.list]"
description: "How to use [github.repo.list] - Lists GitHub repositories."
generated: true
guide: true
---

This is the guide to [`github.repo.list`](/reference/slots/github/github.repo.list/), whose reference page has its arguments, constraints and declaration.

Lists GitHub repositories. If `owner` is omitted, it will list repositories visible to the
authenticated user. If `owner` is provided, it will list repositories for the organization (not a user).

**Notice** - For the authenticated user endpoint, GitHub does not allow combining `visibility` and `type`.
Provide only one of them.

The result is returned as a list, each containing the following fields:

* `name`
* `full_name`
* `private`
* `html_url`
* `description`
* `default_branch`

```
github.repo.list
   owner:my-org
   visibility:all
   type:all
   per-page:100
   page:1
```
