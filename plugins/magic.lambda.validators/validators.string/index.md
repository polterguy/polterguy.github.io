---
title: "How to use [validators.string]"
description: "How to use [validators.string] - This works the same way as the [validators.integer] validator, except instead of being a min/max value the min/max arguments declares the minimum and maximum length of the string, allo..."
generated: true
guide: true
---

The reference page of [`validators.string`](/reference/slots/validators/validators.string/) has its arguments, constraints and declaration.

This works the same way as the **[validators.integer]** validator, except instead of being a min/max
_value_ the min/max arguments declares the minimum and maximum _length_ of the string, allowing you
to restrict string length of arguments to a min/max value for your Hyperlambda. Below is example
usage that will throw an exception unless the argument is between 5 and 15 characters in length.

```
validators.string:x:@.some-arg
   min:5
   max:15
```
