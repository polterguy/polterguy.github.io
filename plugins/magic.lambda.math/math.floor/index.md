---
title: "How to use [math.floor]"
description: "How to use [math.floor] - This slot rounds its input down to the nearest whole number."
generated: true
guide: true
---

The reference page of [`math.floor`](/reference/slots/math/math.floor/) has its arguments, constraints and declaration.

This slot rounds its input down to the nearest whole number. The slot takes a numeric value, which can be a
constant or an expression, and replaces its value with the rounded result.

Below is an example, rounding 2.6 down to 2.

```
.number:double:2.6
math.floor:x:@.number
```
