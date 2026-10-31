---
title: "execution.* slots"
description: "The 4 slots named execution.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

4 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`execution.kill`](/reference/slots/execution/execution.kill/) | Cancels a running execution by execution ID. |
| [`execution.throttle`](/reference/slots/execution/execution.throttle/) | Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded. |
| [`execution.throttle.create`](/reference/slots/execution/execution.throttle.create/) | Creates or replaces a named throttle enforced by [execution.throttle]; declaring an unchanged configuration keeps the existing throttle and its counters, while invoking the slot without arguments deletes the throttle instead. |
| [`execution.timeout`](/reference/slots/execution/execution.timeout/) | Sets a timeout in milliseconds for the current execution. |

