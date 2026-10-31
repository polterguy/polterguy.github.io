---
title: "How to use [get-context]"
description: "How to use [get-context] - This slot returns a context stack object, which is an object added to the stack using [context]."
guide: true
slots: ["get-context"]
---

The reference page of [`get-context`](/reference/slots/core/get-context/) has its arguments, constraints and declaration.

This slot returns a context stack object, which is an object added to the stack using **[context]**.
Below is an example of usage.

```
.result
context:foo
   value:bar
   .lambda

      set-value:x:@.result
         get-context:foo
```

Notice how **[get-context]** inside your above **[.lambda]** invocation is able to retrieve the context object
named _"foo"_, having the value of _"bar"_. See the **[context]** slot further down in this document for
details about how this works.
