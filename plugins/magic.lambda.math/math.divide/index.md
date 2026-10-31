---
title: "How to use [math.divide]"
description: "How to use [math.divide] - This slot divides two or more values with each other, and can be given as many arguments as you wish, such as the following illustrates."
generated: true
guide: true
---

The reference page of [`math.divide`](/reference/slots/math/math.divide/) has its arguments, constraints and declaration.

This slot divides two or more values with each other, and can be given as many arguments as you wish,
such as the following illustrates.

```
.arg:int:5
math.divide
   get-value:x:@.arg
   .:int:2
```

It accepts both slot invocations, retrieving some value by invoking a slot, in addition to static values such as
illustrated above where we provide the number 2 as one of its values.
