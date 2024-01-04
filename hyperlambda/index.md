---
title: Hyperlambda
description: Hyperlambda is a relational file format allowing you to create execution trees, replacing XML as a dynamic markup language for declarative programming
---

Hyperlambda is at the core of Magic. It's the primary axiom around which everything evolves. Technically it's _not_ a programming language, even though you can create anything you can create in any other programming language in it. In its purest form, it's a relational file format, similar to XML and JSON, that allows you to declaratively create execution trees, that just so happens to allow for creating computer functionality.

## Hyperlambda example

Below is an example Hyperlambda snippet to show you its syntax.

```
// Illustrates how to use a [for-each] loop to iterate some node-set.
.data
   item1:Hello from Item1
   item2:Hello from Item2
   item3:Hello from Item3
for-each:x:@.data/*
   log.info:x:@.dp/#
```

The above code _"declares"_ a `for-each` loop, that iterates through each of our **[.data]** node's children, and creates a log entry with its value as it iterates.

## Hyperlambda structure

Hyperlambda is based upon nodes. Each node have the following attributes.

* Name - Must be a string
* Value - Can be any object
* Children - Its children nodes

The name is separated from its value by a `:`, and children are found beneath a node, with 3 additional SP characters to _"scope"_ them as children of its above node. In the above example, our **[.data]** node has 3 children; **[item1]**, **[item2]**, and **[item3]**.

Contrary to JSON, Hyperlambda does _not_ require unique names. JSON maps to fields, which is a dictionary - While Hyperlambda nodes have _list_ of children and is not using a dictionary that requires unique names. This has huge syntactic advantages, making it much less verbose, while still being ridiculously fast to parse. To illustrate the advantage, try to imagine how you would declare a segment in JSON having two consecutive **[if]** nodes.

Hyperlambda is the name of the file format in its text representation. Lambda is the name of the nodes in memory, after having been parsed into a graph object. This distinction is similar in XML which operates with DOM or Document Object Model.

## Lambda expressions

Lambda expressions are what allows you to reference nodes in your lambda objects. They're similar to XPath, but have more features, and are in general more powerful.

Technically Hyperlambda doesn't have variables. This is because _everything_ is a potential variable in Hyperlambda. However, by convention the Hyperlambda executor will not evaluate nodes prepended with a `.` character. This allows you to declare _"data segments"_ by prepending your node's name with a dot, such as illustrated in our above example with our **[.data]** node.

Without the dot character in our above example, the Hyperlambda execution engine would attempt to invoke **[data]** as a _"slot"_. There's no slot named **[data]** so this would result in a runtime error.

Read more about Hyperlambda and lambda expressions below.

* [magic.node](/plugins/magic.node/)
* [magic.lambda](/plugins/magic.lambda/)
* [magic.signals](/plugins/magic.signals/)
* [magic.lambda.hyperlambda](/plugins/magic.lambda.hyperlambda/)