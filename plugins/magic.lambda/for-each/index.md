---
title: "How to use [for-each]"
description: "How to use [for-each] - [for-each] iterates through each node being the result of an expression, and evaluates its lambda object, passing in the currently iterated node as a [.dp] argument, containing the node current..."
guide: true
slots: ["for-each"]
---

The reference page of [`for-each`](/reference/slots/core/for-each/) has its arguments, constraints and declaration.

**[for-each]** iterates through each node being the result of an expression, and evaluates its lambda object,
passing in the currently iterated node as a **[.dp]** argument, containing the node currently
iterated by _reference_.

```
.data
   foo1
   foo2

for-each:x:-/*

   set-value:x:@.dp/#
      .:hello
```

See the documentation for the **[reference]** slot to understand how reference nodes works.
