---
title: "How to use [sort]"
description: "How to use [sort] - Sort takes an expression leading to a list of nodes, in addition to a lambda object."
generated: true
guide: true
---

The reference page of [`sort`](/reference/slots/core/sort/) has its arguments, constraints and declaration.

Sort takes an expression leading to a list of nodes, in addition to a lambda object. Your lambda
object will be invoked several times, with an **[.lhs]**, an **[.rhs]** and a **[.result]** argument.
It is your code's responsibility to set the value of the **[.result]** node according to which of the
**[.lhs]** and **[.rhs]** node should come first in the sorted result.

```
.data
   .
      name:Thomas
   .
      name:John
   .
      name:Jane
   .
      name:Peter
sort:x:@.data/*
   if
      lt:x:@.lhs/#/*/name
         get-value:x:@.rhs/#/*/name
      .lambda
         set-value:x:@.result
            .:int:-1
   else-if
      mt:x:@.lhs/#/*/name
         get-value:x:@.rhs/#/*/name
      .lambda
         set-value:x:@.result
            .:int:1
   else
      set-value:x:@.result
         .:int:0
```

Notice, **[sort]** does not modify the original list, but returns a new list of nodes after having executed.
