---
title: "How to use [math.random]"
description: "How to use [math.random] - This slot returns a random number."
generated: true
guide: true
---

The reference page of [`math.random`](/reference/slots/math/math.random/) has its arguments, constraints and declaration.

This slot returns a random number. Its behavior depends on how many child nodes you give it.

* No children - Returns a random `double` between 0.0 and 1.0.
* One child - Returns a random integer between 0 and the child's value, where the upper bound is exclusive.
* Two children - Returns a random integer between the first child's value, inclusive, and the second child's value, exclusive. The children are documented as **[min]** and **[max]**, but the slot uses the first and second child regardless of their names.

Child values are converted to `int`.

Below are the three ways to invoke the slot. The first returns a random number between 0 and 1, the second a random integer between 0 and 10, and the third a random integer between 5 and 10.

```
math.random

math.random
   max:10

math.random
   min:5
   max:10
```
