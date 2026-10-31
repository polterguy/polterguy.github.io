---
title: "How to use [insert-after]"
description: "How to use [insert-after] - This slot works the exact same way as the [add] and [insert-before] slots, except it will insert the nodes after the node(s) referenced in its main/destination argument."
generated: true
guide: true
---

The reference page of [`insert-after`](/reference/slots/core/insert-after/) has its arguments, constraints and declaration.

This slot works the exact same way as the **[add]** and **[insert-before]** slots, except it will insert the
nodes _after_ the node(s) referenced in its main/destination argument.

```
.foo
   foo1
   foo2
insert-after:x:@.foo/*/foo1
   .
      inserted
```
