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
to achieve, typically _"orchestration code"_ - While
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
and **[else-if]** invocations didn't evaluate
to true - Hence, it just includes its lambda object directly as
children, beneath the else node itself.

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
_Or_ one of its children evaluates to false, at which point it
short circuits, and stops further evaluation of its
children nodes. Only if _all_ children conditions
evaluates to _"true"_, the **[and]** evaluates to _"true"_.

If you exchange the above **[and]** with an **[or]**, it
will stop evaluating its children, once it has found its first
_"true"_ condition, and the **[or]** as a whole yields _"true"_.

Hence, short circuiting in Hyperlambda is logically
similar to how it's implemented in traditional programming
languages. Both **[or]** and **[and]** can have as many
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
or both 3+4 is true. If 1+3 is true, and all others are false, the
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
node in its expression - And as it does, it will _"inject"_
the currently iterated node _by reference_ into its own
lambda object. The name of this _"data pointer"_ argument,
becomes **[.dp]**. Hence, by using the reference iterator `#`
on the **[.dp]** node, we're able to extract a _direct reference_
to the node we're currently iterating.

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
we'll need a different mechanism to change nodes, values, and names
of nodes. This is done by using the following slots.

* __[set-value]__ - Changes the value(s) of nodes
* __[set-name]__ - Changes the name(s) of nodes
* __[add]__ - Appends a list of nodes into your destination(s)
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
node to their invocation node. Some of these slots, such as **[add]** and **[insert-xx]**,
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

The above creates a slot that simply returns the boolean value of _"true"_,
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
that's called **[wait.signal]** - At which point you'd probably want
to prefix your slot's name with **[wait.]** to communicate this
to any users of your slot.

Notice also the subtle difference in
how we invoke a dynamically created slot, by explicitly invoking
it through **[signal]**, instead of directly adding it as a node
name. This is to avoid trying to reference the slot as a C# slot,
and also helps you separate dynamically created slots, from static
C# slots. And in fact, all manipulation of dynamic slots, are slightly
different than statically compiled C# slots. For instance, the invocation
pattern of dynamic slots, doesn't allow us to pass in a _value_ to
our slot invocations, and only children arguments can be passed in.
A dynamic slot can however _return_ a value, as we saw above,
at which point the value will become the value of the **[signal]**
node after invocation.

**Notice** - Dynamic slots are _not_ persisted. This implies that
if you restart your process for some reasons, the slot no longer
exists. If you want to create dynamic slots that always exists in
your app, you'll have to put your slot creation Hyperlambda
into a _"magic.startup"_ folder, inside of your module's folder,
and create your slot from this file. This ensures that your slot
is re-created if the web server restarts for some reasons, since
all files inside of a module's _"magic.startup"_ folder are executed
every time the process restarts. You can see how this works in
your _"/modules/system/magic.startup/"_ folder, which contains
Hyperlambda files that creates dynamic slots during startup.

## [unwrap]

This is a special keyword, since it allows you to _"forward evaluate"_
expressions found as values in nodes. In a way, it's Hyperlambda's
version of _"apply"_, and often used in combination with dynamic
slots, to make sure we correctly pass in arguments to dynamic slots.
Consider the following code to understand what it does.

```
slots.create:foo.bar
   math.add
      get-value:x:@.arguments/*/arg1
      get-value:x:@.arguments/*/arg2
   return:x:@math.add

.arg1:int:5
.arg2:int:7

// Notice unwrap!
unwrap:x:+/*

signal:foo.bar
   arg1:x:@.arg1
   arg2:x:@.arg2
```

In the above Hyperlambda, we obviously want to pass in the _value_ of **[.arg1]**
and **[.arg2]** to our **[foo.bar]** slot. However, since each dynamic slot is
executed in isolation, on a copy of the lambda object, passed in as we created
the slot - This implies that the slot doesn't have access to our **[.arg1]**
or **[.arg2]** nodes as it's executing. This would result in that unless we
explicitly **[unwrap]** the invocation arguments we pass in as we invoke the
slot using **[signal]**, the slot will only see two expressions, leading
into _"oblivion"_. By _"unwrapping"_ the arguments before we invoke the slot though,
the invocation to our slot no longer contains expressions, but rather the _value_
of evaluating those expressions instead. So hence, the slot will be given
the values of 5 and 7 as its arguments, which of course it adds together, and
returns back to the caller as its result.

## Wrapping up

Although Hyperlambda is super-expressive for some types of
tasks, such as orchestration tasks, creating CRUD endpoints,
sending emails, etc - Some things it's _less_ suited for. I don't
advice you to add too much _"logic"_ into your Hyperlambda files,
but rather resort to [C# extension slots](/tutorials/extending-hyperlambda)
if you need a lot of business logic in your apps. If you find
yourself at the point where you're creating dozens of if
statements, loops, math operations, etc - It's probably smarter
to implement these parts of your app in C#, due to Hyperlambda's
sometimes cumbersome syntax to express complex branching and logic.

Also realize that Hyperlambda is _not_ as fast as C#. Every slot
invocation carries some overhead. Hence, you should not use it for
extremely CPU intensive operations, such as polygon rendering,
cryptography, etc - But rather create low level C# methods,
where you put your CPU intensive code, and then _"orchestrate"_
these methods together using Hyperlambda.

However, the beauty of Hyperlambda, is that once you've created
an intelligently architected slot, you can easily reuse this
slot, in many parts of your logic - By assembling together
your slot invocations using Hyperlambda, almost the same way
you'd assemble something with LEGO in the real world.

* [Documentation](/documentation)
