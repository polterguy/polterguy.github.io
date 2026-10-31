---
title: "How to use [execution.throttle.create]"
description: "How to use [execution.throttle.create] - This slot creates, or replaces, a named throttle that [execution.throttle] then enforces."
generated: true
guide: true
---

The reference page of [`execution.throttle.create`](/reference/slots/execution/execution.throttle.create/) has its arguments, constraints and declaration.

This slot creates, or replaces, a named throttle that **[execution.throttle]** then enforces. It takes a **[limit]**, the number of invocations allowed per **[window]** of seconds, and **[per]**, which decides if the limit is counted per user, per IP address or globally. Invoking it with no arguments deletes the throttle. Below is an example.

```
// At the top of your endpoint file, allowing 10 invocations per user per minute.
execution.throttle.create:my-endpoint
   limit:10
execution.throttle:my-endpoint
```
