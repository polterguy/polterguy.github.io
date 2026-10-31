---
title: "How to use [execution.timeout]"
description: "How to use [execution.timeout] - Configures a timeout for the current execution context."
generated: true
guide: true
---

This is the guide to [`execution.timeout`](/reference/slots/execution/execution.timeout/), whose reference page has its arguments, constraints and declaration.

Configures a timeout for the **current** execution context. The value must be a positive number of
milliseconds and is interpreted relative to _now_.

```
execution.timeout:30000
```

The above means the current execution may continue for at most 30 more seconds. The slot returns a
boolean value indicating whether or not the timeout actually tightened the current deadline.

If multiple timeouts are applied to the same execution, the earliest deadline wins. Any child work
created through **[fork]** inherits the same execution context, implying the timeout applies to
forked work too.
