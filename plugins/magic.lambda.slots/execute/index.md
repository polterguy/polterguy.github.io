---
title: "How to use [execute]"
description: "How to use [execute] - The [execute] slot is an alias for [signal], but it will [unwrap] all children nodes, automatically transform any expressions to their static value equivalents, allowing you to combine [unwrap]..."
generated: true
guide: true
---

The reference page of [`execute`](/reference/slots/core/execute/) has its arguments, constraints and declaration.

The **[execute]** slot is an alias for **[signal]**, but it will **[unwrap]** all children nodes, automatically
transform any expressions to their static value equivalents, allowing you to combine **[unwrap]** and **[signal]**
into one invocation. This makes usage slightly less verbose for cases such as the following.

```
.args
   foo1:bar1
   foo2:bar2
execute:whatever-slot
   arg1:x:@.args/*/foo1
   arg2:x:@.args/*/foo2
```

In the above example both arguments to our _"whatever-slot"_ invocation will be evaluated before the slot is invoked,
resulting in **[arg1]** and **[args2]** having the values of _"bar1"_ and _"bar2"_ respectively.

If you pass in a node named **[node_reference]** using the above syntax, this node will be especially handled, and
passed in by reference instead of evaluated as a single expression value. Consider the following alternative to
the above.

```
.args
   foo1:bar1
   foo2:bar2
execute:whatever-slot
   node_reference:x:@.args
```

Inside your above _"whatever-slot"_ you will now have access to the entire **[.args]** node by reference.
It might help to execute the following to understand.

```
.args
   foo1:howdy
   foo2:world
slots.create:foo
   lambda2hyper:x:../*
   return:x:-
execute:foo
   node_reference:x:@.args/*
```
