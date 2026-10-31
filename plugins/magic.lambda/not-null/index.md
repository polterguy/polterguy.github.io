---
title: "How to use [not-null]"
description: "How to use [not-null] - If not, it will return false."
generated: true
guide: true
---

The reference page of [`not-null`](/reference/slots/core/not-null/) has its arguments, constraints and declaration.

**[not-null]** will evaluate to true if its specified expression returns nodes and at least one of those nodes has a value.
If not, it will return false.

```
.src1
   foo:foo
.src2
   foo
.src3
not-null:x:@.src1/*
not-null:x:@.src2/*
not-null:x:@.src3/*
```
