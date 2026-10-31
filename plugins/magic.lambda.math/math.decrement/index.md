---
title: "How to use [math.decrement]"
description: "How to use [math.decrement] - This slot decrements the value of some expression in place, by mutating the value of the node its expression is leading to."
generated: true
guide: true
---

This is the guide to [`math.decrement`](/reference/slots/math/math.decrement/), whose reference page has its arguments, constraints and declaration.

This slot decrements the value of some expression in place, by mutating the value of the node its expression is
leading to.

```
.arg:int:5
math.decrement:x:@.arg
```

It can optionally be given a **[step]** argument, such as illustrated below.

```
.arg:int:5
math.decrement:x:@.arg
   .:int:2
```
