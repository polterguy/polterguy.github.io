---
title: Modifying your lambda object
description: The slots that read and modify your Hyperlambda graph object; [add], [insert-before], [set-value], [unwrap], [get-value], [exists], [reference] and more.
moved_anchors: {"how-to-use-add": "/plugins/magic.lambda/add/", "how-to-use-exists": "/plugins/magic.lambda/exists/", "how-to-use-filter": "/plugins/magic.lambda/filter/", "how-to-use-get-context": "/plugins/magic.lambda/get-context/", "how-to-use-get-count": "/plugins/magic.lambda/get-count/", "how-to-use-get-first-value": "/plugins/magic.lambda/get-first-value/", "how-to-use-get-name": "/plugins/magic.lambda/get-name/", "how-to-use-get-nodes": "/plugins/magic.lambda/get-nodes/", "how-to-use-get-value": "/plugins/magic.lambda/get-value/", "how-to-use-include": "/plugins/magic.lambda/include/", "how-to-use-insert-after": "/plugins/magic.lambda/insert-after/", "how-to-use-insert-before": "/plugins/magic.lambda/insert-before/", "how-to-use-not-exists": "/plugins/magic.lambda/not-exists/", "how-to-use-not-null": "/plugins/magic.lambda/not-null/", "how-to-use-null": "/plugins/magic.lambda/null/", "how-to-use-reference": "/plugins/magic.lambda/reference/", "how-to-use-remove-nodes": "/plugins/magic.lambda/remove-nodes/", "how-to-use-set-name": "/plugins/magic.lambda/set-name/", "how-to-use-set-value": "/plugins/magic.lambda/set-value/", "how-to-use-set-x": "/plugins/magic.lambda/set-x/", "how-to-use-unwrap": "/plugins/magic.lambda/unwrap/"}
---

## Modifying your Hyperlambda graph object

Since there are no explicit variables in Hyperlambda, yet all nodes potentially might change, this requires
the ability to change your nodes as you execute your Hyperlambda. Magic provides many slots to achieve this,
both to change the names, values, and types of your nodes - In addition to adding a range of nodes into some
other node, and/or remove nodes from the children collection of your nodes.

* [`add`](/plugins/magic.lambda/add/) - This slot allows you to dynamically add nodes into a destination node.
* [`insert-before`](/plugins/magic.lambda/insert-before/) - This slot works the exact same way as the [add] node, except it will insert the nodes before the node(s) referenced in its main/destination argument.
* [`insert-after`](/plugins/magic.lambda/insert-after/) - This slot works the exact same way as the [add] and [insert-before] slots, except it will insert the nodes after the node(s) referenced in its main/destination argument.
* [`remove-nodes`](/plugins/magic.lambda/remove-nodes/) - This slot will remove all nodes its expression is pointing to.
* [`include`](/plugins/magic.lambda/include/) - This slot is logically the combination of a [for-each], [add] and [eval/invoke].
* [`filter`](/plugins/magic.lambda/filter/) - Filter allows you to filter using a predicate.
* [`set-value`](/plugins/magic.lambda/set-value/) - Changes the value of all nodes referenced as its main expression to whatever its single source happens to be.
* [`set-x`](/plugins/magic.lambda/set-x/) - Similar to [set-value], but does not evaluate expressions found in its source.
* [`set-name`](/plugins/magic.lambda/set-name/) - Changes the name of all nodes referenced as its main expression to whatever its single source happens to be.
* [`unwrap`](/plugins/magic.lambda/unwrap/) - This slot is useful if you want to evaluate some expression before the node where it's referenced is reached.
* [`get-value`](/plugins/magic.lambda/get-value/) - Returns the value of the node its expression is pointing to.
* [`get-name`](/plugins/magic.lambda/get-name/) - Returns the name of the node referenced in its expression.
* [`get-count`](/plugins/magic.lambda/get-count/) - This slot returns the number of nodes its expression is pointing to.
* [`get-nodes`](/plugins/magic.lambda/get-nodes/) - Returns the nodes its expression is referencing.
* [`exists`](/plugins/magic.lambda/exists/) - [exists] will evaluate to true if its specified expression yields one or more results.
* [`not-exists`](/plugins/magic.lambda/not-exists/) - [not-exists] will evaluate to true if its specified expression yields zero results.
* [`null`](/plugins/magic.lambda/null/) - [null] will evaluate to true if its specified expression yields null, or the expression returns no nodes.
* [`not-null`](/plugins/magic.lambda/not-null/) - [not-null] will evaluate to true if its specified expression returns nodes and at least one of those nodes has a value.
* [`reference`](/plugins/magic.lambda/reference/) - This slot will evaluate its expression, and add the entire node the expression is pointing to, as a referenced node into its value.
* [`get-first-value`](/plugins/magic.lambda/get-first-value/) - Returns the first non-null value resulting from evaluating its expression, and/or its children nodes.
* [`get-context`](/plugins/magic.lambda/get-context/) - This slot returns a context stack object, which is an object added to the stack using [context].
