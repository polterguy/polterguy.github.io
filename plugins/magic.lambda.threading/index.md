---
title: magic.lambda.threading
moved_anchors: {"how-to-use-executionkill": "/reference/slots/execution/execution.kill/#guide", "how-to-use-executionthrottle": "/reference/slots/execution/execution.throttle/#guide", "how-to-use-executiontimeout": "/reference/slots/execution/execution.timeout/#guide", "how-to-use-fork": "/reference/slots/core/fork/#guide", "how-to-use-join": "/reference/slots/core/join/#guide", "how-to-use-semaphore": "/reference/slots/core/semaphore/#guide", "how-to-use-sleep": "/reference/slots/core/sleep/#guide"}
---

This project contains all thread related slots for Hyperlambda. Threading in software development implies
doing multiple things concurrently, scheduling CPU time for each of your threads, creating the illusion
of having your computer doing multiple times concurrently. This concept is often referred to as
_"multi tasking"_ and is crucial for any modern operating system, and/or programming language.
Hyperlambda contains several multi tasking related slots.

* __[\[fork\]](/reference/slots/core/fork/)__ - Executes lambda in a separate thread pool work item
* __[\[join\]](/reference/slots/core/join/)__ - Waits for descendant forks to complete
* __[\[semaphore\]](/reference/slots/core/semaphore/)__ - Synchronizes concurrent access to shared resources
* __[\[sleep\]](/reference/slots/core/sleep/)__ - Suspends the current execution for a number of milliseconds
* __[\[execution.kill\]](/reference/slots/execution/execution.kill/)__ - Cancels another running execution by its execution id
* __[\[execution.timeout\]](/reference/slots/execution/execution.timeout/)__ - Configures a timeout for the current execution context
* __[\[execution.throttle.create\]](/reference/slots/execution/execution.throttle.create/)__ - Creates, replaces or deletes a named throttle
* __[\[execution.throttle\]](/reference/slots/execution/execution.throttle/)__ - Enforces a named throttle, rate limiting invocations
