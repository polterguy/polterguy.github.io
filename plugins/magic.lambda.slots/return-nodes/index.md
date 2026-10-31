---
title: "How to use [return-nodes]"
description: "How to use [return-nodes] - Returns a bunch of nodes (lambda) from your slot."
generated: true
guide: true
---

The reference page of [`return-nodes`](/reference/slots/core/return-nodes/) has its arguments, constraints and declaration.

Returns a bunch of nodes (lambda) from your slot. Can only be invoked from the inside of
a dynamically created slot, and other slots explicitly creating a return context. An example can be
found below.

```
slots.create:foo
   return-nodes
      integer-value:int:57
      string-value:Foo bar

signal:foo
```
