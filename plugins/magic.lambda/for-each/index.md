---
title: "How to use [for-each]"
description: "How to use [for-each] - Hyperlambda accepts comments the exact same way C# does, and you can use either multiline comments or single line comments, like the following example illustrates."
generated: true
guide: true
---

The reference page of [`for-each`](/reference/slots/core/for-each/) has its arguments, constraints and declaration.

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
