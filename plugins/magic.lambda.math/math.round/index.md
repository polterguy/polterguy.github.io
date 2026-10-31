---
title: "How to use [math.round]"
description: "How to use [math.round] - This slot rounds its input to the nearest whole number, using .NET's Math.Round, which rounds halfway values to the nearest even number."
generated: true
guide: true
---

The reference page of [`math.round`](/reference/slots/math/math.round/) has its arguments, constraints and declaration.

This slot rounds its input to the nearest whole number, using .NET's `Math.Round`, which rounds halfway values to the nearest even number. The slot takes a numeric value, which can be a
constant or an expression, and replaces its value with the rounded result.

Below is an example, rounding 2.6 to 3.

```
.number:double:2.6
math.round:x:@.number
```
