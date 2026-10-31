---
title: "How to use [unwrap]"
description: "How to use [unwrap] - This slot is useful if you want to evaluate some expression before the node where it's referenced is reached."
guide: true
slots: ["unwrap"]
---

The reference page of [`unwrap`](/reference/slots/core/unwrap/) has its arguments, constraints and declaration.

This slot is useful if you want to evaluate some expression before the node where it's referenced is reached.
Imagine the following.

```
.src:Hello World
unwrap:x:+
.dest:x:@.src
```

In the above example, before the **[.dest]** node is reached by the Hyperlambda instruction pointer, the value
of the **[.dest]** node will have been _"unwrapped"_ (evaluated), and its value will be _"Hello World"_.
This slot becomes very handy when you invoke lambda objects with expressions, since
it allows you to _"forward evaluate"_ said expressions inside your lambda object, _before_ the lambda object
is actually executed.

The **[unwrap]** slot can also optionally be supplied with a **[apply-lists]** argument as boolean true. By default the **[unwrap]** slot will throw an exception if you unwrap a node leading to multiple nodes. If you apply lists, it will instead add all the source nodes as destination nodes into the unwrapped node. Consider the following.

```
.src
   foo1:bar1
   foo2:bar2
unwrap:x:+
   apply-lists:bool:true
.dest:x:@.src/*
```

If you remove the above **[apply-lists]** argument or set its value to false, the above code will throw an exception. If you keep the above **[apply-lists]** argument as is it will result in the following.

```
.src
   foo1:bar1
   foo2:bar2
unwrap:x:+
   apply-lists:bool:true
.dest
   foo1:bar1
   foo2:bar2
```
