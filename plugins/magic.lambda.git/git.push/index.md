---
title: "How to use [git.push]"
description: "How to use [git.push] - Pushes to a remote. The repo path is the node value."
generated: true
guide: true
---

This is the guide to [`git.push`](/reference/slots/git/git.push/), whose reference page has its arguments, constraints and declaration.

Pushes to a remote. The repo path is the node value.

```
git.push:/modules/stripe/
   remote:origin
   branch:main
```

Optional arguments:

* __[set-upstream]__ - Boolean, adds `-u` to the push

```
git.push:/modules/stripe/
   remote:origin
   branch:main
   set-upstream:true
```
