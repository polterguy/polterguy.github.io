---
title: "How to use [math.subtract]"
description: "How to use [math.subtract] - This slot subtracts two or more values with each other, and can be given as many arguments as you wish, such as the following illustrates."
generated: true
guide: true
---

The reference page of [`math.subtract`](/reference/slots/math/math.subtract/) has its arguments, constraints and declaration.

This slot subtracts two or more values with each other, and can be given as many arguments as you wish,
such as the following illustrates.

```
.arg:int:5
math.subtract
   get-value:x:@.arg
   .:int:2
```

It accepts both slot invocations, retrieving some value by invoking a slot, in addition to static values such as
illustrated above where we provide the number 2 as one of its values.
