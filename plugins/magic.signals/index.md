---
title: magic.signals
moved_anchors: {"active-events-or-super-signals-internals": "/plugins/magic.signals/active-events-or-super-signals-internals/", "passing-arguments-to-your-slots": "/plugins/magic.signals/passing-arguments-to-your-slots/"}
---

magic.signals is a _"Super Signals"_ implementation for .Net 8 built on top of magic.node,
allowing you to invoke functions from one assembly in another assembly without having any direct references between
your projects.


## Execution scoped context

magic.signals also provides the low level runtime pieces required for execution scoped cancellation.
An execution can carry ambient state through the signaler stack, allowing C# slots to retrieve the
current execution context from `ISignaler` without changing every method signature in the system.

The current execution context can be retrieved in C# using the helper extensions in this project.

```csharp
var execution = signaler.GetExecutionContext();
var token = signaler.GetCancellationToken();
signaler.ThrowIfCancelled();
```

An execution context contains the execution id, cancellation token, reference counting for forked
work, and optional deadline tracking for execution timeouts. This allows one request to cancel a
different in-flight request by id, while still allowing child threads to share the same execution
state safely.

Hyperlambda does not receive the raw execution object. Instead, higher layers may expose selected
values such as the execution id through ordinary context values such as `dynamic.execution-id`,
allowing code to use existing helpers such as **[get-context]** without exposing internal runtime
objects.


## Magic Signals a DSL

A lot of the idea behind Magic Signals is that combined with magic.node,
and especially its ability to parse Hyperlambda, it becomes a very good foundation for a DSL, or a Domain Specific
programming Language implementation, allowing you to easily create your own programming languages, and keywords,
based upon Hyperlambda syntax trees. Hyperlambda in this context being the textual representation of your `Node`
hierarchy.


## Topics

* [Active Events or Super Signals internals](/plugins/magic.signals/active-events-or-super-signals-internals/) - Zero cross project references is made possible by always having a YALOA, allowing us to invoke methods in classes through a "magic string", which references a type in a dictionary, where the string is
* [Passing arguments to your slots](/plugins/magic.signals/passing-arguments-to-your-slots/) - The Node class provides a graph object for you, allowing you to automagically pass in any arguments you wish.
