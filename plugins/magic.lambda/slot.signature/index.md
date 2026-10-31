---
title: "How to use [slot.signature]"
description: "How to use [slot.signature] - Returns the documented input and output contract of a single compiled slot, given its name as the value of the slot, or an expression leading to its name."
generated: true
guide: true
---

The reference page of [`slot.signature`](/reference/slots/slot/slot.signature/) has its arguments, constraints and declaration.

Returns the documented input and output contract of a single compiled slot, given its name as the value of the slot,
or an expression leading to its name. The result is returned as child nodes, and may contain the following.

* __[input]__ - The value contract of the slot, with its `kind`, `description`, `required` and `mode`
* __[children]__ - The child nodes the slot accepts
* __[constraints]__ - Constraints between the child nodes
* __[scope]__ - Scopes the slot provides or requires
* __[output]__ - What the slot returns, with its `mode`, `kind` and `description`

```
slot.signature:slot.description
```

Invoking the above returns an **[input]** node declaring `kind` as _"slot-name"_ and `required` as true, in addition to an
**[output]** node declaring `kind` as _"slot-description,text"_. The slot throws an exception if no slot name is supplied, or if
the slot does not exist. Inside a **[whitelist]** invocation, it will also throw for slots the whitelist does not allow.
