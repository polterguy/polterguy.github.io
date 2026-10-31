---
title: magic.lambda.git
moved_anchors: {"how-to-use-gitbranchlist": "/reference/slots/git/git.branch.list/#guide", "how-to-use-gitcheckout": "/reference/slots/git/git.checkout/#guide", "how-to-use-gitclone-repo": "/reference/slots/git/git.clone-repo/#guide", "how-to-use-gitcommit": "/reference/slots/git/git.commit/#guide", "how-to-use-gitcreate-repo": "/reference/slots/git/git.create-repo/#guide", "how-to-use-gitdelete-repo": "/reference/slots/git/git.delete-repo/#guide", "how-to-use-gitdiff": "/reference/slots/git/git.diff/#guide", "how-to-use-gitfetch": "/reference/slots/git/git.fetch/#guide", "how-to-use-githubrepocreate": "/reference/slots/github/github.repo.create/#guide", "how-to-use-githubrepodelete": "/reference/slots/github/github.repo.delete/#guide", "how-to-use-githubrepolist": "/reference/slots/github/github.repo.list/#guide", "how-to-use-gitpull": "/reference/slots/git/git.pull/#guide", "how-to-use-gitpush": "/reference/slots/git/git.push/#guide", "how-to-use-gitremoteadd": "/reference/slots/git/git.remote.add/#guide", "how-to-use-gitrestore": "/reference/slots/git/git.restore/#guide", "how-to-use-gitstatus": "/reference/slots/git/git.status/#guide"}
---

The magic.lambda.git project provides Git and GitHub invocation capabilities for Magic and Hyperlambda. More specifically the
project contains the following 16 slots.

* __[\[git.clone-repo\]](/reference/slots/git/git.clone-repo/)__ - Clones a repository into a folder
* __[\[git.create-repo\]](/reference/slots/git/git.create-repo/)__ - Initializes a folder as a Git repository
* __[\[git.delete-repo\]](/reference/slots/git/git.delete-repo/)__ - Deletes an existing repository folder
* __[\[git.commit\]](/reference/slots/git/git.commit/)__ - Adds files and creates a commit
* __[\[git.push\]](/reference/slots/git/git.push/)__ - Pushes commits to a remote
* __[\[git.checkout\]](/reference/slots/git/git.checkout/)__ - Switches branches (optionally creating a new branch)
* __[git.merge]__ - Merges a branch into the current branch, or aborts a merge that stalled
* __[\[git.remote.add\]](/reference/slots/git/git.remote.add/)__ - Adds a Git remote
* __[\[git.fetch\]](/reference/slots/git/git.fetch/)__ - Fetches updates from a remote
* __[\[git.pull\]](/reference/slots/git/git.pull/)__ - Pulls updates from a remote
* __[\[git.status\]](/reference/slots/git/git.status/)__ - Shows repository status
* __[\[git.diff\]](/reference/slots/git/git.diff/)__ - Shows working tree changes relative to HEAD
* __[git.log]__ - Lists commits, one per line
* __[\[git.restore\]](/reference/slots/git/git.restore/)__ - Discards uncommitted changes for one file or the whole repository
* __[\[git.branch.list\]](/reference/slots/git/git.branch.list/)__ - Lists branches
* __[\[github.repo.create\]](/reference/slots/github/github.repo.create/)__ - Creates a GitHub repository
* __[\[github.repo.delete\]](/reference/slots/github/github.repo.delete/)__ - Deletes a GitHub repository
* __[\[github.repo.list\]](/reference/slots/github/github.repo.list/)__ - Lists GitHub repositories

All slots use the Git CLI under the hood. Paths are always resolved **inside** your _"/files/"_ folder using
`IRootResolver`, and folder paths **must** start with `/` and end with `/`.

**Notice** - The primary argument to all slots is always the node value. Optional arguments must be provided
as child nodes. Folder paths are required to start with `/` and end with `/`.

**Notice** - The given folder must itself be the repository root. Git's normal upward repository discovery
is disabled, implying a folder that isn't itself a repo throws instead of silently resolving to an
enclosing ancestor repository.


## GitHub authentication (HTTPS)

If you use HTTPS for GitHub, the slots will inject a per-command `Authorization` header using values from
`IConfiguration`. Add these keys:

```
magic:git:github:username
magic:git:github:token
magic:git:github:host
magic:git:github:api-base
```

The `host` value defaults to `github.com` if not provided. The `api-base` value defaults to
`https://api.github.com`, but should be set to your GitHub Enterprise API base URL if you use it
(typically `https://your-ghe-domain/api/v3`).


## How to use [git.merge]

Merges a branch into the current branch, or aborts a merge that stopped on conflicts. The repo path is the node
value, and the slot returns the output of the underlying `git merge` command. The merge is created without
opening a commit message editor.

* __[branch]__ - Branch to merge into the current branch. Mandatory unless **[abort]** is true, and the slot throws an exception if it is missing
* __[abort]__ - Boolean, default false, aborts a merge that stopped on conflicts instead of merging
* __[name]__ - Author name for the merge commit
* __[email]__ - Author email for the merge commit


## How to use [git.log]

Lists commits, one per line. The repo path is the node value, and the slot returns the lines as a single string.
Each line contains the side, the abbreviated hash, the author, the age and the subject of a commit, separated by
tab characters. The side is `<` for a commit only found on the left side of a range, and `>` for a commit only found
on the right side of a range.

* __[range]__ - Revision range, such as `HEAD...@{u}` to list the commits that differ from the upstream. If omitted, the commits of the current branch are listed
* __[limit]__ - Integer, default 30, maximum number of commits to return
