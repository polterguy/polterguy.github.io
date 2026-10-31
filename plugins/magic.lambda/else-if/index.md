---
title: "How to use [else-if]"
description: "How to use [else-if] - [else-if] is the younger sibling of [if], and must be preceded by its older sibling, or other [else-if] nodes, and will only be evaluated if all of its previous conditional slots evaluates to fa..."
guide: true
slots: ["else-if"]
---

The reference page of [`else-if`](/reference/slots/core/else-if/) has its arguments, constraints and declaration.

**[else-if]** is the younger sibling of **[if]**, and must be preceded by its older sibling, or other **[else-if]** nodes,
and will only be evaluated if all of its previous conditional slots evaluates to false - At which point **[else-if]** is
allowed to test its condition - And only if its condition evaluates to true, it evaluate its lambda object. Semantically **[else-if]**
is similar to **[if]**, in that it requires two arguments with the same structure as **[if]**.

```
.dest
if
   .:bool:false
   .lambda
      set-value:x:@.dest
         .:yup!
else-if
   .:bool:true
   .lambda
      set-value:x:@.dest
         .:yup2.0!
```

**[else-if]** can also be given an expression directly the same way **[if]** can. See the example for **[if]**
to understand how this works.
