---
title: "How to use [mt]"
description: "How to use [mt] - [mt] will do a comparison between its two arguments, and only return true if its first argument is \"more than\" its second argument."
guide: true
slots: ["mt"]
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
