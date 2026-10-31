---
title: "How to use [default]"
description: "How to use [default] - [switch] can only contain two types of children nodes; [case] and [default]."
generated: true
guide: true
---

The reference page of [`default`](/reference/slots/core/default/) has its arguments, constraints and declaration.

**[switch]** can only contain two types of children nodes; **[case]** and **[default]**. The **[default]** node
will be evaluated if _none_ of the **[case]** node's values are matching the evaluated value of your **[switch]**.
Try evaluating the following in your _"Eval"_ component to understand this.

```
.val:fooXX
.result
switch:x:@.val

   case:bar
      set-value:x:@.result
         .:Oops

   case:foo
      set-value:x:@.result
         .:Oops2.0

   default
      set-value:x:@.result
         .:Success!
```
