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
executes if it should be executed as children, directly beneath
the else node itself. Yet again, everything is a lambda block in
Hyperlambda - Hence, thinking of only **[.lambda]** blocks
as being lambda, is not productive.

## Boolean "operators"

* [Documentation](/documentation)
