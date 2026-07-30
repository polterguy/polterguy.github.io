---
title: Branching and conditional execution
description: The [if], [else-if], [else] and [switch] slots, giving Hyperlambda its branching and conditional execution constructs.
---

## Hyperlambda branching and conditional execution

Branching implies to change the execution path of your code, and examples includes function invocations, and
other similar mechanisms that changes the position of your computer's _"execution pointer"_. Conditional
branching implies to changing the position of the execution pointer, according to some condition. Typically
this implies constructs such as `if`, `else`, `goto` etc in traditional programming languages.

### How to use [if]

This is the Hyperlambda equivalent of `if` from other programming languages. It allows you to test for some condition,
and evaluate a lambda object, only if the condition evaluates to true. **[if]** must be given two arguments.
The first argument can be anything, including a slot invocation - But its second argument must be its **[.lambda]**
argument. The **[.lambda]** node will be evaluated as a lambda object, only if the first argument to **[if]** evaluates
to boolean true. Below is an example.

```
.dest
if
   .:bool:true
   .lambda
      set-value:x:@.dest
         .:yup!
```

All conditional slots, including **[if]**, optionally accepts slots as their first condition argument.
This allows you to invoke slots, treating the return value of the slot as the condition deciding
whether or not the **[.lambda]** object should be executed or not. Below is an example.

```
.arguments
   foo:bool:true
.dest

if
   get-value:x:@.arguments/*/foo
   .lambda
      set-value:x:@.dest
         .:yup!
```

Notice, both the **[if]** slot and the **[else-if]** slot can optionally be directly pointing to an expression,
that is assumed to evaluate to either boolean `true` or boolean `false`, such as the following illustrates.

```
.arguments
   foo:bool:true
.dest

if:x:@.arguments/*/foo
   set-value:x:@.dest
      .:yup!
```

If you use this shorthand version for the slot(s), its lambda object is assumed to be the entirety of the content
of the **[if]** or **[else-if]** slot itself, and there are no needs to explicitly declare your lambda objects as
a **[.lambda]** argument. This only works if the expression leads to a boolean value.

### How to use [else-if]

**[else-if]** is the younger sibling of **[if]**, and must be preceded by its older sibling, or other **[else-if]** nodes,
and will only be evaluated if all of its previous conditional slots evaluates to false - At which point **[else-if]** is
allowed to test its condition - And only if its condition evaluates to true, it evaluate its lambda object. Semantically **[else-if]**
is similar to **[if]**, in that it requires two arguments with the same structure as **[if]**.

```
.dest
if
   .:bool:false
   .lambda
      set-value:x:@.dest
         .:yup!
else-if
   .:bool:true
   .lambda
      set-value:x:@.dest
         .:yup2.0!
```

**[else-if]** can also be given an expression directly the same way **[if]** can. See the example for **[if]**
to understand how this works.

### How to use [else]

**[else]** is the last of the _"conditional siblings"_ that will only be evaluated as a last resort, only if none of its
elder _"siblings"_ evaluates to true. Notice, contrary to both **[if]** and **[else-if]**, **[else]** contains its lambda object
directly as children nodes, and _not_ within a **[.lambda]** node. This is because **[else]** does not require any
conditional arguments like **[if]** and **[else-if]** does. An example can be found below.

```
.src:int:3
.dest
if
   eq
      get-value:x:@.src
      .:int:1
   .lambda

      set-value:x:@.dest
         .:yup!

else-if
   eq
      get-value:x:@.src
      .:int:2
   .lambda

      set-value:x:@.dest
         .:yup2.0!

else

   set-value:x:@.dest
      .:nope
```

### How to use [switch]

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
