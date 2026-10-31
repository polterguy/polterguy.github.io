---
title: "How to use [insert-before]"
description: "How to use [insert-before] - This slot works the exact same way as the [add] node, except it will insert the nodes before the node(s) referenced in its main/destination argument."
generated: true
guide: true
---

The reference page of [`insert-before`](/reference/slots/core/insert-before/) has its arguments, constraints and declaration.

This slot works the exact same way as the **[add]** node, except it will insert the nodes _before_ the
node(s) referenced in its main/destination argument.

```
.foo
   foo1
   foo2
insert-before:x:@.foo/*/foo1
   .
      inserted
```
