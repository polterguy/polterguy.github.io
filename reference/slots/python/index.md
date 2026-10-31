---
title: python.* slots
description: The 1 slots named python.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [python.execute]

Runs a Python script or file in a subprocess and captures stdout, stderr, and exit code.

* **Returns**: Returns stdout in value and stderr and exit code as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | string\|lambda | no | Command-line arguments as a shell-like string or child values. |
| `[args]` / _any node name_ | string | no | Single command-line argument. Can be repeated. |
| `[code]` | string | no | Inline Python code to execute. |
| `[file]` | string | no | Python file to execute. |
| `[stdin]` | string | no | Text written to standard input. |
| `[timeout]` | int | no | Execution timeout in seconds. Default: `30`. |
| `[working-directory]` | string | no | Working directory for the Python process. |

* **Constraint** (ExactlyOneOf): Exactly one code source must be supplied (`[code]`, `[file]`)

Guide: [How to use [python.execute]](/plugins/magic.lambda.python/#how-to-use-pythonexecute)

