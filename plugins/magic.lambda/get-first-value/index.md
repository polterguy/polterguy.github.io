---
title: "How to use [get-first-value]"
description: "How to use [get-first-value] - Returns the first non-null value resulting from evaluating its expression, and/or its children nodes."
guide: true
slots: ["get-first-value"]
---

The reference page of [`get-first-value`](/reference/slots/core/get-first-value/) has its arguments, constraints and declaration.

Returns the _first_ non-null value resulting from evaluating its expression, and/or its children nodes.

```
.data1
   foo1:bar1
   foo2:bar2
.data2:bar3
get-first-value:x:@.data1/*
   get-value:x:@.data2
```

This node returns only the first non-null value resulting from evaluating its expression, and/or its children
nodes. This is useful when you for instance have arguments to some lambda object, but want to apply default
values if the argument is not specified - And or want to have guarantees of that only a single value is returned.
