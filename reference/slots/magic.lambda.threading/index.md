---
title: magic.lambda.threading slot reference
description: Every slot in magic.lambda.threading with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.threading](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.threading). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.threading](/plugins/magic.lambda.threading/)._

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
| `[limit]` | int | no | Maximum number of invocations allowed per window; mandatory when creating a throttle, while invoking the slot without any arguments deletes the throttle instead |
| `[window]` | int | no | Window length in seconds |
| `[per]` | string | no | How to partition the limit; 'user' partitions per authenticated username, 'ip' per client IP address, and 'global' shares one limit between all callers |

## [execution.timeout]

Sets a timeout in milliseconds for the current execution.

* **Value** (`timeout-ms,integer,number`), required: Timeout in milliseconds for the current execution
* **Returns**: Returns true if the timeout was applied

Guide: [How to use [execution.timeout]](/plugins/magic.lambda.threading/#how-to-use-executiontimeout)

## [fork]

Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | lambda | yes | Executable child slot evaluated on the forked thread |

Guide: [How to use [fork]](/plugins/magic.lambda.threading/#how-to-use-fork)

## [join]

Waits for one or more child [fork] operations to finish before proceeding.

* **Returns**: Resolves to the completed [fork] child nodes with evaluated body node values and children preserved

| Argument | Type | Required | Description |
|---|---|---|---|
| `[fork]` | lambda | yes | Fork body to start and wait for; evaluated body node values and children are preserved in the completed fork node |

Guide: [How to use [join]](/plugins/magic.lambda.threading/#how-to-use-join)

## [semaphore]

Serializes access to a critical section by name; only one thread at a time can enter a given semaphore.

* **Value** (`semaphore-name`), required: Semaphore name used to serialize access

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | lambda | yes | Executable child lambda object evaluated while the named semaphore is held |

Guide: [How to use [semaphore]](/plugins/magic.lambda.threading/#how-to-use-semaphore)

## [sleep]

Delays execution for the specified number of milliseconds.

* **Value** (`timeout-ms,integer,number`), required: Delay in milliseconds

Guide: [How to use [sleep]](/plugins/magic.lambda.threading/#how-to-use-sleep)

