---
title: "How to use [sleep]"
description: "How to use [sleep] - This slot will sleep the current thread for x number of milliseconds, where x is an integer value, expected to be passed in as its main value."
generated: true
guide: true
---

The reference page of [`sleep`](/reference/slots/core/sleep/) has its arguments, constraints and declaration.

This slot will sleep the current thread for x number of milliseconds, where x is an integer value, expected
to be passed in as its main value.

```
// Sleeps the main thread for 1 second, or 1000 milliseconds.
sleep:1000
```

**Notice** - This slot is typically releasing the thread back to the operating system, implying as
the current thread is _"sleeping"_, it will not be a blocking call, and require ZERO physical operating
system threads while it is sleeping. This is true because of Hyperlambda's 100% perfectly `async` nature.
