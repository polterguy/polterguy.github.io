---
title: "How to use [slots.delete]"
description: "How to use [slots.delete] - Deletes a previously created dynamic slot."
generated: true
guide: true
---

The reference page of [`slots.delete`](/reference/slots/slots/slots.delete/) has its arguments, constraints and declaration.

Deletes a previously created dynamic slot. The following example _will throw an exception_.

```
slots.create:foo
   return-value:int:57

slots.delete:foo

// Throws exception, since [foo] no longer exists.
slots.get:foo
```
