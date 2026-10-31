---
title: "How to use [add]"
description: "How to use [add] - This slot allows you to dynamically add nodes into a destination node."
guide: true
slots: ["add"]
---

The reference page of [`add`](/reference/slots/core/add/) has its arguments, constraints and declaration.

This slot allows you to dynamically add nodes into a destination node. Its primary argument is the destination,
and it assumes that each children is a collection of nodes it should append to the destination node's children
collection. The reasons for this additional level of indirection, is because the **[add]** slot might have
children that are by themselves slot invocations, which it will evaluate before it starts adding the children
nodes of these arguments to its destination node's children collection. Below is an example.

```
.dest
add:x:@.dest
   .
      foo1:howdy
      foo2:world
   .
      bar1:hello
      bar2:world
```

Notice how all the 4 nodes above (foo1, foo2, bar1, bar2) are appended into the **[.dest]** node's children
collection. This construct allows you to evaluate slots and add the result of your slot invocations into the destination,
such as the following illustrates.

```
.src
   foo1:foo
   foo2:bar
.dest
add:x:@.dest
   get-nodes:x:@.src/*
```

**[add]** can also take an expression leading to multiple destinations as its main argument, allowing you to
add a copy of your source nodes into multiple destination node collections simultaneously with one invocation. **[add]**
can also be given multiple _"source"_ node invocations. In the following example we illustrate both of these
constructs at the same time.

```
.dest
.dest
.src1
   foo1:bar1
.src2
   foo2:bar2
add:x:../*/.dest
   get-nodes:x:@.src1/*
   get-nodes:x:@.src2/*
```

Notice how _both_ of our **[.dest]** nodes above ends up having _both_ the **[foo1]** and the **[foo2]** nodes in
its children collection after executing the above Hyperlambda.
