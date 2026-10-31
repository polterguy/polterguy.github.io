---
title: "How to use [github.repo.create]"
description: "How to use [github.repo.create] - Creates a GitHub repository."
generated: true
guide: true
---

The reference page of [`github.repo.create`](/reference/slots/github/github.repo.create/) has its arguments, constraints and declaration.

Creates a GitHub repository. The repository name is the node value. Optionally provide an
organization owner and additional settings.

```
github.repo.create:my-new-repo
```

```
github.repo.create:my-new-repo
   owner:my-org
   private:true
   description:"Example repo"
   homepage:"https://example.com"
   auto-init:true
   default-branch:main
```

Optional arguments:

* __[owner]__ - Organization name to create repo within (omit to create under authenticated user)
* __[private]__ - Boolean
* __[description]__ - String
* __[homepage]__ - String
* __[auto-init]__ - Boolean
* __[default-branch]__ - String
* __[gitignore-template]__ - String
* __[license-template]__ - String
