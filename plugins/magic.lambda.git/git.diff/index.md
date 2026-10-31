---
title: "How to use [git.diff]"
description: "How to use [git.diff] - Shows the unified diff between the working tree and HEAD."
generated: true
guide: true
---

This is the guide to [`git.diff`](/reference/slots/git/git.diff/), whose reference page has its arguments, constraints and declaration.

Shows the unified diff between the working tree and HEAD. The repo path is the node value. By default the
whole repository is diffed, while providing a repo-relative `file` restricts the diff to that one file.
Untracked files have no diff, since git knows nothing about them yet.

```
git.diff:/modules/stripe/
```

```
git.diff:/modules/stripe/
   file:README.md
```
