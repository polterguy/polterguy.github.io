---
title: "How to use [whitelist]"
description: "How to use [whitelist] - This slot temporarily within the given scope changes the available slots, allowing you to declare a block of lambda, where only a sub-set of your vocabulary is available for some piece of code..."
generated: true
guide: true
---

The reference page of [`whitelist`](/reference/slots/core/whitelist/) has its arguments, constraints and declaration.

This slot temporarily within the given scope changes the available slots, allowing you to declare a block
of lambda, where only a sub-set of your vocabulary is available for some piece of code to invoke. This allows
you to relatively securely allow some partially untrusted source to pass in a piece of Hyperlambda, for then
to allow it to evaluate its own Hyperlambda. The slot takes two arguments.

* __[vocabulary]__ - Whitelisted slots
* __[.lambda]__ - Lambda object to evaluate for the given scope

```
.result
whitelist

   vocabulary
      set-value
      return

   .lambda

      // Inside of this [.lambda] object, we can only invoke [set-value], and no other slots!
      set-value:x:@.result
         .:foo

      // Notice, the next line will throw an exception if you remove its "." character,
      // because [add] is not whitelisted in our above [vocabulary] declaration!
      .add:x:@.result
         .
            foo:bar
      return
         result:success
```

For security reasons the **[whitelist]** invocation's **[.lambda]** object is immutable, and the
caller _cannot_ access nodes outside of the **[.lambda]** object itself, which prohibits the caller
to modify, and/or read nodes from outside of its **[whitelist]** invocation. In addition a **[whitelist]**
invocation creates its own result stack object, allowing the **[whitelist]** invocation to return values
and nodes to the caller using for instance the **[return]** slot. If you execute the above Hyperlambda
you can see how this semantically works by realizing how the above **[.result]** node never has its
value actually changed, because our invocation to **[set-value]** inside our whitelist invocation yields
a _"null node-set result"_. Hence, semantically the **[whitelist]** slot works the same way signaling
a dynamic slot works in Hyperlambda, in that the invocation treats its **[.lambda]** object as if
it was a dynamic slot, isolating it from the rest of our code, allowing the lambda object to return
values and nodes to the caller.
