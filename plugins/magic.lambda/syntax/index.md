---
title: Hyperlambda syntax and conventions
description: Commenting your Hyperlambda code, declaring data segments, lambda expressions, and the documentation conventions used throughout these docs.
---

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
or variables for that matter. Below is an example where **[eval]** will simply ignore the **[.src]** node
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
for expressions in the [magic.node](https://docs.ainiro.io/plugins/magic.node/) project.
