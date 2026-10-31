---
title: "How to use [lt]"
description: "How to use [lt] - [lt] will do a comparison between its two arguments, and only return true if its first argument is \"less than\" its second argument."
guide: true
slots: ["lt"]
---

The reference page of [`lt`](/reference/slots/core/lt/) has its arguments, constraints and declaration.

**[lt]** will do a comparison between its two arguments, and only return true if its first argument is _"less than"_
its second argument. Consider the following.

```
.src1:int:4
lt
   get-value:x:@.src1
   .:int:5
```
