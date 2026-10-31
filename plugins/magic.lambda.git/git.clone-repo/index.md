---
title: "How to use [git.clone-repo]"
description: "How to use [git.clone-repo] - Clones the specified URL."
generated: true
guide: true
---

This is the guide to [`git.clone-repo`](/reference/slots/git/git.clone-repo/), whose reference page has its arguments, constraints and declaration.

Clones the specified URL. The URL is the node value. Optionally provide `path`, `branch`, and `depth`.

```
git.clone-repo:"https://github.com/polterguy/stripe.git"
   path:/modules/stripe/
```

```
git.clone-repo:"https://github.com/polterguy/stripe.git"
   path:/modules/stripe/
   branch:main
   depth:1
```
