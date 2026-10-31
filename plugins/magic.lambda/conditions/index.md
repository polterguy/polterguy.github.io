---
title: Comparison and boolean logic
description: The comparison slots [eq], [neq], [lt], [lte], [mt] and [mte], plus the boolean logical conditions [and], [or] and [not].
moved_anchors: {"how-to-use-and": "/plugins/magic.lambda/and/", "how-to-use-eq": "/plugins/magic.lambda/eq/", "how-to-use-lt": "/plugins/magic.lambda/lt/", "how-to-use-lte": "/plugins/magic.lambda/lte/", "how-to-use-mt": "/plugins/magic.lambda/mt/", "how-to-use-mte": "/plugins/magic.lambda/mte/", "how-to-use-neq": "/plugins/magic.lambda/neq/", "how-to-use-not": "/plugins/magic.lambda/not/", "how-to-use-or": "/plugins/magic.lambda/or/"}
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

* [`eq`](/plugins/magic.lambda/eq/) - [eq] is the equality "operator" in Magic, and it requires two arguments, both of which will be evaluated as potential signals - And the result of evaluating [eq] will only be true if the values of the
* [`neq`](/plugins/magic.lambda/neq/) - [neq] is the not equal "operator" in Magic, and it requires two arguments, both of which will be evaluated as potential signals - And the result of evaluating [neq] will only be true if the values of
* [`lt`](/plugins/magic.lambda/lt/) - [lt] will do a comparison between its two arguments, and only return true if its first argument is "less than" its second argument.
* [`lte`](/plugins/magic.lambda/lte/) - [lte] will do a comparison between its two arguments, and only return true if its first argument is "less than or equal" to its second argument.
* [`mt`](/plugins/magic.lambda/mt/) - [mt] will do a comparison between its two arguments, and only return true if its first argument is "more than" its second argument.
* [`mte`](/plugins/magic.lambda/mte/) - [mte] will do a comparison between its two arguments, and only return true if its first argument is "more than or equal" to its second argument.

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

* [`and`](/plugins/magic.lambda/and/) - [and] requires two or more arguments, and will only evaluate to true, if all of its arguments evaluates to true.
* [`or`](/plugins/magic.lambda/or/) - [or] is similar to [and], except it will evaluate to true if any of its arguments evaluates to true, such as the following illustrates.
* [`not`](/plugins/magic.lambda/not/) - [not] expects exactly one argument, and will negate its boolean value, whatever it is, such as the following illustrates.
