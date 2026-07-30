---
title: Hyperlambda loops
description: The [for-each] and [while] slots, allowing you to iterate node-sets and repeat execution while some condition holds.
---

## Hyperlambda loops

Loops in programming languages implies doing something x number of times, where x is any number. Hyperlambda
provides two basic slots for looping; **[for-each]** and **[while]**. Notice, there is no _"for"_ loop
in Hyperlambda, since this can always be created using the **[while]** loop.

### How to use [for-each]

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

### How to use [while]

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
