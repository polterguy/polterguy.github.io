---
title: "How to use [validators.integer]"
description: "How to use [validators.integer] - This value takes a [min] and [max] value, both of which are optional, and declares the minimum, and/or maximum value of the integer input."
generated: true
guide: true
---

The reference page of [`validators.integer`](/reference/slots/validators/validators.integer/) has its arguments, constraints and declaration.

This value takes a **[min]** and **[max]** value, both of which are optional, and declares the minimum, and/or
maximum value of the integer input. Usage could be as follows.

```
validators.integer:x:@.arguments/*/some-integer-argument
   min:50
   max:100
```

If the specified integer value is not within the range of the min and max value, an exception will be thrown.
