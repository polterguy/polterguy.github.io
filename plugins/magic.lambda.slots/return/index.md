---
title: "How to use [return]"
description: "How to use [return] - This slot returns a value, or its child nodes, to the nearest caller, such as a dynamic slot being invoked with [signal]."
generated: true
guide: true
---

The reference page of [`return`](/reference/slots/core/return/) has its arguments, constraints and declaration.

This slot returns a value, or its child nodes, to the nearest caller, such as a dynamic slot being invoked with **[signal]**. It combines **[return-value]** and **[return-nodes]**, so you can give it a value, or children, as the two examples below show.

```
function:foo
   return:This is the returned value

signal:foo

function:bar
   return
      integer-value:int:57
      string-value:Foo bar

signal:bar
```
