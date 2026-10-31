---
title: "How to use [else]"
description: "How to use [else] - [else] is the last of the \"conditional siblings\" that will only be evaluated as a last resort, only if none of its elder \"siblings\" evaluates to true."
guide: true
slots: ["else"]
---

The reference page of [`else`](/reference/slots/core/else/) has its arguments, constraints and declaration.

**[else]** is the last of the _"conditional siblings"_ that will only be evaluated as a last resort, only if none of its
elder _"siblings"_ evaluates to true. Notice, contrary to both **[if]** and **[else-if]**, **[else]** contains its lambda object
directly as children nodes, and _not_ within a **[.lambda]** node. This is because **[else]** does not require any
conditional arguments like **[if]** and **[else-if]** does. An example can be found below.

```
.src:int:3
.dest
if
   eq
      get-value:x:@.src
      .:int:1
   .lambda

      set-value:x:@.dest
         .:yup!

else-if
   eq
      get-value:x:@.src
      .:int:2
   .lambda

      set-value:x:@.dest
         .:yup2.0!

else

   set-value:x:@.dest
      .:nope
```
