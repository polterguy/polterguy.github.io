---
title: "How to use [reference]"
description: "How to use [reference] - This slot will evaluate its expression, and add the entire node the expression is pointing to, as a referenced node into its value."
guide: true
slots: ["reference"]
---

The reference page of [`reference`](/reference/slots/core/reference/) has its arguments, constraints and declaration.

This slot will evaluate its expression, and add the entire node the expression is pointing to, as a referenced node into
its value. This allows you to pass a node _into_ a slot by reference, and have that slot modify the node itself, or
its children. This might sometimes be useful to have slots modify some original graph object, or parts of a graph -
Or get access to iterate over parts of your graph object's children.

```
.foo
reference:x:@.foo
set-value:x:-/#
   .:Yup!
```

You can think of this slot as the singular version of **[get-nodes]**, except instead of returning multiple
nodes, it assumes its expression only points to a single node, and instead of returning a copy of the node,
it returns the actual node by reference.

**Notice** - The `/#` iterator above, will enter into the node referenced as a value of its current
result - Implying it allows you to deeply traverse nodes passed in as references. This is sometimes
useful in combination with referenced nodes, passed in as values of other nodes. You should as a general
rule of thumb be careful with the **[reference]** slot, since it results in side effects for the caller if
it passes nodes by reference into some slot. Such side effects are as a general rule of thumb considered a _bad thing_,
since they result in unpredictable results. In theory passing in a node by reference to some slot, might change
the logic of the calling function, resulting in changing the code that is being executed, which obviously
makes the code literally impossible to understand. Hence, be careful with the **[reference]** slot!
