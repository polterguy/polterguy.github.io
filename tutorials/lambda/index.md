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

* [Documentation](/documentation)
