---
title: "How to use [validators.default]"
description: "How to use [validators.default] - This validator takes one or more arguments with any name and any value, and if this node does not exist as a child of the node collection specified as its expression value, it appends..."
generated: true
guide: true
---

This is the guide to [`validators.default`](/reference/slots/validators/validators.default/), whose reference page has its arguments, constraints and declaration.

This validator takes one or more arguments with any name and any value, and if this node does not exist as
a child of the node collection specified as its expression value, it appends the node to it.
If the node exists but has a null value, it sets its value to the value of the argument.


```
.arguments
validators.default:x:@.arguments
   foo1:bar1
```
