---
title: magic.lambda
description: The programming language keywords of Hyperlambda - branching, loops, comparisons, exception handling, and the slots that modify your lambda object.
---

magic.lambda is where you will find the _"programming language keywords"_ of Hyperlambda.
It is what makes Hyperlambda Turing complete, and contains slots such as **[for-each]**,
**[if]**, and **[while]**. If you want to learn more, this is probably where you should start.

Notice, you do _not_ need to master these slots to use Magic - the
[Hyperlambda Generator](/dashboard/hyperlambda-generator/) writes the code for you from plain
English. This reference exists for when you want to read, understand, or hand-modify what the
machine created.

## Reference documentation

The documentation is organised by concept, with one page per concept.

* [Hyperlambda internals](/plugins/magic.lambda/internals/) - How the language works; its structure, tokens, slot invocations, and how to extend it with C#
* [Syntax and conventions](/plugins/magic.lambda/syntax/) - Comments, data segments, lambda expressions, and documentation conventions
* [Executing lambda objects](/plugins/magic.lambda/executing/) - **[compose]**, **[eval]** and **[invoke]**
* [Branching and conditional execution](/plugins/magic.lambda/branching/) - **[if]**, **[else-if]**, **[else]** and **[switch]**
* [Comparison and boolean logic](/plugins/magic.lambda/conditions/) - **[eq]**, **[neq]**, **[lt]**, **[lte]**, **[mt]**, **[mte]**, **[and]**, **[or]** and **[not]**
* [Modifying your lambda object](/plugins/magic.lambda/nodes/) - **[add]**, **[insert-before]**, **[set-value]**, **[unwrap]**, **[get-value]**, **[exists]**, **[reference]** and more
* [Hyperlambda exceptions](/plugins/magic.lambda/exceptions/) - **[try]** and **[throw]**
* [Hyperlambda loops](/plugins/magic.lambda/loops/) - **[for-each]** and **[while]**
* [Types and conversion](/plugins/magic.lambda/types/) - **[types]**, **[type]**, **[convert]**, **[format]**, **[int2words]** and **[vocabulary]**
