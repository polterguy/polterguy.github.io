---
title: "How to use [lambda2csv]"
description: "How to use [lambda2csv] - This slot converts the specified lambda object to a CSV string."
generated: true
guide: true
---

The reference page of [`lambda2csv`](/reference/slots/core/lambda2csv/) has its arguments, constraints and declaration.

This slot converts the specified lambda object to a CSV string. Below is an example of usage.

```
.data
   .
      name:Thomas Hansen
      age:int:47
   .
      name:John Doe
      age:int:67

lambda2csv:x:-/*
```

The slot will return type information as children of your **[lambda2csv]** invocation.
