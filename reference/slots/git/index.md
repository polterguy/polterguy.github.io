---
title: git.* slots
description: The 13 slots named git.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [git.branch.list]

Returns every branch in the local repository, marking which one is currently checked out.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns one unnamed child node per git branch name

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | bool | no | List remote branches. Default: `false`. |
| `[all]` | bool | no | List all branches. Default: `false`. |

Guide: [How to use [git.branch.list]](/plugins/magic.lambda.git/#how-to-use-gitbranchlist)

## [git.checkout]

Checks out a Git branch.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git checkout command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | yes | Branch to check out. |
| `[create]` | bool | no | Create the branch while checking it out. Default: `false`. |

Guide: [How to use [git.checkout]](/plugins/magic.lambda.git/#how-to-use-gitcheckout)

## [git.clone-repo]

Clones a Git repository.

* **Value** (`git-url`), required: Repository URL to clone
* **Returns**: Resolves to the git clone command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[path]` | string | no | Destination repository folder. |
| `[branch]` | string | no | Branch to clone. |
| `[depth]` | int | no | Shallow clone depth. |

Guide: [How to use [git.clone-repo]](/plugins/magic.lambda.git/#how-to-use-gitclone-repo)

## [git.commit]

Stages all changes in the repo and creates a new commit with the supplied message and author.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git commit command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[message]` | string | yes | Commit message. |
| `[all]` | bool | no | Stage all changed files before committing. Default: `true`. |
| `[amend]` | bool | no | Amend the previous commit. Default: `false`. |
| `[name]` | string | no | Author name for the commit; omitted falls back to git's configured identity. |
| `[email]` | string | no | Author email for the commit; omitted falls back to git's configured identity. |

Guide: [How to use [git.commit]](/plugins/magic.lambda.git/#how-to-use-gitcommit)

## [git.create-repo]

Initializes a Git repository.

* **Value** (`folder-path`), required: Folder path to initialize as a repository
* **Returns**: Resolves to the git init command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | no | Initial branch name. |
| `[bare]` | bool | no | Create a bare repository. Default: `false`. |

Guide: [How to use [git.create-repo]](/plugins/magic.lambda.git/#how-to-use-gitcreate-repo)

## [git.delete-repo]

Deletes a local Git repository.

* **Value** (`git-repo-path`), required: Repository path to delete

Guide: [How to use [git.delete-repo]](/plugins/magic.lambda.git/#how-to-use-gitdelete-repo)

## [git.diff]

Returns the unified diff between the working tree and HEAD, for the whole repository or one file.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns the unified diff text

| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | no | Repository-relative path of one file to diff; omitted diffs the whole repository. |

Guide: [How to use [git.diff]](/plugins/magic.lambda.git/#how-to-use-gitdiff)

## [git.fetch]

Fetches updates from a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git fetch command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to fetch from. Default: `origin`. |
| `[refspec]` | string | no | Optional refspec to fetch. |

Guide: [How to use [git.fetch]](/plugins/magic.lambda.git/#how-to-use-gitfetch)

## [git.pull]

Pulls updates from a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git pull command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to pull from. Default: `origin`. |
| `[branch]` | string | no | Branch to pull. |
| `[rebase]` | bool | no | Use rebase while pulling. Default: `false`. |
| `[ff-only]` | bool | no | Only allow fast-forward pulls. Default: `false`. |

Guide: [How to use [git.pull]](/plugins/magic.lambda.git/#how-to-use-gitpull)

## [git.push]

Pushes changes to a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git push command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to push to. Default: `origin`. |
| `[branch]` | string | no | Branch to push. |
| `[set-upstream]` | bool | no | Set upstream while pushing. Default: `false`. |

Guide: [How to use [git.push]](/plugins/magic.lambda.git/#how-to-use-gitpush)

## [git.remote.add]

Adds a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git remote add command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[name]` | string | no | Remote name. Default: `origin`. |
| `[url]` | string | yes | Remote URL. |

Guide: [How to use [git.remote.add]](/plugins/magic.lambda.git/#how-to-use-gitremoteadd)

## [git.restore]

Discards uncommitted changes by restoring one file from HEAD, or resets the whole working tree to HEAD including removal of untracked files.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | no | Repository-relative path of one file to restore from HEAD; omitted resets the whole working tree to HEAD and removes untracked files. |

Guide: [How to use [git.restore]](/plugins/magic.lambda.git/#how-to-use-gitrestore)

## [git.status]

Returns Git repository status.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns Git status text in value or, when structured, one child node per status line

| Argument | Type | Required | Description |
|---|---|---|---|
| `[porcelain]` | bool | no | Use porcelain status output. Default: `false`. |
| `[branch]` | bool | no | Include branch information. Default: `false`. |
| `[structured]` | bool | no | Return status lines as child nodes. Default: `false`. |

Guide: [How to use [git.status]](/plugins/magic.lambda.git/#how-to-use-gitstatus)

