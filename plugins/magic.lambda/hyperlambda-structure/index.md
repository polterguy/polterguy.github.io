---
title: "Hyperlambda structure"
description: "Hyperlambda structure - Hyperlambda is the textual representation of a node structure, where each node has a name, an optional value, and a collection of children nodes."
generated: true
---

This page is part of the [magic.lambda](/plugins/magic.lambda/) documentation.

Hyperlambda is the textual representation of a node structure, where each node has a name, an optional value,
and a collection of children nodes. Imagine the following Hyperlambda.

```
name:value
   child1
```

In the above Hyperlambda there is one root node. Its name is _"name"_, its value is _"value"_, and this node
has one child node, with the name of _"child1"_. Its child node does _not_ however have a value, which results
in its value being _"null"_. The reason why the Hyperlambda parser understands _"child1"_ as the child of 
the _"name"_ node, is because it is prefixed by 3 spaces (SP) relative to the _"name"_ node. This allows you
to create graph objects (tree structures) with any depth you wish, by simply starting out with the number of
spaces the node above has, add 3 additional spaces, and you have declared children nodes of the node above.

If you think of these nodes as a sequence of function invocations, from the top to bottom, where all of the
nodes are assumed to be referencing slots, and all children nodes arguments to your slots - You can imagine
how the tree structure resulting from parsing Hyperlambda into a graph object can easily be evaluated, due
to its recursive nature, making it easy to express idioms such as _"if"_, _"while"_, _"for-each"_, etc. In
fact logically this is similar to the way XSLT works, except there's no XML, only Hyperlambda, lambda objects,
and nodes.

Since each slot will be invoked with the node referencing the slot itself as the _"input"_ `Node`,
this makes the Hyperlambda evaluator recursive in nature, allowing a slot to evaluate all of its children,
after executing its custom logic, etc. And yes, before you ask, Hyperlambda has been heavily influenced by
LISP. In some ways Hyperlambda _is_ Lisp for C#, only with a completely different syntax, and without S-Expressions.

---

[&larr; Hyperlambda internals](/plugins/magic.lambda/hyperlambda-internals/) | [all of magic.lambda](/plugins/magic.lambda/) | [Extending Hyperlambda with C# &rarr;](/plugins/magic.lambda/extending-hyperlambda-with-c/)
