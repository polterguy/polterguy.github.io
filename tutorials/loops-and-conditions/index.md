---
title: Loops and branching in Hyperlambda
description: In this article you will learn how to loop and apply conditional branching in Hyperlambda.
---

# Loops and branching in Hyperlambda

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Looping using __\[for-each\]__ and __\[while\]__
* How conditional branching works in Hyperlambda, such as __\[if\]__, __\[else-if\]__ and __\[else\]__

## Looping in Hyperlambda

There are two primary slots in Hyperlambda that allows you to loop. These are as follows.

* __[for-each]__
* __[while]__

The **[for-each]** slot loops once for each result returned by its expression. Below is an example.

```
.data
   foo1:bar1
   foo2:bar2
   foo3:bar3

for-each:x:@.data/*

   set-value:x:@.dp/#
      .:Loop was here
```

If you execute the above in Magic's _"Eval"_ component you will see how the above code results in the following.

```
.data
   foo1:Loop was here
   foo2:Loop was here
   foo3:Loop was here
```

This is because the lambda object of the **[for-each]** slot is executed once for each node resulting from its
expression, passing in the currently iterated node as its **[.dp]** node by _reference_, which is why we have to use the
funny syntax of `/#` to de-reference the actual node we're iterating over. The **\[for-each\]** loop is useful when
you have a node set to iterate over, but sometimes you need another mechanism, such as illustrated below.

```
.no:int:0
.data

while
   lt
      get-value:x:@.no
      .:int:10
   .lambda

      add:x:@.data
         .
            foo:bar
      math.increment:x:@.no
```

The above will iterate 10 times because this is a part of the condition to the **\[while\]** invocation, due
to the **\[lt\]** node only executing the **\[.lambda\]** object as long as the **\[.no\]** node is less than 10,
and the **\[math.increment\]** invocation increases the value of the **\[.no\]** node inside of the while loop.
**\[lt\]** implies _"less than"_ and there are many similar types of conditions in Hyperlambda, which you can
read up about [here](/documentation/magic.lambda/).

## Branching in Hyperlambda

The **\[if\]** slot works almost exactly the same way the **\[while\]** slot works, except it only executes its
lambda objects _once_. Below is an example.

```
.foo:bar
.result

if
   eq
      get-value:x:@.foo
      .:bar
   .lambda

      set-value:x:@.result
         .:Yup!
```

**\[eq\]** in the above Hyperlambda implies _"equals"_, and only returns true if its two children arguments are
equal to each other. Hyperlambda also provides **\[else-if\]** and **\[else\]** slots. Below is an example.

```
.foo:bar
.result

if
   eq
      get-value:x:@.foo
      .:foo
   .lambda

      set-value:x:@.result
         .:Foo was here

else-if
   eq
      get-value:x:@.foo
      .:bar
   .lambda

      set-value:x:@.result
         .:Bar was here

else

   set-value:x:@.result
      .:Nobody was here
```

Notice the difference between the semantics of the **\[else\]** and its related slots, not needing an explicit
**[.lambda]** node. This is because the **[else]** slot cannot be given any arguments, except of course its
lambda object, so there are no reasons to explicitly add a **[.lambda]** node to it to declare its lambda object.

Try playing with the above **[.foo]** node's value, and see how the **[.result]** node changes depending upon what value
you provide. The below C# example is the equivalent of the above code in a more traditional programming language.

```csharp
var foo = "foo";
var result = null;

if (foo == "foo") {

   result = "Foo was here";

} else if (foo == "bar") {

   result = "Bar was here";

} else {

   result = "Nobody was here";

}
```

Hyperlambda also have slots for **[switch]**, **[or]** and **[and]**, in addition to other mechanisms for branching.
Refer to the [magic.lambda](/documentation/magic.lambda/) project for an exhaustive list.

* [Continue with Authentication and Authorisation](/tutorials/auth/)
