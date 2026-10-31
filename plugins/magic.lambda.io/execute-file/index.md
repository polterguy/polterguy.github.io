---
title: "How to use [execute-file]"
description: "How to use [execute-file] - The [execute-file] slot is an alias for [io.file.execute], but it will [unwrap] all children nodes, automatically transform any expressions to their static value equivalents, allowing you t..."
generated: true
guide: true
---

This is the guide to [`execute-file`](/reference/slots/core/execute-file/), whose reference page has its arguments, constraints and declaration.

The **[execute-file]** slot is an alias for **[io.file.execute]**, but it will **[unwrap]** all children nodes,
automatically transform any expressions to their static value equivalents, allowing you to combine **[unwrap]**
and **[io.file.execute]** into one invocation. This makes usage slightly less verbose for cases such as the following.

```
.args
   foo1:bar1
   foo2:bar2
execute-file:/whatever-file.hl
   arg1:x:@.args/*/foo1
   arg2:x:@.args/*/foo2
```

In the above example both arguments to our _"/whatever-file.hl"_ file will be evaluated before the file is executed,
resulting in **[arg1]** and **[args2]** having the values of _"bar1"_ and _"bar2"_ respectively.

If you pass in a node named **[node_reference]** using the above syntax, this node will be especially handled, and
passed in by reference instead of evaluated as a single expression value. Consider the following alternative to
the above.

```
.args
   foo1:bar1
   foo2:bar2
execute-file:/whatever-file.hl
   node_reference:x:@.args
```

Inside your above _"/whatever-file.hl"_ file you will now have access to the entire **[.args]** node by reference.
