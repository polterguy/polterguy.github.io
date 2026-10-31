---
title: "How to use [vocabulary]"
description: "How to use [vocabulary] - Returns the name of every static slot in your system, optionally passing in a string, or an expression leading to a string, which is a filtering condition, where the slot must start with the..."
generated: true
guide: true
---

The reference page of [`vocabulary`](/reference/slots/core/vocabulary/) has its arguments, constraints and declaration.

Returns the name of every static slot in your system, optionally passing in a string, or an expression leading to
a string, which is a filtering condition, where the slot must _start_ with the filter specified to be considered
a part of the end result.

```
// Returns ALL slots in your system.
vocabulary

// Returns only slots starting with [io.file]
vocabulary:io.file
```

Notice, inside a **[whitelist]** invocation this slot only returns the slots the whitelist allows, so it
tells the code running inside what it can actually invoke. A whitelisted slot that is pinned to an argument
is returned once by name, regardless of how many different arguments it is pinned to.
