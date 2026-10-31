---
title: "How to use [math.ceil]"
description: "How to use [math.ceil] - This slot rounds its input up to the nearest whole number."
generated: true
guide: true
---

The reference page of [`math.ceil`](/reference/slots/math/math.ceil/) has its arguments, constraints and declaration.

This slot rounds its input up to the nearest whole number. The slot takes a numeric value, which can be a
constant or an expression, and replaces its value with the rounded result.

Below is an example, rounding 2.6 up to 3.

```
.number:double:2.6
math.ceil:x:@.number
```
