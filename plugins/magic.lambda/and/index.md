---
title: "How to use [and]"
description: "How to use [and] - the following. // Evaluates to false."
generated: true
guide: true
---

The reference page of [`and`](/reference/slots/core/and/) has its arguments, constraints and declaration.

**[and]** requires two or more arguments, and will only evaluate to true, if all of its arguments evaluates to true. Consider
the following.

```
// Evaluates to false.
and
   .:bool:true
   .:bool:false

// Evaluates to true.
and
   .:bool:true
   .:bool:true
```

Notice, **[and]** will short circuit itself if it reaches a condition that does _not_ evaluate to true, implying
none of its conditions afterwards will be considered, since the **[and]** as a whole evaluates to false.
**[and]** will also evaluate its arguments before checking if they evaluate to true, allowing you
to use it as a part of richer comparison trees, such as the following illustrates.

```
.s1:bool:true
.s2:bool:true
.res

if
   and
      get-value:x:@.s1
      get-value:x:@.s2
   .lambda

      set-value:x:@.res
         .:OK
```
