---
title: "How to use [git.merge]"
description: "How to use [git.merge] - Merges a branch into the current branch, or aborts a merge that stopped on conflicts."
generated: true
guide: true
---

The reference page of [`git.merge`](/reference/slots/git/git.merge/) has its arguments, constraints and declaration.

Merges a branch into the current branch, or aborts a merge that stopped on conflicts. The repo path is the node
value, and the slot returns the output of the underlying `git merge` command. The merge is created without
opening a commit message editor.

* __[branch]__ - Branch to merge into the current branch. Mandatory unless **[abort]** is true, and the slot throws an exception if it is missing
* __[abort]__ - Boolean, default false, aborts a merge that stopped on conflicts instead of merging
* __[name]__ - Author name for the merge commit
* __[email]__ - Author email for the merge commit
