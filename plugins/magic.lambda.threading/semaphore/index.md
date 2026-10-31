---
title: "How to use [semaphore]"
description: "How to use [semaphore] - Creates a named semaphore, where only one thread will be allowed to evaluate the same semaphore at the same time."
generated: true
guide: true
---

The reference page of [`semaphore`](/reference/slots/core/semaphore/) has its arguments, constraints and declaration.

Creates a named semaphore, where only one thread will be allowed to evaluate the same semaphore at
the same time. Notice, the semaphore to use is defined through its value, implying you can use the same
semaphore multiple places, by using the same value of your **[semaphore]** invocation.

```
semaphore:foo-bar
   /*
    * Only one thread will be allowed entrance into this piece of
    * code at the same time, ensuring synchronized access, for cases
    * where you cannot allow more than one thread to enter at the
    * same time.
    */
```

In the above semaphore _"foo-bar_" becomes the name of your semaphore. If you invoke **[semaphore]** in
any other parts of your Hyperlambda code, with _"foo-bar"_ as the value, only _one_ of your
lambda objects will be allowed to execute at the same time. This allows you to _"synchronize access"_
to shared resources, where only _one_ thread should be allowed to access the shared resource at the same
time. Such shared resources might be for instance files, or other things shared between multiuple threads,
where it's crucial that only one thread is allowed to access the shared resource at the same time.
