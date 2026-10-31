---
title: Branching and conditional execution
description: The [if], [else-if], [else] and [switch] slots, giving Hyperlambda its branching and conditional execution constructs.
moved_anchors: {"how-to-use-else": "/plugins/magic.lambda/else/", "how-to-use-else-if": "/plugins/magic.lambda/else-if/", "how-to-use-if": "/plugins/magic.lambda/if/", "how-to-use-switch": "/plugins/magic.lambda/switch/"}
---

## Hyperlambda branching and conditional execution

Branching implies to change the execution path of your code, and examples includes function invocations, and
other similar mechanisms that changes the position of your computer's _"execution pointer"_. Conditional
branching implies to changing the position of the execution pointer, according to some condition. Typically
this implies constructs such as `if`, `else`, `goto` etc in traditional programming languages.

* [`if`](/plugins/magic.lambda/if/) - This is the Hyperlambda equivalent of if from other programming languages.
* [`else-if`](/plugins/magic.lambda/else-if/) - [else-if] is the younger sibling of [if], and must be preceded by its older sibling, or other [else-if] nodes, and will only be evaluated if all of its previous conditional slots evaluates to false -
* [`else`](/plugins/magic.lambda/else/) - [else] is the last of the "conditional siblings" that will only be evaluated as a last resort, only if none of its elder "siblings" evaluates to true.
* [`switch`](/plugins/magic.lambda/switch/) - [switch] works similarly to a switch/case block in a traditional programming language, and will find the first [case] node with a value matching the evaluated value of the [switch] node, and execute t
