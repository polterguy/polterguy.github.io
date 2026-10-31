---
title: "How to use [signal]"
description: "How to use [signal] - Invokes a previously created dynamic slot."
generated: true
guide: true
---

The reference page of [`signal`](/reference/slots/core/signal/) has its arguments, constraints and declaration.

Invokes a previously created dynamic slot. Assuming you have created the foo slot from the create slot example,
you can invoke the slot using the following Hyperlambda.

```
signal:foo
```

After evaluating the above Hyperlambda, the **[signal]** node will end up having a value of _"57"_.

**Notice** - This slot obeys by the rules of **[whitelist]** invocations from magic.lambda, allowing you to
declare a list of dynamic slots, which are exclusively allowed to be invoked temporarily inside of an
invocation to whitelist, allowing you to restrict some piece of potentially unsafe code to *only* signal
a pre-defined list of dynamically created slots. Below is an example.

```
slots.create:foo1
   return-value:Safe

slots.create:foo2
   return-value:Unsafe

whitelist

   vocabulary
      signal
      signal:foo1

   .lambda

      // Assuming you have a [foo1] slot created, this will work
      signal:foo1

      // This will throw, since [foo2] is not whitelisted
      signal:foo2
```

Basically, _only_ the slots declared in the above **[vocabulary]** will be allowed to be invoked inside
of the above **[.lambda]** object. You must have your dynamic slots declared as **signal:slot-name**,
such as the above illustrates. And in order to signal dynamic slots *at all*, you'll need to (obviously)
whitelist **[signal]** itself, as illustrated in the above code. Read more about **[whitelist]** in 
the magic.lambda project. Inside your slots though any **[whitelist]** invocations will simply be ignored,
allowing you to whitelist a single dynamic slot, for then to ignore what the slot itself is doing internally.
This _might_ create security issues for you if you have dynamically created slots that for some reasons
execute lambda object supplied to them. Hence as a general rule of thumb, you should _avoid_ whitelisting
slots that executes lambda objects supplied to them. The same is true for Hyperlambda files executed with
**[execute-file]** or **[io.file.execute]**, which you can pin in a whitelist by path - see
[magic.lambda.io](/plugins/magic.lambda.io/).
