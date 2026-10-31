---
title: "How to use [map]"
description: "How to use [map] - evaluates its lambda object once for each node, passing in the currently iterated node as a [.dp] argument."
generated: true
guide: true
---

The reference page of [`map`](/reference/slots/core/map/) has its arguments, constraints and declaration.

**[map]** iterates through each node being the result of its expression, the same way **[for-each]** does, and
evaluates its lambda object once for each node, passing in the currently iterated node as a **[.dp]** argument.
The value or nodes returned by the lambda object for each iteration, becomes the result of the slot. Each returned
value becomes a `.` node, and any returned child nodes are added as they are. After evaluation, the children of
**[map]** are replaced with the mapped result.

* __[map]__ - Expression selecting the nodes to map
* Children - Lambda object evaluated once per selected node, and expected to return a value or nodes, for instance using **[return]** or **[yield]**

```
.src
   .:int:1
   .:int:2
   .:int:3
map:x:@.src/*
   math.increment:x:@.dp/#
   unwrap:x:+/*
   yield
      .:x:@math.increment
```

After execution, **[map]** has 3 children, with the values 2, 3 and 4. If an iteration returns neither a value nor
any nodes, the slot throws an exception.
