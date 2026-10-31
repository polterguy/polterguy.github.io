---
title: "How to use [invoke]"
description: "How to use [invoke] - This slot works similarly to [eval], except it treats the invocation similarly to an invocation to a dynamic slot, allowing you to pass in arguments, and return nodes from the invocation."
generated: true
guide: true
---

The reference page of [`invoke`](/reference/slots/core/invoke/) has its arguments, constraints and declaration.

This slot works similarly to **[eval]**, except it treats the invocation similarly to an invocation to
a dynamic slot, allowing you to pass in arguments, and return nodes from the invocation.

```
.lambda
   strings.concat
      .:"Hello "
      get-value:x:@.arguments/*/name
   return:x:-
invoke:x:@.lambda
   name:John
```

Notice, you cannot supply an expression leading to multiple nodes, and the slot invokes the lambda
object immutable, such that it doesn't change. The invocation also does _not_ have access to anything
outside of its own lambda object.
