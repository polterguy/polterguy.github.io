---
title: Hyperlambda exceptions
description: The [try] and [throw] slots, allowing you to catch exceptions and throw your own from Hyperlambda.
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

### How to use [try]

This slot allows you to create a try/catch/finally block in Hyperlambda, from where exceptions are caught,
and optionally handled in a **[.catch]** lambda, and/or a **[.finally]** lambda.

```
try
   throw:Whatever

.catch
   log.info:ERROR HAPPENED!! 42, 42, 42!

.finally
   log.info:Yup, we are finally there!
```

Semantically this works the exact same way as try/catch/finally in other programming languages, such as
C# for instance, in that an exception thrown inside of a try/catch block will always end up inside of
its **[.catch]** block - And regardless of whether or not an exception is thrown, the **[.finally]**
block will _always_ execute, allowing you to some extent create deterministic execution of Hyperlambda
code, which has a guarantee of executing, regardless of whether or not an exception is thrown or not.

### How to use [throw]

This slot simply throws an exception, with the exception message taken from its value.
See the **[try]** slot above for an example. Notice, you can make the exception propagate to the client
by adding a **[public]** parameter, and set its value to boolean _"true"_ - At which point
the exception will be returned to the client, even in release builds, if no **[.catch]** block
handles it before it propagates to the client - Otherwise the exception
will only be visible in debug builds, and never returned to the client. You can also modify
the **[status]** HTTP return value that's returned to the client, to become e.g. 404,
indicating _"not found"_, etc. In addition you can pass in a **[field]** which will be serialised
back to the client if specified to help the client to semantically figure out which field
that triggered the exception. Below is an example of all of the above.

```
throw:Whatever error message here
   status:398
   public:true
   field:whatever-field
```

If you create an endpoint using for instance _"Hyper IDE"_, and throw the above exception, you can see
how this propagates to the client without the exception handler.
