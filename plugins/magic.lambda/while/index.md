---
title: "How to use [while]"
description: "How to use [while] - Semantically similar to [if], but instead of evaluating its lambda object once, will iterate it for as long as the condition evaluates to true."
guide: true
slots: ["while"]
---

The reference page of [`while`](/reference/slots/core/while/) has its arguments, constraints and declaration.

Semantically similar to **[if]**, but instead of evaluating its lambda object once, will iterate it for
as long as the condition evaluates to true. Requires _exactly_ two arguments, the same way **[if]** does.

```
.no:int:0
.res

while
   lt
      get-value:x:@.no
      .:int:5
   .lambda

      add:x:@.res
         .
            foo
      math.increment:x:@.no
```

The above Hyperlambda snippet basically implies the following if we are to translate it into plain English;
_"Set .no to 0, then loop while .no is less than 5, where the loop adds a node into .res, before it increments .no by 1"_.
