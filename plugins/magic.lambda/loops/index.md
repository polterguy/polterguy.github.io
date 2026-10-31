---
title: Hyperlambda loops
description: The [for-each] and [while] slots, allowing you to iterate node-sets and repeat execution while some condition holds.
---

## Hyperlambda loops

Loops in programming languages implies doing something x number of times, where x is any number. Hyperlambda
provides two basic slots for looping; **[for-each]** and **[while]**. Notice, there is no _"for"_ loop
in Hyperlambda, since this can always be created using the **[while]** loop. The **[map]** slot also iterates
a node-set, but collects the result of each iteration into a new result set.

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

### How to use [map]

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
