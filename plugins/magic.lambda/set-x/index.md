---
title: "How to use [set-x]"
description: "How to use [set-x] - Similar to [set-value], but does not evaluate expressions found in its source."
generated: true
guide: true
---

The reference page of [`set-x`](/reference/slots/core/set-x/) has its arguments, constraints and declaration.

Similar to **[set-value]**, but does not evaluate expressions found in its source. Where **[set-value]** replaces a source
expression with the value it points to, **[set-x]** assigns the expression itself as the new value of its destination
nodes. It takes the same arguments as **[set-value]**; a main expression selecting the destination nodes, and at most one
source child. Having more than one child throws an exception.

```
.foo1:.bar1
set-x:x:../*/.foo1
   .:x:../*/.foo1
```

After execution, the value of **[.foo1]** is the expression `../*/.foo1`, and not the value `.bar1`.
