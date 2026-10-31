---
title: "How to use [yield]"
description: "How to use [yield] - This slot returns its child nodes to the caller, after unwrapping any expressions they contain."
generated: true
guide: true
---

The reference page of [`yield`](/reference/slots/core/yield/) has its arguments, constraints and declaration.

This slot returns its child nodes to the caller, after unwrapping any expressions they contain. It is typically used inside **[map]**, where it returns what each iteration produces. Below is an example, incrementing every number.

```
.src
   .:int:1
   .:int:2
   .:int:3
map:x:@.src/*
   math.increment:x:@.dp/#
   unwrap:x:+/*
   yield
      .:x:@math.increment
```
