---
title: "How to use [mte]"
description: "How to use [mte] - to its second argument."
generated: true
guide: true
---

The reference page of [`mte`](/reference/slots/core/mte/) has its arguments, constraints and declaration.

**[mte]** will do a comparison between its two arguments, and only return true if its first argument is _"more than or equal"_
to its second argument. Consider the following.

```
.src1:int:7
mte
   get-value:x:@.src1
   .:int:5
```
