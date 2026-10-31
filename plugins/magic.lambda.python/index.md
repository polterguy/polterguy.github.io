---
title: magic.lambda.python
---

This project provides Python execution capabilities for Magic and Hyperlambda.

* __[python.execute]__ - Executes Python code or a Python file and returns stdout to caller

## How to use [python.execute]

You must provide either `code` or `file`.

```
python.execute
   code:@"
print('hello from python')
"
```

```
python.execute
   file:/modules/scripts/hello.py
   args
      .:--name
      .:Magic
```

Optional arguments:

* __[args]__ - Either a string of arguments or child nodes (each child is one argument)
* __[stdin]__ - String passed to stdin
* __[working-directory]__ - Working directory (must be under `/files/`)
* __[timeout]__ - Timeout in seconds (default 30)

Notes:

* File paths are resolved under `/files/` using `IRootResolver`.
* Non-zero exit codes throw a Hyperlambda exception with stderr/stdout.
