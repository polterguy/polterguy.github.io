---
title: "How to use [strings.builder]"
description: "How to use [strings.builder] - Creates a string builder scope."
generated: true
guide: true
---

The reference page of [`strings.builder`](/reference/slots/strings/strings.builder/) has its arguments, constraints and declaration.

Creates a string builder scope. Every **[strings.builder.append]** invocation found inside it appends its value
to the builder, and when the scope ends the value of **[strings.builder]** becomes the concatenated text.
Its children are evaluated as a lambda object, and the slot has no arguments of its own.

```
strings.builder
   strings.builder.append:"howdy"
   strings.builder.append:" world"
get-value:x:@strings.builder
```

The above will result in the value of the last node being _"howdy world"_.
