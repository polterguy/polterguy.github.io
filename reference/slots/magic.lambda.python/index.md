---
title: magic.lambda.python slot reference
description: Every slot in magic.lambda.python with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.python](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.python). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.python](/plugins/magic.lambda.python/)._

## [python.execute]

Runs a Python script or file in a subprocess and captures stdout, stderr, and exit code.

* **Returns**: Returns stdout in value and stderr and exit code as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[code]` | string | no | Inline Python code to execute |
| `[file]` | string | no | Python file to execute |
| `[stdin]` | string | no | Text written to standard input |
| `[working-directory]` | string | no | Working directory for the Python process |
| `[timeout]` | int | no | Execution timeout in seconds |
| `[*]` | string | no | Single command-line argument |

Guide: [How to use [python.execute]](/plugins/magic.lambda.python/#how-to-use-pythonexecute)

