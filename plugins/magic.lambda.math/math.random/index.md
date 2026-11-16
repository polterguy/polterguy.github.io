---
title: "How to use [math.random]"
description: "How to use [math.random] - This slot returns a random number."
generated: true
guide: true
---

The reference page of [`math.random`](/reference/slots/math/math.random/) has its arguments, constraints and declaration.

This slot returns a random number. Its behavior depends on its **[min]** and **[max]** children.

* No children - Returns a random `double` between 0.0 and 1.0.
* **[max]** only - Returns a random integer between 0 and **[max]**, where the upper bound is exclusive.
* **[min]** and **[max]** - Returns a random integer between **[min]**, inclusive, and **[max]**, exclusive.

Both values are converted to `int`, and either may be an expression, such as `max:x:@.count`. Any other
child, and **[min]** without **[max]**, throws an exception.

Below are the three ways to invoke the slot. The first returns a random number between 0 and 1, the second a random integer between 0 and 10, and the third a random integer between 5 and 10.

```
math.random

math.random
   max:10

math.random
   min:5
   max:10
```
