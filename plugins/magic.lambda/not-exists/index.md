---
title: "How to use [not-exists]"
description: "How to use [not-exists] - [not-exists] will evaluate to true if its specified expression yields zero results."
guide: true
slots: ["not-exists"]
---

The reference page of [`not-exists`](/reference/slots/core/not-exists/) has its arguments, constraints and declaration.

**[not-exists]** will evaluate to true if its specified expression yields zero results. If not, it will
return false. It's the logical opposite of **[exists]**.

```
.src1
   foo
.src2
not-exists:x:@.src1/*
not-exists:x:@.src2/*
```
