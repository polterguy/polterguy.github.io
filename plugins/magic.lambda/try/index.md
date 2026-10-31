---
title: "How to use [try]"
description: "How to use [try] - This slot allows you to create a try/catch/finally block in Hyperlambda, from where exceptions are caught, and optionally handled in a [.catch] lambda, and/or a [.finally] lambda."
generated: true
guide: true
---

The reference page of [`try`](/reference/slots/core/try/) has its arguments, constraints and declaration.

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
