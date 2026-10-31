---
title: "How to use [git.checkout]"
description: "How to use [git.checkout] - Switches branches in a repo."
generated: true
guide: true
---

This is the guide to [`git.checkout`](/reference/slots/git/git.checkout/), whose reference page has its arguments, constraints and declaration.

Switches branches in a repo. The repo path is the node value. The `branch` child node is required.

```
git.checkout:/modules/stripe/
   branch:feature-x
```

Optional argument:

* __[create]__ - Boolean, creates the branch

```
git.checkout:/modules/stripe/
   branch:feature-x
   create:true
```
