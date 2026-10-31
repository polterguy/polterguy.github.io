---
title: "How to use [neq]"
description: "How to use [neq] - [neq] is the not equal \"operator\" in Magic, and it requires two arguments, both of which will be evaluated as potential signals - And the result of evaluating [neq] will only be true if the values of"
guide: true
slots: ["neq"]
---

The reference page of [`neq`](/reference/slots/core/neq/) has its arguments, constraints and declaration.

**[neq]** is the _not_ equal _"operator"_ in Magic, and it requires two arguments, both of which will be evaluated as potential
signals - And the result of evaluating **[neq]** will only be true if the values of these two arguments are _not the same_.

```
.src:int:5
neq
   get-value:x:@.src
   .:int:5
```
