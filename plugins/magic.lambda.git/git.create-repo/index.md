---
title: "How to use [git.create-repo]"
description: "How to use [git.create-repo] - Initializes a folder as a repository."
generated: true
guide: true
---

This is the guide to [`git.create-repo`](/reference/slots/git/git.create-repo/), whose reference page has its arguments, constraints and declaration.

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
