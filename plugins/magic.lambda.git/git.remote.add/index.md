---
title: "How to use [git.remote.add]"
description: "How to use [git.remote.add] - Adds a remote to a repository."
generated: true
guide: true
---

The reference page of [`git.remote.add`](/reference/slots/git/git.remote.add/) has its arguments, constraints and declaration.

Adds a remote to a repository. The repo path is the node value. The `url` child node is required.
The `name` child node defaults to `origin` if omitted.

```
git.remote.add:/modules/stripe/
   url:"https://github.com/polterguy/stripe.git"
```

```
git.remote.add:/modules/stripe/
   name:origin
   url:"https://github.com/polterguy/stripe.git"
```
