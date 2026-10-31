---
title: "How to use [try-signal]"
description: "How to use [try-signal] - Invokes a previously created dynamic slot."
generated: true
guide: true
---

The reference page of [`try-signal`](/reference/slots/core/try-signal/) has its arguments, constraints and declaration.

Invokes a previously created dynamic slot. This slot works exactly the same as **[signal]** except it does
not throw an exception if the slot does not exist. Assuming you have created the foo slot from the create slot example,
you can invoke the slot using the following Hyperlambda.

```
try-signal:foo
```
