---
title: "How to use [if]"
description: "How to use [if] - This is the Hyperlambda equivalent of if from other programming languages."
guide: true
slots: ["if"]
---

The reference page of [`if`](/reference/slots/core/if/) has its arguments, constraints and declaration.

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
