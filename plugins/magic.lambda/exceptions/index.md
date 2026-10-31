---
title: Hyperlambda exceptions
description: The [try] and [throw] slots, allowing you to catch exceptions and throw your own from Hyperlambda.
moved_anchors: {"how-to-use-throw": "/plugins/magic.lambda/throw/", "how-to-use-try": "/plugins/magic.lambda/try/"}
---

## Hyperlambda exceptions

Exceptions in Hyperlambda are similar to exceptions in traditional programming languages, and are basically a
mechanism to raise errors in such a way that the stack is completely rewinded, to the point in your code
where you want to handle error conditions. This allows you to _"ignore"_ errors occurring in all places,
except a single point in your code, from where you want to handle said exceptions. Below is some example
Hyperlambda code illustrating how to use exceptions.

```
try
   throw:Whatever

.catch
   log.info:ERROR HAPPENED!! 42, 42, 42!

.finally
   log.info:Yup, we are finally there!
```

Like most modern programming languages, Hyperlambda supports both try, catch and finally. However,
the catch is referenced as **[.catch]** and the finally block is referenced as **[.finally]**.

* [`try`](/plugins/magic.lambda/try/) - This slot allows you to create a try/catch/finally block in Hyperlambda, from where exceptions are caught, and optionally handled in a [.catch] lambda, and/or a [.finally] lambda.
* [`throw`](/plugins/magic.lambda/throw/) - This slot simply throws an exception, with the exception message taken from its value.
