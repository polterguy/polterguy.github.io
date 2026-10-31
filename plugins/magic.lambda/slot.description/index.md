---
title: "How to use [slot.description]"
description: "How to use [slot.description] - Returns the description of a single compiled slot, given its name as the value of the slot, or an expression leading to its name."
generated: true
guide: true
---

The reference page of [`slot.description`](/reference/slots/slot/slot.description/) has its arguments, constraints and declaration.

Returns the description of a single compiled slot, given its name as the value of the slot, or an expression
leading to its name.

```
slot.description:while
```

The above returns the value _"Repeats execution while a condition is true"_. The slot throws an exception if no slot name is
supplied, or if the slot does not exist. Inside a **[whitelist]** invocation, it will also throw for slots the whitelist does not allow.
