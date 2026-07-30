---
title: Modifying your lambda object
description: The slots that read and modify your Hyperlambda graph object; [add], [insert-before], [set-value], [unwrap], [get-value], [exists], [reference] and more.
---

## Modifying your Hyperlambda graph object

Since there are no explicit variables in Hyperlambda, yet all nodes potentially might change, this requires
the ability to change your nodes as you execute your Hyperlambda. Magic provides many slots to achieve this,
both to change the names, values, and types of your nodes - In addition to adding a range of nodes into some
other node, and/or remove nodes from the children collection of your nodes.

### How to use [add]

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

### How to use [insert-before]

This slot works the exact same way as the **[add]** node, except it will insert the nodes _before_ the
node(s) referenced in its main/destination argument.

```
.foo
   foo1
   foo2
insert-before:x:@.foo/*/foo1
   .
      inserted
```

### How to use [insert-after]

This slot works the exact same way as the **[add]** and **[insert-before]** slots, except it will insert the
nodes _after_ the node(s) referenced in its main/destination argument.

```
.foo
   foo1
   foo2
insert-after:x:@.foo/*/foo1
   .
      inserted
```

### How to use [remove-nodes]

This slot will remove all nodes its expression is pointing to.

```
.data
   foo1
   foo2
   foo3
remove-nodes:x:@.data/*/foo2
```

### How to use [include]

This slot is logically the combination of a **[for-each]**, **[add]** and **[eval/invoke]**. The slot takes a lambda
object, that will be executed with a **[.dp]** node, for each node resulting from evaluating its expression passed
in by reference. The returned nodes will then be appended into the currently iterated node, allowing you to _"include"_
sub trees into a destination tree using a declarative syntax. It is useful for adding nodes dynamically to an existing
graph object, declaratively, according to the state of its destination nodes.

```
.data
   foo1:bar1
   foo2:bar2
   foo3:bar3
include:x:@.data/*
   strings.concat
      get-value:x:@.dp/#
      .:" howdy"
   unwrap:x:+/*
   return
      howdy:x:@strings.concat
```

### How to use [filter]

Filter allows you to filter using a predicate. If the predicate returns true for the currently iterated list item, it's included, otherwise not. Below is an example.

```
.src
   .:int:1
   .:int:2
   .:int:3
   .:int:4
filter:x:@.src/*
   mt
      get-value:x:@.dp/#
      .:int:2
   return:x:-
```

The above will return only nodes having a value above integer value _"2"_.

### How to use [set-value]

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

### How to use [set-name]

Changes the name of all nodes referenced as its main expression to whatever its single source happens to be.

```
.foo
   old-name
set-name:x:@.foo/*
   .:new-name
```

The **[set-name]** invocation can also be given multiple destinations, but only _one_ source.

### How to use [unwrap]

This slot is useful if you want to evaluate some expression before the node where it's referenced is reached.
Imagine the following.

```
.src:Hello World
unwrap:x:+
.dest:x:@.src
```

In the above example, before the **[.dest]** node is reached by the Hyperlambda instruction pointer, the value
of the **[.dest]** node will have been _"unwrapped"_ (evaluated), and its value will be _"Hello World"_.
This slot becomes very handy when you invoke lambda objects with expressions, since
it allows you to _"forward evaluate"_ said expressions inside your lambda object, _before_ the lambda object
is actually executed.

The **[unwrap]** slot can also optionally be supplied with a **[apply-lists]** argument as boolean true. By default the **[unwrap]** slot will throw an exception if you unwrap a node leading to multiple nodes. If you apply lists, it will instead add all the source nodes as destination nodes into the unwrapped node. Consider the following.

```
.src
   foo1:bar1
   foo2:bar2
unwrap:x:+
   apply-lists:bool:true
.dest:x:@.src/*
```

If you remove the above **[apply-lists]** argument or set its value to false, the above code will throw an exception. If you keep the above **[apply-lists]** argument as is it will result in the following.

```
.src
   foo1:bar1
   foo2:bar2
unwrap:x:+
   apply-lists:bool:true
.dest
   foo1:bar1
   foo2:bar2
```

### How to use [get-value]

Returns the value of the node its expression is pointing to.

```
.data:Hello World
get-value:x:-
```

### How to use [get-name]

Returns the name of the node referenced in its expression.

```
.foo
get-name:x:-
```

### How to use [get-count]

This slot returns the number of nodes its expression is pointing to.

```
.data
   foo1
   foo2
get-count:x:@.data/*
```

### How to use [get-nodes]

Returns the nodes its expression is referencing.

```
.data
   foo1
   foo2
get-nodes:x:-/*
```

### How to use [exists]

**[exists]** will evaluate to true if its specified expression yields one or more results. If not, it will
return false.

```
.src1
   foo
.src2
exists:x:@.src1/*
exists:x:@.src2/*
```

### How to use [not-exists]

**[not-exists]** will evaluate to true if its specified expression yields zero results. If not, it will
return false. It's the logical opposite of **[exists]**.

```
.src1
   foo
.src2
not-exists:x:@.src1/*
not-exists:x:@.src2/*
```

### How to use [null]

**[null]** will evaluate to true if its specified expression yields null, or the expression returns no nodes.
If not, it will return false.

```
.src1
   foo:foo
.src2
   foo
null:x:@.src1/*
null:x:@.src2/*
```

### How to use [not-null]

**[not-null]** will evaluate to true if its specified expression returns nodes and at least one of those nodes has a value.
If not, it will return false.

```
.src1
   foo:foo
.src2
   foo
.src3
not-null:x:@.src1/*
not-null:x:@.src2/*
not-null:x:@.src3/*
```

### How to use [reference]

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

### How to use [get-first-value]

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

### How to use [get-context]

This slot returns a context stack object, which is an object added to the stack using **[context]**.
Below is an example of usage.

```
.result
context:foo
   value:bar
   .lambda

      set-value:x:@.result
         get-context:foo
```

Notice how **[get-context]** inside your above **[.lambda]** invocation is able to retrieve the context object
named _"foo"_, having the value of _"bar"_. See the **[context]** slot further down in this document for
details about how this works.
