---
title: "How to use [math.multiply]"
description: "How to use [math.multiply] - This slot multiplies two or more values with each other, and can be given as many arguments as you wish, such as the following illustrates."
generated: true
guide: true
---

The reference page of [`math.multiply`](/reference/slots/math/math.multiply/) has its arguments, constraints and declaration.

This slot multiplies two or more values with each other, and can be given as many arguments as you wish,
such as the following illustrates.

```
.arg:int:5
math.multiply
   get-value:x:@.arg
   .:int:3
```

It accepts both slot invocations, retrieving some value by invoking a slot, in addition to static values such as
illustrated above where we provide the number 3 as one of its values.
