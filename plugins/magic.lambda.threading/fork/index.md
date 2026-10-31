---
title: "How to use [fork]"
description: "How to use [fork] - Forks the given lambda into a new thread of execution, using a thread from the thread pool."
generated: true
guide: true
---

This is the guide to [`fork`](/reference/slots/core/fork/), whose reference page has its arguments, constraints and declaration.

Forks the given lambda into a new thread of execution, using a thread from the thread pool. This
slot is useful for creating _"fire and forget"_ lambda objects, where you don't need to wait
for the result of the execution before continuing executing the current scope.

```
fork
   info.log:I was invoked from another thread
```

To understand how **[fork]** works, you can imagine your computer's CPU as a single river,
running down hill, and at some point the river divides into two equally large rivers. This is
referred to as _"a fork"_. The analogy of the river becomes important for another reason, which
is the understanding of that the total amount of water is still the same, it's only parted
into two smaller rivers - Implying you cannot _"do more"_ with multi tasking, you can only
equally share the same amount of resources as you had before between two different tasks.
Multi threading does not make your CPU faster, it only schedules your CPU's time on multiple
things, doing these things concurrently. However, if you have multiple tasks where each
individual task needs to wait for IO data, threading typically speeds up your application,
since it can make multiple requests for IO simultaneously, and have other machines, and/or
processes working in parallel.
