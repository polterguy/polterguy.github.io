---
title: "How to use [slots.exists]"
description: "How to use [slots.exists] - Returns true if the specified slot exists."
generated: true
guide: true
---

This is the guide to [`slots.exists`](/reference/slots/slots/slots.exists/), whose reference page has its arguments, constraints and declaration.

Returns true if the specified slot exists. Example can be found below.

```
slots.create:foo
   return-value:Blah, blah, blah ...

slots.exists:foo
slots.exists:DOES-NOT-EXISTS
```
