---
title: "How to use [lte]"
description: "How to use [lte] - to its second argument."
generated: true
guide: true
---

The reference page of [`lte`](/reference/slots/core/lte/) has its arguments, constraints and declaration.

**[lte]** will do a comparison between its two arguments, and only return true if its first argument is _"less than or equal"_
to its second argument. Consider the following.

```
.src1:int:4
lte
   get-value:x:@.src1
   .:int:4
```
