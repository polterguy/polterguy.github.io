---
title: "How to use [context]"
description: "How to use [context] - This slot allows you to add an object unto the stack, such that it can later be retrieved with the [get-context] slot."
guide: true
slots: ["context"]
---

The reference page of [`context`](/reference/slots/core/context/) has its arguments, constraints and declaration.

This slot allows you to add an object unto the stack, such that it can later be retrieved with
the **[get-context]** slot. Below is an example.

```
.result

context:foo
   value:bar
   .lambda

      set-value:x:@.result
         get-context:foo
```

The slot requires a name as the value of its slot invocation node, a **[value]** as the value
you want to put onto the stack, and a **[.lambda]** object being the lambda where the stack object
exists, and can be retrieved using **[get-context]**. This is quite useful if you have some piece
of data that needs to be accessible through the entirety of the execution of some Hyperlambda snippet,
implying also for slots you invoke, where you don't want to pass in the data as an argument to the
slot itself. Imagine the following to understand how this works.

```
slots.create:bar

   get-context:foo
   return:x:-

context:foo
   value:Context value
   .lambda

      signal:bar
```

If you execute the above Hyperlambda you will notice how the slot called **[bar]** actually has access to
the context value called _"foo"_, and can retrieve this. This feature allows you to declare and create
_"long lasting arguments"_ that are accessible from within the entirety of a piece of Hyperlambda, including
each slot it invokes, and/or Hyperlambda files it executes.
