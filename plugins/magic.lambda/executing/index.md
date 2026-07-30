---
title: Executing lambda objects
description: The [compose], [eval] and [invoke] slots, allowing you to compose lambda objects and execute them dynamically.
---

## How to use [compose]

Compose allows you to dynamically create expressions by supplying it with a list of iterators. To understand it
realise the following invocation.

```
compose
   .:..
   .:*
   .:.data
   .:*
```

Results in the following result.

```
compose:x:../*/.data/*
```

Since expressions are for the most parts recursively evaluated, this allows you to dynamically compose
expressions you de-reference, allowing you to dynamically create expressions you're using in your code.

## How to use [eval]

This is the by far most important slot in Hyperlambda, since it's arguably _"the heart"_ of Hyperlambda,
allowing Hyperlambda to execute. This slot executes the specified lambda object(s) assumed
to exist either as a lambda in its children collection, or as an expression leading to one or more nodes,
where each of these nodes will be executed. The example below illustrates how to use **[eval]** with
an expression.

```
.res

.lambda
   set-value:x:@.res
      .:OK

eval:x:@.lambda
```

Notice, you could have multiple **[.lambda]** nodes in the above Hyperlambda, at which point _all_
of these would be executed consecutively. Below is an example.

```
.res:

.lambda
   set-value:x:@.res
      strings.concat
         get-value:x:@.res
         .:" OK 1 "

.lambda
   set-value:x:@.res
      strings.concat
         get-value:x:@.res
         .:" OK 2 "

eval:x:../*/.lambda
```

You can also provide the lambda object as children of the **[eval]** node itself, such as the following
illustrates.

```
.res

eval
   set-value:x:@.res
      .:Yup!
```

Notice, the **[eval]** slot is _not_ immutable, as in it has access to the outer graph object such as
illustrated above, where we set the value of a node existing _outside_ of the **[.lambda]** itself.
Implying **[eval]** cannot return values or nodes the same way for instance **[signal]** can.

## How to use [invoke]

This slot works similarly to **[eval]**, except it treats the invocation similarly to an invocation to
a dynamic slot, allowing you to pass in arguments, and return nodes from the invocation.

```
.lambda
   strings.concat
      .:"Hello "
      get-value:x:@.arguments/*/name
   return:x:-
invoke:x:@.lambda
   name:John
```

Notice, you cannot supply an expression leading to multiple nodes, and the slot invokes the lambda
object immutable, such that it doesn't change. The invocation also does _not_ have access to anything
outside of its own lambda object.
