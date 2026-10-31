---
title: Hyperlambda loops
description: The [for-each] and [while] slots, allowing you to iterate node-sets and repeat execution while some condition holds.
moved_anchors: {"how-to-use-for-each": "/plugins/magic.lambda/for-each/", "how-to-use-map": "/plugins/magic.lambda/map/", "how-to-use-while": "/plugins/magic.lambda/while/"}
---

## Hyperlambda loops

Loops in programming languages implies doing something x number of times, where x is any number. Hyperlambda
provides two basic slots for looping; **[for-each]** and **[while]**. Notice, there is no _"for"_ loop
in Hyperlambda, since this can always be created using the **[while]** loop. The **[map]** slot also iterates
a node-set, but collects the result of each iteration into a new result set.

* [`for-each`](/plugins/magic.lambda/for-each/) - [for-each] iterates through each node being the result of an expression, and evaluates its lambda object, passing in the currently iterated node as a [.dp] argument, containing the node currently iter
* [`map`](/plugins/magic.lambda/map/) - [map] iterates through each node being the result of its expression, the same way [for-each] does, and evaluates its lambda object once for each node, passing in the currently iterated node as a [.dp]
* [`while`](/plugins/magic.lambda/while/) - Semantically similar to [if], but instead of evaluating its lambda object once, will iterate it for as long as the condition evaluates to true.
