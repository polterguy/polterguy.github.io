---
title: "How to use [case]"
description: "How to use [case] - [switch] works similarly to a switch/case block in a traditional programming language, and will find the first [case] node with a value matching the evaluated value of the [switch] node, and execute t"
generated: true
guide: true
---

The reference page of [`case`](/reference/slots/core/case/) has its arguments, constraints and declaration.

**[switch]** works similarly to a switch/case block in a traditional programming language, and will find the
first **[case]** node with a value matching the evaluated value of the **[switch]** node, and execute that
**[case]** node as a lambda object.

```
.val:foo
.result
switch:x:@.val

   case:bar
      set-value:x:@.result
         .:Oops

   case:foo
      set-value:x:@.result
         .:Success!
```
