---
title: "How to use [join]"
description: "How to use [join] - Joins all child [fork] invocations, implying the slot will wait until all forks directly below it has finished executing, and automatically copy the result of the [fork] into the original node."
generated: true
guide: true
---

The reference page of [`join`](/reference/slots/core/join/) has its arguments, constraints and declaration.

Joins all child **[fork]** invocations, implying the slot will wait until all forks directly below it
has finished executing, and automatically copy the result of the **[fork]** into the original node.

```
join
   fork
      http.get:"https://servergardens.com"
   fork
      http.get:"https://gaiasoul.com"
```

As an analogy for what occurs above, imagine the two rivers from our above **[fork]** analogy
that forked from one larger river into two smaller rivers, for then again to join up and becoming one
large river again further down.
