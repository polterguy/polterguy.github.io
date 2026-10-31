---
title: "How to use [git.pull]"
description: "How to use [git.pull] - Pulls updates from a remote."
generated: true
guide: true
---

The reference page of [`git.pull`](/reference/slots/git/git.pull/) has its arguments, constraints and declaration.

Pulls updates from a remote. The repo path is the node value. The `remote` child node defaults to `origin`.

```
git.pull:/modules/stripe/
```

```
git.pull:/modules/stripe/
   remote:origin
   branch:main
   rebase:false
   ff-only:false
```
