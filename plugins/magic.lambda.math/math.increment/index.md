---
title: "How to use [math.increment]"
description: "How to use [math.increment] - This slot increments the value of some expression in place, by mutating the value of the node its expression is leading to."
generated: true
guide: true
---

The reference page of [`math.increment`](/reference/slots/math/math.increment/) has its arguments, constraints and declaration.

This slot increments the value of some expression in place, by mutating the value of the node its expression is
leading to.

```
.arg:int:5
math.increment:x:@.arg
```

It can optionally be given a **[step]** argument, such as illustrated below.

```
.arg:int:5
math.increment:x:@.arg
   .:int:2
```
