---
title: "How to use [strings.builder.append]"
description: "How to use [strings.builder.append] - Appends its value to the closest [strings.builder] scope."
generated: true
guide: true
---

The reference page of [`strings.builder.append`](/reference/slots/strings/strings.builder.append/) has its arguments, constraints and declaration.

Appends its value to the closest **[strings.builder]** scope. The slot requires a value, which can be a constant
or an expression, and can only be used inside a **[strings.builder]** invocation. See the example in the
documentation for **[strings.builder]** above.

Creates a string builder scope. Every **[strings.builder.append]** invocation found inside it appends its value
to the builder, and when the scope ends the value of **[strings.builder]** becomes the concatenated text.
Its children are evaluated as a lambda object, and the slot has no arguments of its own.

```
strings.builder
   strings.builder.append:"howdy"
   strings.builder.append:" world"
get-value:x:@strings.builder
```
