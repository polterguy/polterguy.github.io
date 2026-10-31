---
title: "How to use [git.commit]"
description: "How to use [git.commit] - Creates a commit. The repo path is the node value."
generated: true
guide: true
---

The reference page of [`git.commit`](/reference/slots/git/git.commit/) has its arguments, constraints and declaration.

Creates a commit. The repo path is the node value. The `message` child node is required.

```
git.commit:/modules/stripe/
   message:Initial commit
```

Optional arguments:

* __[all]__ - Boolean, default true, runs `git add -A` before commit
* __[amend]__ - Boolean, amends the previous commit
* __[name]__ - Author name for the commit, falling back to git's configured identity when omitted
* __[email]__ - Author email for the commit, falling back to git's configured identity when omitted

Author identity is injected per invocation the same way authentication is, implying nothing is ever
written to the global git configuration on the server.

Optional arguments:

* __[all]__ - Boolean, default true, runs `git add -A` before commit
* __[amend]__ - Boolean, amends the previous commit

```
git.commit:/modules/stripe/
   message:"Fix issue"
   all:true
   amend:false
```
