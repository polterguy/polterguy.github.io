---
title: "How to use [hyperlambda.verify-slots]"
description: "How to use [hyperlambda.verify-slots] - This slot statically verifies a piece of Hyperlambda without executing it, and is useful for checking generated Hyperlambda before you run it."
generated: true
guide: true
---

This is the guide to [`hyperlambda.verify-slots`](/reference/slots/hyperlambda/hyperlambda.verify-slots/), whose reference page has its arguments, constraints and declaration.

This slot statically verifies a piece of Hyperlambda without executing it, and is useful for checking generated
Hyperlambda before you run it. A slot name that doesn't exist is silently treated as an inert data node by the
evaluator, and this slot surfaces such names. The Hyperlambda to verify is given as the value of the slot, either as
a string or as an expression leading to a string. If no value is given, the slot verifies its own children instead.
Below is an example.

```
.hl:@"try
   missing.try
.catch
   eval"

hyperlambda.verify-slots:x:@.hl
```

The slot returns `false` if the Hyperlambda is invalid, and `true` if it is valid, in which case it has no children.
When it returns `false`, every missing slot name is returned as an unnamed child node, and the example above
returns `missing.try` this way.

The slot verifies the root level of the Hyperlambda, in addition to the bodies of slots such as **[try]**,
**[.catch]**, **[.finally]**, **[switch]**, **[case]**, **[default]** and **[eval]**, to any depth. Nodes whose
names start with a `.`, such as variables, comments and **[.arguments]**, are not treated as slot invocations, and
arguments such as the **[table]** and **[where]** nodes of **[data.read]** are not checked as slots.

In addition to missing slots, the slot also reports the following as **[invalid-invocation]** child nodes.

* A slot that requires a primary value, but is invoked without one.
* A slot that requires either a primary value or child nodes, but is invoked with neither.
* A child argument that the slot's signature doesn't declare.
