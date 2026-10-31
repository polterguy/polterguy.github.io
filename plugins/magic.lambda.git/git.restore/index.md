---
title: "How to use [git.restore]"
description: "How to use [git.restore] - Discards uncommitted changes."
generated: true
guide: true
---

The reference page of [`git.restore`](/reference/slots/git/git.restore/) has its arguments, constraints and declaration.

Discards uncommitted changes. The repo path is the node value. With a repo-relative `file`, that one file is
restored from HEAD in both index and working tree. Without `file`, the whole working tree is reset to HEAD
**and untracked files and folders are removed**, leaving the folder identical to the last commit.

```
git.restore:/modules/stripe/
   file:README.md
```

```
git.restore:/modules/stripe/
```
