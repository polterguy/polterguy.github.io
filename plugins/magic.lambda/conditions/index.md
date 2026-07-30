---
title: Comparison and boolean logic
description: The comparison slots [eq], [neq], [lt], [lte], [mt] and [mte], plus the boolean logical conditions [and], [or] and [not].
---

## Hyperlambda comparison

All comparison _"operators"_ works the same way in Hyperlambda, in that they have an LHS and a RHS, implying
respectively _"Left Hand Side"_ and _"Right Hand Side"_. However, since the _"comparison operators"_ in Hyperlambda
are slots themselves, this implies there is no _"left"_ or _"right"_ side in your comparison, implying the _"left"_
parts of your comparison is the first argument, and the _"right"_ side is the second argument. All comparison
slots will consider types, which implies that boolean true will _not_ be considered equal to the string value
of _"true"_, and the integer value of 5 is _not_ the same as the decimal value of 5.0, etc.

You can provide the two arguments to these slots either as children nodes, where the first child node becomes
the LHS part, and the second its RHS part - Or you can alternatively supply the LHS part as an expression
leading to a value, at which point the only child argument assumed for your comparison becomes the RHS argument.

### How to use [eq]

**[eq]** is the equality _"operator"_ in Magic, and it requires two arguments, both of which will be evaluated as potential
signals - And the result of evaluating **[eq]** will only be true if the values of these two arguments are _exactly the same_.

```
.src:int:5
eq
   get-value:x:@.src
   .:int:5
```

### How to use [neq]

**[neq]** is the _not_ equal _"operator"_ in Magic, and it requires two arguments, both of which will be evaluated as potential
signals - And the result of evaluating **[neq]** will only be true if the values of these two arguments are _not the same_.

```
.src:int:5
neq
   get-value:x:@.src
   .:int:5
```

### How to use [lt]

**[lt]** will do a comparison between its two arguments, and only return true if its first argument is _"less than"_
its second argument. Consider the following.

```
.src1:int:4
lt
   get-value:x:@.src1
   .:int:5
```

### How to use [lte]

**[lte]** will do a comparison between its two arguments, and only return true if its first argument is _"less than or equal"_
to its second argument. Consider the following.

```
.src1:int:4
lte
   get-value:x:@.src1
   .:int:4
```

### How to use [mt]

**[mt]** will do a comparison between its two arguments, and only return true if its first argument is _"more than"_
its second argument. Consider the following.

```
.src1:int:7
mt
   get-value:x:@.src1
   .:int:5
```

### How to use [mte]

**[mte]** will do a comparison between its two arguments, and only return true if its first argument is _"more than or equal"_
to its second argument. Consider the following.

```
.src1:int:7
mte
   get-value:x:@.src1
   .:int:5
```

### Commonalities for all Hyperlambda comparison slots

All comparison slots can optionally be given an expression that will be assumed to be their LHS argument,
or _"Left Hand Side"_ argument, that if given will replace the first child argument. Below is an example for
the **[mte]** slot, but all comparison slots works similarly.

```
.src1:int:7
mte:x:@.src1
   .:int:5
```

In the above example the expression `:x:@.src1` becomes the left hand side, while the child argument becomes the right hand
side of the comparison. To translate the above into how it might look like in a traditional programming language to
give you an idea of its structure please consider the following.

```
src1 >= 5
```

Due to that the **[if]** slot, the **[else-if]** slot, and the **[while]** slot can optionally be given slot
invocations themselves as their conditions, and all comparison slots are slots - You can inject comparison slot
invocations inside of for instance your **[if]** invocations, serving as the slot invocation declaring the condition
for your **[if]**. Consider the following to understand this.

```
.result
.arg1:foo

if
   eq:x:@.arg1
      .:foo
   .lambda
      set-value:x:@.result
         .:Yup!
```

The above is the equivalent of the following in a more traditional programming language.

```
string result;
var arg1 = "foo";

if (arg1 == "foo")
{
   result = "Yup!";
}
```

## Boolean logical conditions

### How to use [and]

**[and]** requires two or more arguments, and will only evaluate to true, if all of its arguments evaluates to true. Consider
the following.

```
// Evaluates to false.
and
   .:bool:true
   .:bool:false

// Evaluates to true.
and
   .:bool:true
   .:bool:true
```

Notice, **[and]** will short circuit itself if it reaches a condition that does _not_ evaluate to true, implying
none of its conditions afterwards will be considered, since the **[and]** as a whole evaluates to false.
**[and]** will also evaluate its arguments before checking if they evaluate to true, allowing you
to use it as a part of richer comparison trees, such as the following illustrates.

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

### How to use [or]

**[or]** is similar to **[and]**, except it will evaluate to true if _any_ of its arguments evaluates to true, such
as the following illustrates. **[or]** will also evaluate its arguments, allowing you to use it as a part of richer comparison
trees, the same way **[and]** allows you to. Below is a simple example.

```
// Evaluates to false.
or
   .:bool:false
   .:bool:false

// Evaluates to true.
or
   .:bool:false
   .:bool:true
```

**[or]** will also short circuit itself if it reaches a condition that evaluates to true, implying
none of its conditions afterwards will be considered, since the **[or]** as a whole evaluates to true
if _any_ of its arguments evaluates to true.

### How to use [not]

**[not]** expects _exactly one argument_, and will negate its boolean value, whatever it is, such as the following illustrates.

```
not
   .:bool:true

not
   .:bool:false
```

**[not]** will also evaluate its argument, allowing you to use it in richer comparison trees, the same you could do
with both **[or]** and **[and]**. Below is an example combining these slots together to create more complex types
of logical comparisons.

```
.foo1:bar
.foo2:bool:false
.foo3:bool:true
.result

if
   and
      eq:x:@.foo1
         .:bar
      or
         get-value:x:@.foo2
         get-value:x:@.foo3
   .lambda

      set-value:x:@.result
         .:Yup!
```

Notice you can actually follow the path the Hyperlambda executor took during execution of your code if you use the
_"Eval"_ menu item, since the result it produces for the above code will resemble the following.

```
.foo1:bar
.foo2:bool:false
.foo3:bool:true
.result:Yup!
if:bool:true
   and:bool:true
      eq:bool:true
         .:bar
      or:bool:true
         get-value:bool:false
         get-value:bool:true
   .lambda
      set-value:x:@.result
         .:Yup!
```

In the above code we can see that the first child of our above **[or]** node evaluates to `false`, but since the
second child of our **[or]** node evaluates to true, the **[or]** as a whole evaluates to `true`. If you change
its **[.foo2]** data node to boolean `true`, you will see that your second child of **[or]** never even is
considered, since your **[or]** invocation is _"short circuiting"_. You can nest as many **[or]** and **[and]**
invocations as you wish, creating any amount of complexity in your Hyperlambda.
