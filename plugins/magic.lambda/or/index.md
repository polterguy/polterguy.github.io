---
title: "How to use [or]"
description: "How to use [or] - as the following illustrates."
generated: true
guide: true
---

The reference page of [`or`](/reference/slots/core/or/) has its arguments, constraints and declaration.

**[or]** is similar to **[and]**, except it will evaluate to true if _any_ of its arguments evaluates to true, such
as the following illustrates. **[or]** will also evaluate its arguments, allowing you to use it as a part of richer comparison
trees, the same way **[and]** allows you to. Below is a simple example.

```
// Evaluates to false.
or
   .:bool:false
   .:bool:false

// Evaluates to true.
or
   .:bool:false
   .:bool:true
```

**[or]** will also short circuit itself if it reaches a condition that evaluates to true, implying
none of its conditions afterwards will be considered, since the **[or]** as a whole evaluates to true
if _any_ of its arguments evaluates to true.
