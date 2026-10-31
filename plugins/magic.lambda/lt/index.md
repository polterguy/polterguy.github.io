---
title: "How to use [lt]"
description: "How to use [lt] - At the heart of Hyperlambda is the [eval] slot."
generated: true
guide: true
---

The reference page of [`lt`](/reference/slots/core/lt/) has its arguments, constraints and declaration.

At the heart of Hyperlambda is the **[eval]** slot. This slot is responsible for executing your lambda object
and follows a couple of simple rules. All nodes starting with a _"."_ will be ignored, and **[eval]** will not
try to raise these nodes as signals. This has two benefits.

1. You can create _"hidden"_ slots, that are only accessible from C#.
2. You can use nodes starting with _"."_ as data nodes, separating function invocations from data.

**[eval]** makes Hyperlambda _"super functional"_ in nature. Below is an example of a Hyperlambda
piece of code, that illustrates this, by adding a _"callback"_ lambda object to its **[while]** invocation
as a **[.lambda]** node, that will be invoked once for every iteration of your while loop.

```
.no:int:0

while
   lt
      get-value:x:@.no
      .:int:20
   .lambda

      // Your lambda goes here.
      log.info:Howdy from while
      math.increment:x:@.no
```
