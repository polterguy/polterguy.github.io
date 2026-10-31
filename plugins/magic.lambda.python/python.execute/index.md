---
title: "How to use [python.execute]"
description: "How to use [python.execute] - You must provide either code or file."
generated: true
guide: true
---

The reference page of [`python.execute`](/reference/slots/python/python.execute/) has its arguments, constraints and declaration.

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
