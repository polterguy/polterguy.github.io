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
...
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
and the **\[math.increment\]** invocation increases the value of the **\[.no\]** node inside of the while loop by 1.
**\[lt\]** implies _"less than"_ and there are many similar types of conditions in Hyperlambda, which you can
read up about [here](/documentation/magic.lambda/). If you want to read more about math slots in Hyperlambda, such
the the above **[math.increment]** slot, you can find it [here](/documentation/magic.lambda.math/).

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

## Branching commonalities

The **[while]**, **[if]**, **[else-if]** and **[else]** slots are what is commonly referred to as _"conditional branching"_.
Branching implies your code takes a different execution path as it executes, and conditional branching implies there
are conditions associated with these alternative execution paths. All of the branching slots in Hyperlambda have similar
semantics, implying taking a condition as an argument. All branching slots except the **[else]** slot, requires
_exactly one child node_, or argument - Which is the condition associated with their lambda object. In addition each
of these slots also requires exactly one **[.lambda]** argument, being the code to execute if their condition is _true_.
Logically this becomes the equivalent of the following in plain English.

> If some-condition, then do this

Where _"some-condition"_ is your condition, and _"this"_ is your lambda object. If the condition is _not_ true, their
associated lambda object will _not_ execute. The **[else]** node on the other hand only executes its lambda object if
all **[if]** and **[else-if]** invocations before it returned _false_. You can add any slot invocation to such branching
slots as your conditions. Below is an example of using a custom slot returning true instead of the comparison slots.

```
slots.create:foo-bar
   return:bool:true

.result

if
   signal:foo-bar
   .lambda

      set-value:x:@.result
         .:Yup!

else

   set-value:x:@.result
      .:Nope!
```

The [magic.lambda](/documentation/magic.lambda/) project also contains logical slots, such as **[or]** and **[and]**
that only yields true if _either_ of their list of conditions returns true, or _all_ of their conditions returns
true, respectively. This gives you the same capabilities as the following pseudo code in for instance C# would
give you.

```csharp
if (x && y) {
   do_something();
}
```

However, the syntax in Hyperlambda might be a bit different compared to what you are used to, since the above
would look like the following in Hyperlambda.

```
if
   and
      x
      y
   .lambda
      do_something
```

Notice how the **[and]** part is the outermost invocation, and not separating your conditions as it would in
a more traditional programming language. The same is true for **[or]**. This has the advantage of allowing you
to create your own logical operators, which might be useful sometimes, to create your own domain specific _"keywords"_
in C# related to your particular problem at hand. Below is a  working Hyperlambda example illustrating this concept.

```
.s1:bool:true
.s2:bool:true
.res
if
   and
      get-value:x:@.s1
      get-value:x:@.s2
   .lambda
      set-value:x:@.res
         .:OK
```

* [Continue with Authentication and Authorisation](/tutorials/auth/)
