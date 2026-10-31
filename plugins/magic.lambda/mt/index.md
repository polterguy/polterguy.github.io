---
title: "How to use [mt]"
description: "How to use [mt] - its second argument. Consider the following."
generated: true
guide: true
---

The reference page of [`mt`](/reference/slots/core/mt/) has its arguments, constraints and declaration.

**[mt]** will do a comparison between its two arguments, and only return true if its first argument is _"more than"_
its second argument. Consider the following.

```
.src1:int:7
mt
   get-value:x:@.src1
   .:int:5
```
