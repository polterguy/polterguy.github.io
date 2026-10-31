---
title: magic.lambda.threading
moved_anchors: {"how-to-use-executionkill": "/plugins/magic.lambda.threading/execution.kill/", "how-to-use-executionthrottle": "/plugins/magic.lambda.threading/execution.throttle/", "how-to-use-executionthrottlecreate": "/plugins/magic.lambda.threading/execution.throttle.create/", "how-to-use-executiontimeout": "/plugins/magic.lambda.threading/execution.timeout/", "how-to-use-fork": "/plugins/magic.lambda.threading/fork/", "how-to-use-join": "/plugins/magic.lambda.threading/join/", "how-to-use-semaphore": "/plugins/magic.lambda.threading/semaphore/", "how-to-use-sleep": "/plugins/magic.lambda.threading/sleep/"}
---

This project contains all thread related slots for Hyperlambda. Threading in software development implies
doing multiple things concurrently, scheduling CPU time for each of your threads, creating the illusion
of having your computer doing multiple times concurrently. This concept is often referred to as
_"multi tasking"_ and is crucial for any modern operating system, and/or programming language.
Hyperlambda contains several multi tasking related slots.

* __[\[fork\]](/plugins/magic.lambda.threading/fork/)__ - Executes lambda in a separate thread pool work item
* __[\[join\]](/plugins/magic.lambda.threading/join/)__ - Waits for descendant forks to complete
* __[\[semaphore\]](/plugins/magic.lambda.threading/semaphore/)__ - Synchronizes concurrent access to shared resources
* __[\[sleep\]](/plugins/magic.lambda.threading/sleep/)__ - Suspends the current execution for a number of milliseconds
* __[\[execution.kill\]](/plugins/magic.lambda.threading/execution.kill/)__ - Cancels another running execution by its execution id
* __[\[execution.timeout\]](/plugins/magic.lambda.threading/execution.timeout/)__ - Configures a timeout for the current execution context
* __[\[execution.throttle.create\]](/plugins/magic.lambda.threading/execution.throttle.create/)__ - Creates, replaces or deletes a named throttle
* __[\[execution.throttle\]](/plugins/magic.lambda.threading/execution.throttle/)__ - Enforces a named throttle, rate limiting invocations
