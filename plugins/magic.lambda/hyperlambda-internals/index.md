---
title: "Hyperlambda internals"
description: "Hyperlambda internals - Everything is a slot in Hyperlambda."
generated: true
---

This page is part of the [magic.lambda](/plugins/magic.lambda/) documentation.

_Everything_ is a slot in Hyperlambda. This allows you to evaluate and extend its conditional operators and logical operators
the same way you would evaluate or create a function in a traditional programming language. This might at first seem a bit weird
if you come from a traditional programming language, but has a lot of advantages, such as allowing the computer to look
at the entirety of your function object as a hierarchical tree structure, parsing it as such, and executing your lambda
object as an _"execution tree"_.

In a normal programming language, the equal operator must have a left hand side (lhs), and a right hand
side (rhs). In Hyperlambda this is different, since the equal slot is the main invocation of a function, requiring two
arguments, allowing you to think about it as a _function_. To compare this to the way a traditional programming might
have implemented this, imagine the equal operator as a function, such as the following pseudo code illustrates.

```
equals(object lhs, object rhs)
```

The actual Hyperlambda code that would be the equivalent of the above pseudo code, can be found below, and this code
actually executes successfully if you execute it as Hyperlambda.

```
eq
   .:lhs
   .:rhs
```

As you study Hyperlambda it might be beneficial to use the _"Hyperlambda Playground"_ component that you can find in its
frontend dashboard. This component allows you to play with Hyperlambda in _"immediate mode"_,
experiment with Hyperlambda, execute it immediately from your browser, in a rich code editor,
providing syntax highlighting for you, autocomplete on slots, etc. The _"Hyperlambda Playground"_ component also allows
you to save your snippets for later on your server.

If you put your cursor on an empty line and click CTRL+SPACE or FN+CONTROL+SPACE on a Mac, you will be given
autocomplete, allowing you to easily see which slots are available for you.

Logically the Hyperlambda evaluator will signal each node in your Hyperlambda code sequentially, assuming
all of your nodes are referencing an `ISlot` class, unless the node's name starts with a _"."_ or has an empty name.
Most slots again are recursively executing their children slots, resulting in a recursively executed _"execution tree"_.

---

[all of magic.lambda](/plugins/magic.lambda/) | [Hyperlambda structure &rarr;](/plugins/magic.lambda/hyperlambda-structure/)
