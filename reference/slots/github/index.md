---
title: github.* slots
description: The 3 slots named github.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [github.repo.create]

Creates a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Resolves to the created GitHub repository as child nodes projected from the API response

| Argument | Type | Required | Description |
|---|---|---|---|
| `[auto-init]` | bool | no | Initialize the repository. Default: `false`. |
| `[default-branch]` | string | no | Default branch name. |
| `[description]` | string | no | Repository description. |
| `[gitignore-template]` | string | no | GitHub gitignore template. |
| `[homepage]` | string | no | Repository homepage URL. |
| `[license-template]` | string | no | GitHub license template. |
| `[owner]` | string | no | Organization owner; omit to create under the authenticated user. |
| `[private]` | bool | no | Whether the repository is private. Default: `false`. |

Guide: [How to use [github.repo.create]](/plugins/magic.lambda.git/#how-to-use-githubrepocreate)

## [github.repo.delete]

Deletes a GitHub repository.

* **Value** (`github-repo-name`), required: GitHub repository name
* **Returns**: Returns true after the repository has been deleted

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Repository owner; omit to delete from the authenticated user. |

Guide: [How to use [github.repo.delete]](/plugins/magic.lambda.git/#how-to-use-githubrepodelete)

## [github.repo.list]

Lists GitHub repositories using child-node filters.

* **Returns**: Returns one child node per GitHub repository with the projected repository metadata

| Argument | Type | Required | Description |
|---|---|---|---|
| `[owner]` | string | no | Organization owner; omit to list authenticated user repositories. |
| `[page]` | int | no | Page number. |
| `[per-page]` | int | no | Number of repositories per page. |
| `[type]` | string | no | Repository type filter. |
| `[visibility]` | string | no | Repository visibility filter. |

Guide: [How to use [github.repo.list]](/plugins/magic.lambda.git/#how-to-use-githubrepolist)

