---
title: "How to use [get-count]"
description: "How to use [get-count] - This slot returns the number of nodes its expression is pointing to."
guide: true
slots: ["get-count"]
---

The reference page of [`get-count`](/reference/slots/core/get-count/) has its arguments, constraints and declaration.

This slot returns the number of nodes its expression is pointing to.

```
.data
   foo1
   foo2
get-count:x:@.data/*
```
