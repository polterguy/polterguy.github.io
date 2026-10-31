---
title: "How to use [include]"
description: "How to use [include] - This slot is logically the combination of a [for-each], [add] and [eval/invoke]."
guide: true
slots: ["include"]
---

The reference page of [`include`](/reference/slots/core/include/) has its arguments, constraints and declaration.

This slot is logically the combination of a **[for-each]**, **[add]** and **[eval/invoke]**. The slot takes a lambda
object, that will be executed with a **[.dp]** node, for each node resulting from evaluating its expression passed
in by reference. The returned nodes will then be appended into the currently iterated node, allowing you to _"include"_
sub trees into a destination tree using a declarative syntax. It is useful for adding nodes dynamically to an existing
graph object, declaratively, according to the state of its destination nodes.

```
.data
   foo1:bar1
   foo2:bar2
   foo3:bar3
include:x:@.data/*
   strings.concat
      get-value:x:@.dp/#
      .:" howdy"
   unwrap:x:+/*
   return
      howdy:x:@strings.concat
```
