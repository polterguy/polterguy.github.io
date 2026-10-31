---
title: "How to use [null]"
description: "How to use [null] - If not, it will return false."
generated: true
guide: true
---

The reference page of [`null`](/reference/slots/core/null/) has its arguments, constraints and declaration.

**[null]** will evaluate to true if its specified expression yields null, or the expression returns no nodes.
If not, it will return false.

```
.src1
   foo:foo
.src2
   foo
null:x:@.src1/*
null:x:@.src2/*
```
