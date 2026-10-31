---
title: "How to use [transformers.hash-password]"
description: "How to use [transformers.hash-password] - This slot is a \"transformer\" and typically used for input payloads originating from HTTP invocations, such as when creating a new user, etc."
guide: true
slots: ["transformers.hash-password"]
---

This slot is a _"transformer"_ and typically used for input payloads originating from HTTP invocations,
such as when creating a new user, etc. The following Hyperlambda illustrates its usage.

```
.arguments
   password:foo
eval:x:+
signal:transformers.hash-password
   reference:x:@.arguments/*/password
```

The idea of the slot is that it transforms in place the specified argument by reference. Implying executing
the above Hyperlambda will result in something resembling the following.

```
.arguments
   password:$2b$10$ZjOhP3DecbgqYsTKknvLmODs1H1C6bfCheBug6iTk5TNmEckE9H3e
```

This makes it perfect for _"transforming"_ input payloads containing passwords before persisting these into
your database.
