---
title: magic.lambda
description: The programming language keywords of Hyperlambda - branching, loops, comparisons, exception handling, and the slots that modify your lambda object.
moved_anchors: {"extending-hyperlambda-with-c": "/plugins/magic.lambda/extending-hyperlambda-with-c/", "hyperlambda-internals": "/plugins/magic.lambda/hyperlambda-internals/", "hyperlambda-structure": "/plugins/magic.lambda/hyperlambda-structure/"}
---

magic.lambda is where you will find the _"programming language keywords"_ of Hyperlambda.
It is what makes Hyperlambda Turing complete, and contains slots such as **[\[for-each\]](/reference/slots/core/for-each/)**,
**[\[if\]](/reference/slots/core/if/)**, and **[\[while\]](/reference/slots/core/while/)**. If you want to learn more, this is probably where you should start.

Notice, you do _not_ need to master these slots to use Magic - the
[Hyperlambda Generator](/dashboard/hyperlambda-generator/) writes the code for you from plain
English. This reference exists for when you want to read, understand, or hand-modify what the
machine created.


## Reference documentation

The slot reference is organised by concept, with one page per concept.

* [Executing lambda objects](/plugins/magic.lambda/executing/) - **[\[compose\]](/reference/slots/core/compose/)**, **[\[eval\]](/reference/slots/core/eval/)** and **[\[invoke\]](/reference/slots/core/invoke/)**
* [Branching and conditional execution](/plugins/magic.lambda/branching/) - **[\[if\]](/reference/slots/core/if/)**, **[\[else-if\]](/reference/slots/core/else-if/)**, **[\[else\]](/reference/slots/core/else/)** and **[\[switch\]](/reference/slots/core/switch/)**
* [Comparison and boolean logic](/plugins/magic.lambda/conditions/) - **[\[eq\]](/reference/slots/core/eq/)**, **[\[neq\]](/reference/slots/core/neq/)**, **[\[lt\]](/reference/slots/core/lt/)**, **[\[lte\]](/reference/slots/core/lte/)**, **[\[mt\]](/reference/slots/core/mt/)**, **[\[mte\]](/reference/slots/core/mte/)**, **[\[and\]](/reference/slots/core/and/)**, **[\[or\]](/reference/slots/core/or/)** and **[\[not\]](/reference/slots/core/not/)**
* [Modifying your lambda object](/plugins/magic.lambda/nodes/) - **[\[add\]](/reference/slots/core/add/)**, **[\[insert-before\]](/reference/slots/core/insert-before/)**, **[\[set-value\]](/reference/slots/core/set-value/)**, **[\[set-x\]](/reference/slots/core/set-x/)**, **[\[unwrap\]](/reference/slots/core/unwrap/)**, **[\[get-value\]](/reference/slots/core/get-value/)**, **[\[exists\]](/reference/slots/core/exists/)**, **[\[reference\]](/reference/slots/core/reference/)** and more
* [Hyperlambda exceptions](/plugins/magic.lambda/exceptions/) - **[\[try\]](/reference/slots/core/try/)** and **[\[throw\]](/reference/slots/core/throw/)**
* [Hyperlambda loops](/plugins/magic.lambda/loops/) - **[\[for-each\]](/reference/slots/core/for-each/)**, **[\[map\]](/reference/slots/core/map/)** and **[\[while\]](/reference/slots/core/while/)**
* [Types and conversion](/plugins/magic.lambda/types/) - **[\[types\]](/reference/slots/core/types/)**, **[\[type\]](/reference/slots/core/type/)**, **[\[convert\]](/reference/slots/core/convert/)**, **[\[floatArray2bytes\]](/reference/slots/core/floatArray2bytes/)**, **[\[format\]](/reference/slots/core/format/)**, **[\[int2words\]](/reference/slots/core/int2words/)**, **[\[vocabulary\]](/reference/slots/core/vocabulary/)**, **[\[slot.signature\]](/reference/slots/slot/slot.signature/)** and **[\[slot.description\]](/reference/slots/slot/slot.description/)**


## How Hyperlambda invokes slots

At the heart of Hyperlambda is the **[\[eval\]](/reference/slots/core/eval/)** slot. This slot is responsible for executing your lambda object
and follows a couple of simple rules. All nodes starting with a _"."_ will be ignored, and **[\[eval\]](/reference/slots/core/eval/)** will not
try to raise these nodes as signals. This has two benefits.

1. You can create _"hidden"_ slots, that are only accessible from C#.
2. You can use nodes starting with _"."_ as data nodes, separating function invocations from data.

**[\[eval\]](/reference/slots/core/eval/)** makes Hyperlambda _"super functional"_ in nature. Below is an example of a Hyperlambda
piece of code, that illustrates this, by adding a _"callback"_ lambda object to its **[\[while\]](/reference/slots/core/while/)** invocation
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


## Hyperlambda tokens

The separating of a node's name and its value is done by using a `:` character. To the left is the node's
name, and to the right is its value. The value of a node can also be a C# type of string, using double
quotes, and even single quotes, or prefix your opening double quote with an "@" character, allowing you
to use carriage returns in your strings the same way you can in for instance C#. Below are some examples.

```
.str1:"   This is a \r\n  string"
.str2:' This is also a string '
.str3:@"This
    is
  also a
      string"
```

Strings in Hyperlambda can be escaped with the exact same semantics as you would escape your C# strings,
including referencing UNICODE characters in your strings. Hyperlambda is _always_ serialized using UTF8,
so you can add any UNICODE characters in your Hyperlambda you wish. Just make sure you save your files
as UTF8 if you are using an external code editor to edit your Hyperlambda files.


## How to comment your Hyperlambda code

Hyperlambda accepts comments the exact same way C# does, and you can use either multiline comments
or single line comments, like the following example illustrates.

```
/*
 * Multiline comment.
 */

// Single line comment.
```

You _cannot_ put comments on lines containing nodes, and comments must be indented the same
amount of indentations as the nodes they are commenting, implying the nodes below them. Below is
an example.

```
.data
   foo1:bar1
   foo2:bar2

for-each:x:@.data/*

   // This is correct indentation.
   set-value:x:@.dp/#
      .:Loop was here ...
```

Since Hyperlambda is using spaces (SP characters) to denote scope, indentation _is important_,
also for comments. If you de-indent the above comment, you might get unpredictable results, in particular
if you're serializing and de-serializing your Hyperlambda preserving comments. Comments should as a general
rule of thumb be applied with the same amount of indentation as the node below them.


## Hyperlambda data segments

Hyperlambda does not separate between a _"variable"_ and a _"function invocation"_. Hence, a node
might serve as both at the same time. This allows you to dynamically modify your lambda structure, as you
traverse it and execute it. But this creates another problem for you, which is that you will need
a mechanism to store data. This is accomplished by prefixing a node's name with a `.` character, at which point
the Hyperlambda evaluator will ignore it, as it is traversing your tree, and _not_ attempt to signal
that particular node as a slot. Think of all nodes starting with a `.` character as _"data segments"_,
or variables for that matter. Below is an example where **[\[eval\]](/reference/slots/core/eval/)** will simply ignore the **[.src]** node
and the **[.dest]** node, not attempting to invoke these as slots, but treat these as _"data nodes"_.

```
.src:foo
.dest
set-value:x:@.dest
   get-value:x:@.src
```

If you change name of the above **[.src]** node to simply **[src]**, your code will raise an exception,
with an error such as follows _"No slot exists for [src]"_ since this slot doesn't exist in your Hyperlambda
vocabulary - Unless you for some reasons have an installation where this slot has been explicitly added to
your vocabulary.


## Hyperlambda documentation conventions

When we document Hyperlambda slots, and nodes, which are almost the same, we will document the node's
name with square brackets surrounding it, such as **[this]** illustrates, where _"this"_ is referencing
a node, and is the name of a node. We will also make such node references **bold**, to make them
more easy to see.


## Lambda expressions

Hyperlambda is heavily using _"lambda expressions"_. Think of these like XPath, except instead
of referencing XML nodes they're referencing Hyperlambda nodes. You can find the documentation
for expressions in the [magic.node](/plugins/magic.node/) project.


## Topics

* [Hyperlambda internals](/plugins/magic.lambda/hyperlambda-internals/) - Everything is a slot in Hyperlambda.
* [Hyperlambda structure](/plugins/magic.lambda/hyperlambda-structure/) - Hyperlambda is the textual representation of a node structure, where each node has a name, an optional value, and a collection of children nodes.
* [Extending Hyperlambda with C#](/plugins/magic.lambda/extending-hyperlambda-with-c/) - To understand the relationship between C# and Hyperlambda, it might be beneficial for you to analyze the following code.
