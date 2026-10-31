---
title: "How to use [exists]"
description: "How to use [exists] - return false. .src1    foo .src2 exists:x:@.src1/ exists:x:@.src2/"
generated: true
guide: true
---

The reference page of [`exists`](/reference/slots/core/exists/) has its arguments, constraints and declaration.

**[exists]** will evaluate to true if its specified expression yields one or more results. If not, it will
return false.

```
.src1
   foo
.src2
exists:x:@.src1/*
exists:x:@.src2/*
```
