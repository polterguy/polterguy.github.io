---
title: "How to use [case]"
description: "How to use [case] - first [case] node with a value matching the evaluated value of the [switch] node, and execute that .val:foo .result switch:x:@.val    case:bar       set-value:x:@.result          .:Oops    case:foo"
generated: true
guide: true
---

The reference page of [`case`](/reference/slots/core/case/) has its arguments, constraints and declaration.

**[switch]** works similarly to a switch/case block in a traditional programming language, and will find the
first **[case]** node with a value matching the evaluated value of the **[switch]** node, and execute that
**[case]** node as a lambda object.

```
.val:foo
.result
switch:x:@.val

   case:bar
      set-value:x:@.result
         .:Oops

   case:foo
      set-value:x:@.result
         .:Success!
```

**[switch]** can only contain two types of children nodes; **[case]** and **[default]**. The **[default]** node
will be evaluated if _none_ of the **[case]** node's values are matching the evaluated value of your **[switch]**.
Try evaluating the following in your _"Eval"_ component to understand this.

```
.val:fooXX
.result
switch:x:@.val

   case:bar
      set-value:x:@.result
         .:Oops

   case:foo
      set-value:x:@.result
         .:Oops2.0

   default
      set-value:x:@.result
         .:Success!
```

In the above, the expression evaluated in the switch, which is `@.val` will become _"fooXX"_ after evaluating it.
None of its children **[case]** nodes contains this as an option, hence the **[default]** node will be evaluated,
and this results in setting the **[.result]** node's value to _"Success!"_.

**[default]** _cannot_ have a value, and all your **[case]** nodes must have a value, either a constant or
an expression. However, any types can be used as values for your **[case]** nodes. And your **[switch]** node
must at the very least have minimum one **[case]** node. The **[default]** node is optional though. You can mix
and match different types as you see fit in your **[case]** nodes.
