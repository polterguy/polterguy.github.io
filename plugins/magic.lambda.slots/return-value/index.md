---
title: "How to use [return-value]"
description: "How to use [return-value] - Returns a single value from your slot."
generated: true
guide: true
---

This is the guide to [`return-value`](/reference/slots/core/return-value/), whose reference page has its arguments, constraints and declaration.

Returns a single value from your slot. Can only be invoked from the inside of
a dynamically created slot, and other slots explicitly creating a return context. An example can be
found below.

```
slots.create:foo
   return-value:This becomes the returned value from your slot

signal:foo
```
