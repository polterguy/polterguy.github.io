# Real programming with Hyperlambda

So far what we have done, have probably felt more like _"configuring"_ than
programming. In this article, we will take the step into the Turing complete
parts of Hyperlambda, and create some real code, with branching, loops, and
everything you normally associate with a _"real programming language"_.
Create a file in your _"/modules/tutorials/"_ folder, and give it the
name _"branching.get.hl"_. Put the following code into it.

```
.arguments
   condition:bool
if
   get-value:x:@.arguments/*/condition
   .lambda
      return
         result:Yup, it's true!
else
   return
      result:Nope! It's false!
```

Then go to your endpoints and invoke your newly created endpoint,
passing in a query parameter named _"condition"_ and set its
value to _"false"_. As you do, you'll end up with a result resembling
the following.

```json
{
   "result": "Nope! It's false!"
}
```

Change the query parameter's value to _"true"_, invoke your endpoint
again, and see how it returns a different result this time. Hence,
obviously Hyperlambda allows you to create branching code. With
branching, we imply code that is conditionally executed, depending
upon arguments given to your code.

**Notice** - Hyperlambda _is_ first and foremost an orchastration
programming language. This implies that some things are much easier
to achieve, typically _"orhastration code"_ - While
other things are more difficult to achieve, which includes branching,
looping, and more traditional programming constructs. Sometimes
you still want to use Hyperlambda for such code, due to
needing a more dynamic environment than what C# gives you. However,
have this in mind as you go through the examples here. Implying,
some things here are probably more cumbersome to achieve in Hyperlambda
than its C# equivalent.

## Explanation of above code

What the above Hyperlambda example does, is to conditionally
execute one of two different lambda objects, depending upon
the value of the given _"condition"_ argument. Basically, if
the argument is true it executes the parts that returns _"Yup, it's true!"_,
otherwise it returns the parts that returns _"Nope! It's false!"_.

This is traditionally referred to as _"branching"_ in programming,
and is something most developers would be acquainted with. Hyperlambda
has its differences though in these regards, among other things
due to that everything is a _"lambda"_ object in Hyperlambda.
This implies that all potential branches are individually evaluated,
as you can see in the above example. To understand this process,
consider the following pseudo code.

```
if
   .bool:some-condition
   .lambda

      /*
       * If condition is true, execute this lambda.
       */

else

   /*
    * If not, execute this lambda object
    */
```

The first argument to your **[if]** is basically anything able
to return a boolean value somehow, and it can be anything,
including slot invocations - While the second argument, the **[.lambda]**,
is simply the block of lambda to execute if the condition yields
true. The **[else]** however, doesn't require a condition to
evaluate, since it'll only be executed if all previous **[if]**
and **[else-if]** invocations didn't evaluate their condition(s)
to true - Hence, it just includes the lambda object which it
executes if it should be executed directly as children, beneath
the else node itself.

Yet again, everything is a lambda block in
Hyperlambda - Hence, thinking of only **[.lambda]** blocks
as being lambda, is not productive. Even the **[if]** node
itself is evaluated using **[eval]**, which is why we can reference
slots as conditions, and also why **[.lambda]** starts with a `.`,
such that it won't be evaluated or attempted to be signaled as a
slot invocation.

## Boolean "operators"

Hyperlambda doesn't contain the construct of _"operators"_. Hence,
what you'd normally refer to in a traditional programming language
as boolean operators, is rather in fact slots by themselves in
Hyperlambda. Let's illustrate with an example.

```
.arguments
   condition1:bool
   condition2:bool
if
   and
      get-value:x:@.arguments/*/condition1
      get-value:x:@.arguments/*/condition2
   .lambda
      return
         result:Yup, both conditions are true
else
   return
      result:Both conditions are not true!
```

Notice how the **[and]** node above becomes a lambda
object in itself, sequentially invoking its children,
until all children have evaluated, and yielded true -
_Or_ one of its children evaluates to false, at which it
short circuits, and stops further evaluation of its
children nodes. Only of _all_ children conditions
evaluates to _"true"_, the **[and]** evaluates to _"true"_.

If you exchange the above **[and]** with an **[or]**, it
will stop evaluating its children, once it has found its first
_"true"_ condition, and the **[or]** as a whole yields _"true"_.

Hence, short circuiting in Hyperlambda is logically
similar to how it's implemented in traditional programming
languages. Bot **[or]** and **[and]** can have as many
children conditions as you wish, and you can also nest
logical slots, and add inner boolean logical slots,
effectively resulting in the same as you'd achieve using
paranthesis in traditional programming languages. Below
is an example.

```
.arguments
   condition1:bool
   condition2:bool
   condition3:bool
   condition4:bool
if
   or
      and
         get-value:x:@.arguments/*/condition1
         get-value:x:@.arguments/*/condition2
      and
         get-value:x:@.arguments/*/condition3
         get-value:x:@.arguments/*/condition4
   .lambda
      return
         result:Condition 1+2 or 3+4 are true
else
   return
      result:Neither condition 1+2 nor 3+4 are true
```

The above **[if]** will only evaluate to true if both 1+2 is true,
or 3+4 is true. If 1+3 is true, and all others are false, the
**[if]** will evaluate to false. This becomes the equivalent
of the following more traditional programming construct.

```csharp
if ((condition1 && condition2) || (condition3 && condition4)) {
   /* ... Do stuff! ... */
}
```

Hence, although Hyperlambda _is_ a bit _"verbose"_ in these
regards, there's nothing preventing you from creating just
as complex conditions in Hyperlambda, as you could create in
any other programming language.

**Notice** - the **[while]** slot functions exactly the
same is the **[if]** slot, except of course it will execute
over and over again, until the condition for some reasons
yields _"false"_.

## Looping

Since **[while]** is semantically the _exact same_ as
**[if]**, we will focus on the **[for-each]** loop here,
which allows you to iterate once for every node found through
some expression. Try executing the following in your _"Evaluator"_.

```
.data
   foo1:bar1
   foo2:bar2
   foo3:bar3
.result:
for-each:x:@.data/*
   set-value:x:@.result
      strings.concat
         get-value:x:@.result
         get-value:x:@.dp/#
```

The above will iterate once for each node beneath **[.data]**,
and append the value of the currently iterated node, into
the **[.result]** node.

### The reference iterator

At this point the reference iterator becomes crucial to understand.
The **[for-each]** slot, will execute once for each resulting
onde in its expression - And as it does, it will _"inject"_
the currently iterated node _by reference_ into its own
lambda object. the name of this _"data pointer"_ argument,
becomes **[.dp]**. Hence, by using the reference iteratr `#`,
we're able to extract a _direct reference_ to the node we're
iterating.

Normally when you're handling nodes in Hyperlambda, you're
working on a _copy_ of the node. For reference nodes, containing
other nodes by reference as their values, this is _not_ true -
And you're actually working on the node you're iterating
directly, and not a copy of it. To understand this, try executing
the following Hyperlambda, and watch how the **[fooX]** nodes are
changing their values after execution.

```
.data
   foo1:bar1
   foo2:bar2
   foo3:bar3
.result:
for-each:x:@.data/*
   set-value:x:@.dp/#
      .:Thomas Hansen was here!
```

The whole point being that after execution, the **[.data]**
node will resemble the following.

```
.data
   foo1:Thomas Hansen was here!
   foo2:Thomas Hansen was here!
   foo3:Thomas Hansen was here!
```

## Changing your tree

Since Hyperlambda doesn't really contain the notion of variables,
we'll need a different mechanism to change nodes, values and names
of nodes. This is done by using the following slots.

* __[set-value]__ - Changes the value(s) of nodes
* __[set-name]__ - Changes the name(s) of nodes
* __[add]__ - Appends a list of nodes into some destination
* __[insert-before]__ - Insert a bunch of nodes _after_ its destination(s)
* __[insert-after]__ - Insert a bunch of nodes _before_ its destination(s)
* __[remove-nodes]__ - Removes the nodes specified by its source expression
* __[unwrap]__ - Forward evaluates expressions found in other nodes

Some Hyperlambda illustrating usage of these can be found below.

```
.foo1:howdy
.foo2:world
.foo3
set-value:x:@.foo1
   .:Thomas was here
set-name:x:@.foo2
   .:Thomas was here too
add:x:@.foo3
   .
      item2:howdy
      item2:world
```

These slots are fairly self explanatory, but you can refer to the
[reference documentation for Magic lambda](/documentation/magic.lambda)
if you want to see what you can do with these slots.

One important detail here, is that _all_ of these slots takes the _destination_
as their main argument, implying the expression value of their invocation node.
While those requiring a source argument, normally acceps this as a child
node to their invocation node. Some of these slots, such as **[add]**, **[insert-xx]**,
can handle multiple sources - While others will throw exceptions
if you have an expression leading to multiple sources, such as the **[set-xx]** nodes.

## Custom dynamic slots

You can also create dynamic slots in Hyperlambda. Think _"your own functions"_
to understand its purpose. These basically becomes key/lambda dictionary
lookups, allowing you to invoke them dynamically, as
if they were pure C# slots. Below is an example.

```
slots.create:foo.bar
   return:bool:true
```

the above creates a slot that simply returns the boolean value of _"true"_,
but you can put any amount of Hyperlambda into your slots - And due to
the functional aspect of Hyperlambda, you can use these slots as
if they were normal C# slots. An example of invoking the
above slot can be found below, where we combine it with
conditional execution.

```
if
   signal:foo.bar
   .lambda
      return
         result:Dynamic slot returned true
else
   return
      result:Dynamic slot did not return true
```

Of course, if you try to execute the above Hyperlambda, without first having
created your **[foo.bar]** slot, an exception will be thrown, due to
trying to invoke a slot that doesn't exist.

Dynamic slots can also contain async slot invocations, but if
they do, you'll have to invoke them using the async invocation slot,
that's called **[wait.signal]**. Notice also the subtle difference in
how we invoke a dynamically created slot, by explicitly invoking
it through **[signal]**, instead of directly adding it as a node
name. This is to avoid trying to reference the slot as a C# slot,
and also helps you separate dynamically created slots, from static
C# slots. And in fact, all manipulation of dynamic slots, are slightly
different than statically compiled C# slots. For instance, the invocation
pattern of dynamic slots, doesn't allow us to pass in a _value_ to
our slot invocations, and only childrne arguments can be passed in.

A dynamic slot can however _return_ a value, as we saw above,
at which point the value will become the value of the **[signal]**
node after invocation.

* [Documentation](/documentation)
