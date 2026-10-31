---
title: "How to use [set-name]"
description: "How to use [set-name] - Changes the name of all nodes referenced as its main expression to whatever its single source happens to be."
guide: true
slots: ["set-name"]
---

The reference page of [`set-name`](/reference/slots/core/set-name/) has its arguments, constraints and declaration.

Changes the name of all nodes referenced as its main expression to whatever its single source happens to be.

```
.foo
   old-name
set-name:x:@.foo/*
   .:new-name
```

The **[set-name]** invocation can also be given multiple destinations, but only _one_ source.
