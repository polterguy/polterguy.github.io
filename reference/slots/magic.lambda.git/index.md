---
title: magic.lambda.git slot reference
description: Every slot in magic.lambda.git with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.git](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.git). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.git](/plugins/magic.lambda.git/)._

## [git.branch.list]

Returns every branch in the local repository, marking which one is currently checked out.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns one unnamed child node per git branch name

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | bool | no | List remote branches |
| `[all]` | bool | no | List all branches |

Guide: [How to use [git.branch.list]](/plugins/magic.lambda.git/#how-to-use-gitbranchlist)

## [git.checkout]

Checks out a Git branch.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git checkout command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | yes | Branch to check out |
| `[create]` | bool | no | Create the branch while checking it out |

Guide: [How to use [git.checkout]](/plugins/magic.lambda.git/#how-to-use-gitcheckout)

## [git.clone-repo]

Clones a Git repository.

* **Value** (`git-url`), required: Repository URL to clone
* **Returns**: Resolves to the git clone command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[path]` | string | no | Destination repository folder |
| `[branch]` | string | no | Branch to clone |
| `[depth]` | int | no | Shallow clone depth |

Guide: [How to use [git.clone-repo]](/plugins/magic.lambda.git/#how-to-use-gitclone-repo)

## [git.commit]

Stages all changes in the repo and creates a new commit with the supplied message and author.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git commit command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[message]` | string | yes | Commit message |
| `[all]` | bool | no | Stage all changed files before committing |
| `[amend]` | bool | no | Amend the previous commit |
| `[name]` | string | no | Author name for the commit; omitted falls back to git's configured identity |
| `[email]` | string | no | Author email for the commit; omitted falls back to git's configured identity |

Guide: [How to use [git.commit]](/plugins/magic.lambda.git/#how-to-use-gitcommit)

## [git.create-repo]

Initializes a Git repository.

* **Value** (`folder-path`), required: Folder path to initialize as a repository
* **Returns**: Resolves to the git init command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | no | Initial branch name |
| `[bare]` | bool | no | Create a bare repository |

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
| `[file]` | string | no | Repository-relative path of one file to diff; omitted diffs the whole repository |

Guide: [How to use [git.diff]](/plugins/magic.lambda.git/#how-to-use-gitdiff)

## [git.fetch]

Fetches updates from a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git fetch command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to fetch from |
| `[refspec]` | string | no | Optional refspec to fetch |

Guide: [How to use [git.fetch]](/plugins/magic.lambda.git/#how-to-use-gitfetch)

## [git.log]

Lists commits, one per line as side, hash, author, age and subject separated by tabs, where side is '<' for a commit only on the left of a range and '>' for one only on the right.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the commit lines

| Argument | Type | Required | Description |
|---|---|---|---|
| `[range]` | string | no | Revision range, such as 'HEAD...@{u}' for the commits that differ from the upstream; omitted lists the current branch |
| `[limit]` | int | no | Maximum number of commits to return |

Guide: [How to use [git.log]](/plugins/magic.lambda.git/#how-to-use-gitlog)

## [git.merge]

Merges a Git branch into the current branch, or aborts a merge that stopped on conflicts.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git merge command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[branch]` | string | no | Branch to merge into the current branch, required unless [abort] is true |
| `[abort]` | bool | no | Abort a merge that stopped on conflicts |
| `[name]` | string | no | Author name of the merge commit |
| `[email]` | string | no | Author email of the merge commit |

Guide: [How to use [git.merge]](/plugins/magic.lambda.git/#how-to-use-gitmerge)

## [git.pull]

Pulls updates from a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git pull command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to pull from |
| `[branch]` | string | no | Branch to pull |
| `[rebase]` | bool | no | Use rebase while pulling |
| `[merge]` | bool | no | Merge while pulling, which is what lets a diverged branch be pulled |
| `[ff-only]` | bool | no | Only allow fast-forward pulls |
| `[name]` | string | no | Author name of the merge commit a merging pull creates |
| `[email]` | string | no | Author email of the merge commit a merging pull creates |

Guide: [How to use [git.pull]](/plugins/magic.lambda.git/#how-to-use-gitpull)

## [git.push]

Pushes changes to a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git push command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[remote]` | string | no | Remote to push to |
| `[branch]` | string | no | Branch to push |
| `[set-upstream]` | bool | no | Set upstream while pushing |

Guide: [How to use [git.push]](/plugins/magic.lambda.git/#how-to-use-gitpush)

## [git.remote.add]

Adds a Git remote.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git remote add command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[name]` | string | no | Remote name |
| `[url]` | string | yes | Remote URL |

Guide: [How to use [git.remote.add]](/plugins/magic.lambda.git/#how-to-use-gitremoteadd)

## [git.restore]

Discards uncommitted changes by restoring one file from HEAD, or resets the whole working tree to HEAD including removal of untracked files.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Resolves to the git command output

| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | no | Repository-relative path of one file to restore from HEAD; omitted resets the whole working tree to HEAD and removes untracked files |

Guide: [How to use [git.restore]](/plugins/magic.lambda.git/#how-to-use-gitrestore)

## [git.status]

Returns Git repository status.

* **Value** (`git-repo-path`), required: Repository path
* **Returns**: Returns Git status text in value or, when structured, one child node per status line

| Argument | Type | Required | Description |
|---|---|---|---|
| `[porcelain]` | bool | no | Use porcelain status output |
| `[branch]` | bool | no | Include branch information |
| `[structured]` | bool | no | Return status lines as child nodes |

Guide: [How to use [git.status]](/plugins/magic.lambda.git/#how-to-use-gitstatus)

## [github.repo.create]

Creates a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Resolves to the created GitHub repository as child nodes projected from the API response

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Organization owner; omit to create under the authenticated user |
| `[private]` | bool | no | Whether the repository is private |
| `[description]` | string | no | Repository description |
| `[homepage]` | string | no | Repository homepage URL |
| `[auto-init]` | bool | no | Initialize the repository |
| `[default-branch]` | string | no | Default branch name |
| `[gitignore-template]` | string | no | GitHub gitignore template |
| `[license-template]` | string | no | GitHub license template |

Guide: [How to use [github.repo.create]](/plugins/magic.lambda.git/#how-to-use-githubrepocreate)

## [github.repo.delete]

Deletes a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Returns true after the repository has been deleted

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Repository owner; omit to delete from the authenticated user |

Guide: [How to use [github.repo.delete]](/plugins/magic.lambda.git/#how-to-use-githubrepodelete)

## [github.repo.list]

Lists GitHub repositories using child-node filters.

* **Returns**: Returns one child node per GitHub repository with the projected repository metadata

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Organization owner; omit to list authenticated user repositories |
| `[visibility]` | string | no | Repository visibility filter |
| `[type]` | string | no | Repository type filter |
| `[per-page]` | int | no | Number of repositories per page |
| `[page]` | int | no | Page number |

Guide: [How to use [github.repo.list]](/plugins/magic.lambda.git/#how-to-use-githubrepolist)

