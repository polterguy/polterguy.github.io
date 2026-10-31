---
title: "How to use [set-value]"
description: "How to use [set-value] - Changes the value of all nodes referenced as its main expression to whatever its single source happens to be."
guide: true
slots: ["set-value"]
---

The reference page of [`set-value`](/reference/slots/core/set-value/) has its arguments, constraints and declaration.

Changes the value of all nodes referenced as its main expression to whatever its single source happens to be.
Notice, when you invoke a slot that tries to change the value, name, or the node itself of some expression,
and you supply a source expression to your invocation - Then the result of the source expression
_cannot_ return more than one result. The destination expression however can modify multiple nodes
simultaneously.

```
.foo
.foo
set-value:x:../*/.foo
   .:SUCCESS
```
