---
title: "How to use [math.modulo]"
description: "How to use [math.modulo] - This slot calculates the modulo of two or more values with each other, and can be given as many arguments as you wish, such as the following illustrates."
generated: true
guide: true
---

This is the guide to [`math.modulo`](/reference/slots/math/math.modulo/), whose reference page has its arguments, constraints and declaration.

This slot calculates the modulo of two or more values with each other, and can be given as many arguments as you wish,
such as the following illustrates.

```
.arg:int:5
math.modulo
   get-value:x:@.arg
   .:int:2
```

It accepts both slot invocations, retrieving some value by invoking a slot, in addition to static values such as
illustrated above where we provide the number 2 as one of its values.
