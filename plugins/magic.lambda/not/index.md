---
title: "How to use [not]"
description: "How to use [not] - [not] expects exactly one argument, and will negate its boolean value, whatever it is, such as the following illustrates."
guide: true
slots: ["not"]
---

The reference page of [`not`](/reference/slots/core/not/) has its arguments, constraints and declaration.

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
