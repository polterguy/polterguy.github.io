---
title: "How to use [git.status]"
description: "How to use [git.status] - Shows repo status. The repo path is the node value."
generated: true
guide: true
---

This is the guide to [`git.status`](/reference/slots/git/git.status/), whose reference page has its arguments, constraints and declaration.

Shows repo status. The repo path is the node value. By default this returns the raw `git status` output.
If you provide `structured:true`, each line is returned as a `.` node.

```
git.status:/modules/stripe/
```

```
git.status:/modules/stripe/
   porcelain:true
   branch:true
   structured:true
```
