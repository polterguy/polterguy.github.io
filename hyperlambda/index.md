---
title: Hyperlambda
description: Hyperlambda is a relational file format allowing you to create execution trees, replacing XML as a dynamic markup language for declarative programming
header:
  image: /assets/images/hyperlambda-wizard.png
---

Hyperlambda is at the core of Magic. It's the primary axiom around which everything evolves. Technically it's _not_ a programming language, even though you can create anything in it that you can create in any other programming language. In its purest form, it's a relational file format, similar to XML and JSON, that allows you to declaratively create execution trees, that just so happens to allow for executing functionality.

Such execution trees can be automatically created by the machine itself to a much larger extent than traditional programming languages allows for, allowing the software developer to become more of an _"orchestrator"_ than an actual player. There's a reason we say the following about Magic Cloud.

> Where the Machine Creates the Code

Hyperlambda is implemented in C# and runs on .Net Core version 8, but you rarely have to consider this, unless you want to extend Hyperlambda with your own keywords, or use it as a DSL.

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

The above invocation to **[for-each]** is referred to as a _"slot invocation"_, and the **[for-each]** slot is implemented in C#, specifically in the [magic.lambda](/plugins/magic.lambda/#how-to-use-for-each) project. Typically we refer to such slots in Magic's documentation using square brackets and bold text.

Hyperlambda contains slots for all the most important programming constructs, such as **[if]**, **[while]**, **[slots.create]**, **[execute-file]**, etc - Allowing you to use it as if it was a programing language, even though technically it's not.

* [Read more about the programming constructs of Hyperlambda](/plugins/magic.lambda/)

## Hyperlambda structure

Hyperlambda is based upon nodes. Nodes have the following attributes.

* Name - Must be a string
* Value - Can be any object
* Children - Its children nodes

The name is separated from its value by a `:`, and children are found beneath a node, with 3 additional SP characters to _"scope"_ them as children of its above node. In the above example, our **[.data]** node has 3 children; **[item1]**, **[item2]**, and **[item3]**.

Contrary to JSON, Hyperlambda does _not_ require unique names. JSON maps to fields, which is a dictionary - While Hyperlambda nodes have a _list_ of children and is not using a dictionary that requires unique names. This has huge syntactic advantages, making it much less verbose, while still being ridiculously fast to parse. To illustrate the advantage, try to imagine how you would declare a segment in JSON having two consecutive **[if]** nodes.

Hyperlambda is the name of the file format in its text representation. Lambda is the name of the nodes in memory, after having been parsed into a graph object. This distinction is similar to XML, operating with XML DOM or the XML Document Object Model.

It could be argued that Hyperlambda is a simplified and humanly readable XML alternative.

* [Read more about nodes](/plugins/magic.node/)

## Lambda expressions

Lambda expressions are what allows you to reference nodes in your lambda objects. They're similar to XPath, but have more features, and are in general more powerful.

Technically Hyperlambda doesn't have variables. This is because _everything_ is a potential variable in Hyperlambda. However, by convention the Hyperlambda executor will not evaluate nodes prepended with a `.` character. This allows you to declare _"data segments"_ by prepending your node's name with a dot, such as illustrated in our above example with our **[.data]** node.

Without the dot character in our above example, the Hyperlambda execution engine would attempt to invoke **[data]** as a _"slot"_. There's no slot named **[data]** so this would result in a runtime error.

* [Read more about lambda expressions](/plugins/magic.node/#lambda-expressions)

## Hyperlambda types

Hyperlambda is a functional programming language and does not allow for declaring classes or types. However, it does contain basic support for native types such as integers, strings, date and time objects, etc. Such type declarations are squeezed in between the name of your node and its value such as follows.

```
.foo1:int:5
.foo2:long:55
.foo3:string:Howdy world
```

String is the default type unless another type is explicitly declared, and strings only needs `"` or `'` if they contain colons (`:`) or quoting characters as a part of their values. Strings are treated the same way as in C#, except Hyperlambda doesn't support extrapolated strings, only `@"` and `"` types of strings.

* [Read more about Hyperlambda types](/plugins/magic.node/#hyperlambda-types)

## Hyperlambda execution

You can use the [Hyperlambda Playground](/dashboard/hyperlambda-playground/) to play with Hyperlambda, and execute snippets of Hyperlambda code in _"immediate"_ mode.

The Hyperlambda execution engine, or the **[eval]** slot from [magic.lambda](/plugins/magic.lambda/#how-to-use-eval), executes nodes sequentially from top to bottom, assuming everything is a slot, unless it starts with a `.` character. Most slots require arguments, which sometimes are given in the form of lambda objects, such as illustrated below.

```
.source
   foo1:bar1
   foo2:bar2
.destination
add:x:@.destination
   get-nodes:x:@.source/*
```

The above **[add]** node for instance, is given a lambda object containing one node, being **[get-nodes]**. Our above **[get-nodes]** invocation is executed first, becoming the source for our **[add]** invocation - Resulting in the following result after execution.

```
.source
   foo1:bar1
   foo2:bar2
.destination
   foo1:bar1
   foo2:bar2
add:x:@.destination
```

As you can see we created a copy of each child node of our **[.source]** node, and appended these into our **[.destination]** node.

* [Read more about eval](/plugins/magic.lambda/#how-to-use-eval)

## Reference documentation

The most important parts of Hyperlambda is implemented in the following projects. If you want to dive deep into Hyperlambda you should probably read the documentation to both of these projects.

* [magic.lambda](/plugins/magic.lambda/)
* [magic.node](/plugins/magic.node/)
