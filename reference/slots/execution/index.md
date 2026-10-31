---
title: execution.* slots
description: The 4 slots named execution.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [execution.kill]

Cancels a running execution by execution ID.

* **Value** (`execution-id`), required: Execution ID to cancel
* **Returns**: Returns true if the execution was cancelled

Guide: [How to use [execution.kill]](/plugins/magic.lambda.threading/#how-to-use-executionkill)

## [execution.throttle]

Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded.

* **Value** (`throttle-name`), required: Name of the throttle to enforce, as previously declared with [execution.throttle.create]

Guide: [How to use [execution.throttle]](/plugins/magic.lambda.threading/#how-to-use-executionthrottle)

## [execution.throttle.create]

Creates or replaces a named throttle enforced by [execution.throttle]; declaring an unchanged configuration keeps the existing throttle and its counters, while invoking the slot without arguments deletes the throttle instead.

* **Value** (`throttle-name`), required: Name of the throttle to create, replace or delete

| Argument | Type | Required | Description |
|---|---|---|---|
| `[limit]` | int | no | Maximum number of invocations allowed per window; mandatory when creating a throttle, while invoking the slot without any arguments deletes the throttle instead. |
| `[per]` | string | no | How to partition the limit; 'user' partitions per authenticated username, 'ip' per client IP address, and 'global' shares one limit between all callers. Default: `user when authenticated, otherwise ip`. |
| `[window]` | int | no | Window length in seconds. Default: `60`. |

## [execution.timeout]

Sets a timeout in milliseconds for the current execution.

* **Value** (`timeout-ms,integer,number`), required: Timeout in milliseconds for the current execution
* **Returns**: Returns true if the timeout was applied

Guide: [How to use [execution.timeout]](/plugins/magic.lambda.threading/#how-to-use-executiontimeout)

