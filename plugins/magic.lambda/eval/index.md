---
title: "How to use [eval]"
description: "How to use [eval] - This is the by far most important slot in Hyperlambda, since it's arguably \"the heart\" of Hyperlambda, allowing Hyperlambda to execute."
guide: true
slots: ["eval"]
---

The reference page of [`eval`](/reference/slots/core/eval/) has its arguments, constraints and declaration.

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
