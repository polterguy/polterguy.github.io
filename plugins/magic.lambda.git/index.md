---
title: magic.lambda.git
---

The magic.lambda.git project provides Git invocation capabilities for Magic and Hyperlambda. More specifically the
project contains the following 6 slots.

* __[git.clone-repo]__ - Clones a repository into a folder
* __[git.create-repo]__ - Initializes a folder as a Git repository
* __[git.delete-repo]__ - Deletes an existing repository folder
* __[git.commit]__ - Adds files and creates a commit
* __[git.push]__ - Pushes commits to a remote
* __[git.checkout]__ - Switches branches (optionally creating a new branch)

All slots use the Git CLI under the hood. Paths are always resolved **inside** your _"/files/"_ folder using
`IRootResolver`, and folder paths **must** start with `/` and end with `/`.

**Notice** - The primary argument to all slots is always the node value. Optional arguments must be provided
as child nodes.

## GitHub authentication (HTTPS)

If you use HTTPS for GitHub, the slots will inject a per-command `Authorization` header using values from
`IConfiguration`. Add these keys:

```
magic:git:github:username
magic:git:github:token
magic:git:github:host
```

The `host` value defaults to `github.com` if not provided.

## How to use [git.clone-repo]

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

## How to use [git.create-repo]

Initializes a folder as a repository. The folder path is the node value.

```
git.create-repo:/modules/new-repo/
```

Optional arguments:

* __[branch]__ - Initial branch name
* __[bare]__ - Boolean, creates a bare repo

```
git.create-repo:/modules/new-repo/
   branch:main
   bare:false
```

## How to use [git.delete-repo]

Deletes the repository folder. The folder path is the node value.

```
git.delete-repo:/modules/old-repo/
```

## How to use [git.commit]

Creates a commit. The repo path is the node value. The `message` child node is required.

```
git.commit:/modules/stripe/
   message:"Initial commit"
```

Optional arguments:

* __[all]__ - Boolean, default true, runs `git add -A` before commit
* __[amend]__ - Boolean, amends the previous commit

```
git.commit:/modules/stripe/
   message:"Fix issue"
   all:true
   amend:false
```

## How to use [git.push]

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

## How to use [git.checkout]

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
