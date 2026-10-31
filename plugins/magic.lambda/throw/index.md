---
title: "How to use [throw]"
description: "How to use [throw] - This slot simply throws an exception, with the exception message taken from its value."
guide: true
slots: ["throw"]
---

The reference page of [`throw`](/reference/slots/core/throw/) has its arguments, constraints and declaration.

This slot simply throws an exception, with the exception message taken from its value.
See the **[try]** slot above for an example. Notice, you can make the exception propagate to the client
by adding a **[public]** parameter, and set its value to boolean _"true"_ - At which point
the exception will be returned to the client, even in release builds, if no **[.catch]** block
handles it before it propagates to the client - Otherwise the exception
will only be visible in debug builds, and never returned to the client. You can also modify
the **[status]** HTTP return value that's returned to the client, to become e.g. 404,
indicating _"not found"_, etc. In addition you can pass in a **[field]** which will be serialised
back to the client if specified to help the client to semantically figure out which field
that triggered the exception. Below is an example of all of the above.

```
throw:Whatever error message here
   status:398
   public:true
   field:whatever-field
```

If you create an endpoint using for instance _"Hyper IDE"_, and throw the above exception, you can see
how this propagates to the client without the exception handler.
