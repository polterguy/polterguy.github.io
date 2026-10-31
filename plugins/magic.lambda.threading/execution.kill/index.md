---
title: "How to use [execution.kill]"
description: "How to use [execution.kill] - Cancels another running execution by its execution id."
generated: true
guide: true
---

The reference page of [`execution.kill`](/reference/slots/execution/execution.kill/) has its arguments, constraints and declaration.

Cancels another running execution by its execution id. This is useful when you have previously returned
an execution id to a caller and later want to stop that execution from another request or thread.

```
execution.kill:6c5a0bd3f7d64d6382d6cf3e7df5dc7c
```

The slot returns a boolean value indicating whether or not a matching live execution was found and
cancelled.
