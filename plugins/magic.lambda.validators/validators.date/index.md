---
title: "How to use [validators.date]"
description: "How to use [validators.date] - This slot works similarly to the [validator.integer] validator, except instead of providing a min/max integer value, you're expected to provide a min/max date value."
generated: true
guide: true
---

The reference page of [`validators.date`](/reference/slots/validators/validators.date/) has its arguments, constraints and declaration.

This slot works similarly to the **[validator.integer]** validator, except instead of providing a min/max
integer value, you're expected to provide a min/max _date_ value. Below is an example of how you could use
it.

```
validators.date:x:@.arguments/*/date
   min:date:"2005-01-21T23:59:47"
   max:date:"2023-01-21T23:59:47"
```
