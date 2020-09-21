# Real programming with Hyperlambda

So far what we have done, have probably felt more like _"configuring"_ than
programming. In this tutorial, we will take the step into the Turing complete
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



* [Documentation](/documentation)
