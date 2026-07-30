---
title: Types and conversion
description: The [types], [type], [convert], [format] and [int2words] slots for working with Hyperlambda types, plus [vocabulary] returning every slot in your cloudlet.
---

## Types and conversion

These slots allow you to inspect and convert between Hyperlambda types, in addition to
returning the vocabulary of slots your cloudlet understands.

### How to use [types]

This slot returns all Hyperlambda types your current installation supports.

```
types
```

### How to use [type]

This slot returns the Hyperlambda type name of some value.

```
.foo:int:57
type:x:-
```

After invoking the above, the value of **[type]** will be `int`.

### How to use [convert]

This slot converts the value of an expression from its original type, to whatever **[type]** declaration you
supply as its argument.

```
.foo:57
convert:x:-
   type:int
```

**Notice** - You can also base64 encode and decode `byte[]` with this slot, by passing in _"base64"_ or
_"from-base64"_ as your **[type]** argument. The value of the object you want to convert must obviously support
conversion to the specified type, and will throw an exception if no conversion is possible, such as if you
for instance try to convert the string of _"foo-bar"_ to an integer.

### How to use [format]

This slot converts some expression or value according to some specified `String.Format` pattern.
The following code will string format the number 57 to make sure it's prefixed with leading zeros, always ending
up having at least 5 digits. See .Net String.Format method for which patterns you can use. The culture used will
be the invariant one, unless you explicitly override the culture with a **[culture]** argument.

```
.foo:int:57
format:x:-
   pattern:"{0:00000}"
```

To override the **[culture]** argument used you can use something such as follows.

```
.foo:decimal:57
format:x:-
   pattern:"{0:0.00}"
   culture:nb-NO
```

Since the above is using Norwegian Bokmal as its **[culture]** argument, it will return the result with a `,`
as a decimal separator instead of the default which is `.`. You can use the same **[pattern]** values for
this slot as you can use in C# and .Net. To see an extensive list of for instance the formatting patterns you
can use for a date and time object, you can browse the [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings)
related to this. If you don't supply a **[culture]** argument the invariant culture will be used.

### How to use [int2words]

This slot takes a signed 64 bit integer and converts it to its word representation, such as for instance 1200050 becoming _"one million two hundred thousand and fifty"_. Below is an example of using the slot.

```
int2words:1200050
```

The slot works with signed 64 bit integer values, implying it can work with numbers in the trillions if required. The result of executing the above should resemble the following.

```
int2words:one million two hundred thousand and fifty
```

The slot is particularly useful for RAG and VSS databases, where embedding models such as _"text-embedding-ada-002"_ tends to do a much better job at matching numbers if you spell these out instead of simply providing them as numbers.

### How to use [vocabulary]

Returns the name of every static slot in your system, optionally passing in a string, or an expression leading to
a string, which is a filtering condition, where the slot must _start_ with the filter specified to be considered
a part of the end result.

```
// Returns ALL slots in your system.
vocabulary

// Returns only slots starting with [io.file]
vocabulary:io.file
```

### How to use [whitelist]

This slot temporarily within the given scope changes the available slots, allowing you to declare a block
of lambda, where only a sub-set of your vocabulary is available for some piece of code to invoke. This allows
you to relatively securely allow some partially untrusted source to pass in a piece of Hyperlambda, for then
to allow it to evaluate its own Hyperlambda. The slot takes two arguments.

* __[vocabulary]__ - Whitelisted slots
* __[.lambda]__ - Lambda object to evaluate for the given scope

```
.result
whitelist

   vocabulary
      set-value
      return

   .lambda

      // Inside of this [.lambda] object, we can only invoke [set-value], and no other slots!
      set-value:x:@.result
         .:foo

      // Notice, the next line will throw an exception if you remove its "." character,
      // because [add] is not whitelisted in our above [vocabulary] declaration!
      .add:x:@.result
         .
            foo:bar
      return
         result:success
```

For security reasons the **[whitelist]** invocation's **[.lambda]** object is immutable, and the
caller _cannot_ access nodes outside of the **[.lambda]** object itself, which prohibits the caller
to modify, and/or read nodes from outside of its **[whitelist]** invocation. In addition a **[whitelist]**
invocation creates its own result stack object, allowing the **[whitelist]** invocation to return values
and nodes to the caller using for instance the **[return]** slot. If you execute the above Hyperlambda
you can see how this semantically works by realizing how the above **[.result]** node never has its
value actually changed, because our invocation to **[set-value]** inside our whitelist invocation yields
a _"null node-set result"_. Hence, semantically the **[whitelist]** slot works the same way signaling
a dynamic slot works in Hyperlambda, in that the invocation treats its **[.lambda]** object as if
it was a dynamic slot, isolating it from the rest of our code, allowing the lambda object to return
values and nodes to the caller.

### How to use [context]

This slot allows you to add an object unto the stack, such that it can later be retrieved with
the **[get-context]** slot. Below is an example.

```
.result

context:foo
   value:bar
   .lambda

      set-value:x:@.result
         get-context:foo
```

The slot requires a name as the value of its slot invocation node, a **[value]** as the value
you want to put onto the stack, and a **[.lambda]** object being the lambda where the stack object
exists, and can be retrieved using **[get-context]**. This is quite useful if you have some piece
of data that needs to be accessible through the entirety of the execution of some Hyperlambda snippet,
implying also for slots you invoke, where you don't want to pass in the data as an argument to the
slot itself. Imagine the following to understand how this works.

```
slots.create:bar

   get-context:foo
   return:x:-

context:foo
   value:Context value
   .lambda

      signal:bar
```

If you execute the above Hyperlambda you will notice how the slot called **[bar]** actually has access to
the context value called _"foo"_, and can retrieve this. This feature allows you to declare and create
_"long lasting arguments"_ that are accessible from within the entirety of a piece of Hyperlambda, including
each slot it invokes, and/or Hyperlambda files it executes.

### How to use [apply]

This slot takes an expression in addition to a list of arguments, and _"applies"_ the arguments unto the expression's
result node set, allowing you to perform dynamic substitutions on lambda hierarchies such as the following illustrates.

```
.lambda
   foo
      arg1:{some_arg}
      some-static-node:static-value

apply:x:-
   some_arg:value of argument
```

After execution of the above Hyperlambda you will have a result resembling the following.

```
apply
   foo
      arg1:value of argument
      some-static-node:static-value
```

Notice how the nodes from your template lambda object have been copied as children into your **[apply]**
node, while during this _"copying process"_, the arguments you supplied to **[apply]** have been used
to perform substitutions on all nodes in your template lambda having a value of `{xxx}`, where xxx is
your argument name. In the above example for instance the `arg1:{some_arg}` template node had its value
replaced by the value of the **[some_arg]** node passed in as a parameter to **[apply]**. If the name of
the argument to **[apply]**, matches the value of your template node wrapped inside curly braces - Then
the value of your argument to apply becomes the _new value_ of your template node after substitution has
been performed.

Only node values starting out with `{` and ending with `}` will be substituted, and you are expected to provide
all arguments found in the template lambda object, or the invocation will fail, resulting in an exception. This
allows you to create _"template lambda objects"_ that you dynamically transform into something else, without
really caring about its original structure, but rather only its set of dynamic substitution arguments. This
slot leaves all other nodes as is.

Basically, the way it works, is that it takes your expression, and recursively iterates each node below the
result of your expression, checks to see if the node's value is an argument such as e.g. `{howdy}` -
And if so, it substitutes the `{howdy}` parts with the value of the argument you are expected to supply to your
invocation having the name **[howdy]**.

You can also reference the same argument multiple times in your template, in addition to create arguments that
are lambda objects instead of simple values. Below is an example of both of these constructs.

```
.lambda
   foo
      foo1:{arg1}
      foo2:{arg1}
      foo3:{arg2}

apply:x:-
   arg1:int:5
   arg2
      this:is
         an:entire
         lambda:object
      used_as_an_argument:int:7
```

The above will result in the following.

```
apply
   foo
      foo1:int:5
      foo2:int:5
      foo3
         this:is
            an:entire
            lambda:object
         used_as_an_argument:int:7
```

Above you can also see how typing information is not lost, since the **[foo1]** and **[foo2]** nodes
are both having integer values of 5 after apply is done executing. At the same time you can see how
the **[foo3]** node instead of having a simple value applied, actually ended up with a copy of all
children passed in as **[arg2]**. You can also substitute names of nodes, such as the following
illustrates.

```
.lambda
   foo
      {arg1}:value-is-preserved

apply:x:-
   arg1:foo1
```

The above of course results in the following.

```
apply
   foo
      foo1:value-is-preserved
```

This is a fairly advanced slot, but it's the heart of the generator, allowing us to generate HTTP endpoints,
starting out with some template file, which is dynamically changed, according to input arguments supplied during
the crudification process. You can also combine transformations of names, values, and children in the
same template nodes. The process is also recursive in nature, performing substitutions through the entire
hierarchy of your template lambda.

### How to use [sort]

Sort takes an expression leading to a list of nodes, in addition to a lambda object. Your lambda
object will be invoked several times, with an **[.lhs]**, an **[.rhs]** and a **[.result]** argument.
It is your code's responsibility to set the value of the **[.result]** node according to which of the
**[.lhs]** and **[.rhs]** node should come first in the sorted result.

```
.data
   .
      name:Thomas
   .
      name:John
   .
      name:Jane
   .
      name:Peter
sort:x:@.data/*
   if
      lt:x:@.lhs/#/*/name
         get-value:x:@.rhs/#/*/name
      .lambda
         set-value:x:@.result
            .:int:-1
   else-if
      mt:x:@.lhs/#/*/name
         get-value:x:@.rhs/#/*/name
      .lambda
         set-value:x:@.result
            .:int:1
   else
      set-value:x:@.result
         .:int:0
```

Notice, **[sort]** does not modify the original list, but returns a new list of nodes after having executed.
