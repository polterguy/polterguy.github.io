
# Magic Lambda

Magic lambda is where you will find the _"keywords"_ of Hyperlambda.
It is what makes Hyperlambda Turing complete, and contains slots such as **[for-each]**
and **[if]**.

## Structure

Since _everything_ is a slot in Hyperlambda, this allows you to evaluate its conditional operators and logical operators,
the same way you would evaluate a function in a traditional programming language. This might at first seem a bit unintuitive
if you come from a traditional programming language, but has a lot of advantages, such as allowing the computer to look
at the entirety of your function objects as hierarchical tree structures, parsing them as such, and imagining these as
_"execution trees"_.

For instance, in a normal programming language, the equal operator must have a left hand side (lhs), and a right hand
side (rhs). In Hyperlambda this is not true, since the equal slot is the main invocation of a function, requiring two
arguments, allowing you to think about it as a _function_. To compare this to the way a traditional programming might
have implemented this, imagine the equal operator as a function, such as the following pseudo code illustrates.

```
=(arg1, arg1)
```

The actual Hyperlambda code that would be the equivalent of the above pseudo code, can be found below.

```
eq
   .:arg1
   .:arg2
```

As you study Hyperlambda, it might be beneficial to use the _"Evaluator"_ component that you can find in its
frontend Angular dashboard website. This component allows you to play with Hyperlambda in _"immediate mode"_,
allowing you to experiment with it, execute it immediately from your browser, using a very rich code editor,
providing syntax highlighting, autocomplete on slots, and allows you to save your snippets for later on your
server. If you do this, then click the _"information button"_ in the component to learn the basic shortcuts,
and access help in general. Below is a screenshot of the _"Evaluator"_ component to give you an idea of what
you might expect.

<img alt="Hyperlambda Evaluator" title="Hyperlambda Evaluator" src="https://servergardens.files.wordpress.com/2020/05/evaluator.png" />

Logically the Hyperlambda evaluator will signal each nodes in your Hyperlambda code sequentially, assuming
all of your nodes are referencing an `ISlot` class, unless the node's name starts with a _"."_ or has an empty name.

## Hyperlambda structure

Hyperlambda is the textual representation of a node structure, where each node has a name, an optional value,
and a collection of children nodes. Imagine the following Hyperlambda.

```
name:value
   child1
```

In the above Hyperlambda, there is one root node. Its name is _"name"_, its value is _"value"_, and this node
has one child node, with the name of _"child1"_. Its child node does _not_ however have a value, which results
in its value being _"null"_. The reason why the Hyperlambda parser understands _"child1"_ as the child of 
the _"name"_ node, is because it is prefixed by 3 spaces (SP) relatively to the _"name"_ node. This allows you
to create graph objects (tree structures) with any depth you wish, by simply starting out with the number of
spaces the node above has, add 3 additional spaces, and you can declare children nodes of the above node.

If you think of these nodes as a sequence of function invocations, from the top to bottom, where all of the
nodes are assumed to be referencing slots - You can imagine how the tree structure resulting from parsing
Hyperlambda into a graph object can easily be evaluated, due to its recursive nature, making it easy to
express idioms such as _"if"_, _"while"_, _"for-each"_, etc.

Since each slot will be invoked with the node referencing the slot itself as the _"input"_ `Node`,
this makes the Hyperlambda evaluator recursive in nature, allowing a slot to evaluate all of its children,
after executing its custom logic, etc. And yes, before you ask, Hyperlambda has been heavily influenced by
LISP. In many ways, Hyperlambda _is_ LISP for C#.

## Extending Hyperlambda

To understand the relationship between C# and Hyperlambda, it might be beneficial for you to analyze the
following code. The following code creates a new `ISlot` for you, implementing the interface found in
the NuGet package called _"magic.signals.contracts"_.

```csharp
using magic.node;
using magic.signals.contracts;

namespace acme.foo
{
    [Slot(Name = "acme.foo")]
    public class Foo : ISlot
    {
        public void Signal(ISignaler signaler, Node input)
        {
            var arg1 = input.Children.First().Get<int>();
            var arg2 = input.Children.Skip(1).First().Get<int>();
            input.Value = arg1 + arg2;
            input.Clear();
        }
    }
}
```

The above will result in a slot you can invoke from Hyperlambda using the following code.

```
acme.foo
   arg1:5
   arg2:7
```

Which of course will result in the following after having been executed.

```
acme.foo:int:12
```

Notice the relationship between the `[Slot(Name = "acme.foo")]` C# code, and the way we invoke the `acme.foo`
slot from Hyperlambda afterwards. It might help to imagine Hyperlambda as a simple string/type Dictionary,
which resolves an object from your IoC container, using the name of the node as the key.

To create your own slots, follow the recipe below.

1. Reference the NuGet package `magic.signals.contracts` in your project.
2. Create your class, and implement the `ISlot` interface.
3. Mark your class with the `Slot` attribute, giving it an adequate `Name` property value.

**Notice** - You can also implement `ISlotAsync` if you want to create an `async` slot.

## The gory details

At the heart of Hyperlambda is the **[eval]** slot, this slot is responsible for executing your lambda object,
and it follows a couple of simple rules.

All nodes starting with a _"."_ will be ignored, and **[eval]** will not try to raise these nodes as signals.
This has two benefits.

1. You can create _"hidden"_ slots, that are only accessible from C#.
2. You can use nodes starting with _"."_ as data nodes, separating function invocations from data.

**[eval]** makes Hyperlambda _"super functional"_ in nature. Below is an example of a Hyperlambda
piece of code, that illustrates this, by adding a _"callback"_ lambda object to its POP3 fetch emails
slot, which will be invoked once for each available email on your POP3 server.

```
/*
 * Example of how to retrieve emails form a POP3 server.
 */
mail.pop3.fetch
   max:int:50
   raw:bool:false
   .lambda

      /*
       * Some lambda object invoked once for every email fetched.
       * Given message as [.message] node structured as lambda.
       */
      lambda2hyper:x:..
      log.info:x:-
```

The `ISlot` called **[mail.pop3.fetch]** will invoke the above **[.lambda]** object once for each email
it finds on the POP3 server it connects to. It will use the **[eval]* slot to do this.

## Tokens

The separating of a node's name and its value, is done by using a ":" character. To the left is the node's
name, and to the right is its value. The value of a node can also be a C# type of string, using double
quotes, and even single quotes or prefix your opening double quote with an "@" character, allowing you
to use carriage returns in your strings the same way you would do in for instance C#. Below is an example

```
.str1:"   This is a \r\n  string"
.str2:' This is also a string '
.str3:@"This
    is
  also a
      string"
```

Strings in Hyperlambda can be escaped with the exact same semantics as you would escape your C# strings.

## Comments

Hyperlambda accepts comments the exacts same way C# does, and you can use either multiline comments,
or single line comments, like the following example illustrates.

```
/*
 * Multiline comment.
 */

// Single line comment.
```

You _cannot_ put comments on lines containing nodes however.

## Lambda expressions

To understand Hyperlambda, and how to efficiently create your own Hyperlambda, you'll have to understand
_"lambda expressions"_. These are kind of like XPath expressions. However, instead of referencing XML
nodes, lambda expressions are referencing lambda nodes. This allows you to retrieve node names, values,
and their children collection - For either to manipulate these, or read their values and react accordingly.

Notice, Hyperlambda does not separate between a _"variable"_ and a _"function invocation"_ - Hence, a node
might serve as both at the same time. This allows you to dynamically modify your lambda structure, as you
traverse it, and execute it - But this creates another problem for you, which is that you will need
a mechanism to store data. This is accomplished by prefixing a node's name with a "." character, at which point
the Hyperlambda evaluator will ignore it, as it is traversing your tree, and _not_ attempt to signal
that particular node as a slot. Think of all nodes starting with a `.` character as _"data segments"_
or variables for that matter.

Combining _"data nodes"_ with expressions, allows you to use, modify and reference these as _"variables"_.
Below is an example.

```
.src:foo
.dest
set-value:x:@.dest
   get-value:x:@.src
```

What the above code basically translates into, is.

> Set the value of the [.dest] node to the value of [.src]

## Branching and conditional execution

Magic Lambda contains the following slots. Most of these slots have async overloads, which will be
automatically used by Magic if possible.

### [if]

This is the Hyperlambda equivalent of `if` from other programming languages. It allows you to test for some condition,
and evaluate a lambda object, only if the condition evaluates to true. **[if]** must be given exactly two arguments.
The first argument can be anything, including a slot invocation - But its second argument must be its **[.lambda]**
argument. The **[.lambda]** node will be evaluated as a lambda object, only if the first argument to **[if]** evaluates
to boolean true. Below is an example.

```
.dest
if
   .:bool:true
   .lambda
      set-value:x:@.dest
         .:yup!
```

All conditional slots, including **[if]**, optionally accepts slots as their first condition argument.
This allows you to invoke slots, treating the return value of the slot as the condition deciding
whether or not the **[.lambda]** object should be executed or not. Below is an example.

```
.arguments
   foo:bool:true
.dest

if
   get-value:x:@.arguments/*/foo
   .lambda
      set-value:x:@.dest
         .:yup!
```

### [else-if]

**[else-if]** is the younger sibling of **[if]**, and must be preceeded by its older sibling, or other **[else-if]** nodes,
and will only be evaluated if all of its previous conditional slots evaluates to false - At which point **[else-if]** is
allowed to test its condition - And only if it evaluates to true, evaluate its lambda object. Semantically **[else-if]**
is similar to **[if]**, in that it requires exactly two arguments with the same structure as **[if]**.

```
.dest
if
   .:bool:false
   .lambda
      set-value:x:@.dest
         .:yup!
else-if
   .:bool:true
   .lambda
      set-value:x:@.dest
         .:yup2.0!
```

### [else]

**[else]** is the last of the _"conditional siblings"_ that will only be evaluated as a last resort, only if none of its
elder _"siblings"_ evaluates to true. Notice, contrary to both **[if]** and **[else-if]**, **[else]** contains its lambda object
directly as children nodes, and _not_ within a **[.lambda]** node. This is because **[else]** does not require any
conditional arguments like **[if]** and **[else-if]** does. An example can be found below.

```
.src:int:3
.dest
if
   eq
      get-value:x:@.src
      .:int:1
   .lambda
      set-value:x:@.dest
         .:yup!
else-if
   eq
      get-value:x:@.src
      .:int:2
   .lambda
      set-value:x:@.dest
         .:yup2.0!
else
   set-value:x:@.dest
      .:nope
```

### [switch]

**[switch]** works similarly as a switch/case block in a traditional programming language, and will find the
first **[case]** node with a value matching the evaluated value of the **[switch]** node, and execute that
**[case]** node as a lambda object.

```
.val:foo
.result
switch:x:@.val
   case:bar
      set-value:x:@.result
         .:Oops
   case:foo
      set-value:x:@.result
         .:Success!
```

The **[switch]** slot can only contain two children nodes, **[case]** and **[default]**. The **[default]** node
will be evaluated if _none_ of the **[case]** node's values are matching the evaluated value of your **[switch]**.
Try evaluating the following in your _"Evaluator"_ to understand what I mean.

```
.val:fooXX
.result
switch:x:@.val
   case:bar
      set-value:x:@.result
         .:Oops
   case:foo
      set-value:x:@.result
         .:Oops2.0
   default
      set-value:x:@.result
         .:Success!
```

In the above, the expression evaluated in the switch, which is `@.val` will become _"fooXX"_ after evaluating it.
None of its children **[case]** nodes contains this as an option, hence the **[default]** node will be evaluated,
and this results in setting the **[.result]** node's value to _"Success!"_.

**[default]** _cannot_ have a value, and all your **[case]** nodes must have a _constant_ value, meaning not
an expression. However, any types can be used as values for your **[case]** nodes. And your **[switch]** node
must at the very least have minimum one **[case]** node. The **[default]** node is optional though.

## Comparisons

### [eq]

**[eq]** is the equality _"operator"_ in Magic, and it requires two arguments, both of which will be evaluated as potential
signals - And the result of evaluating **[eq]** will only be true if the values of these two arguments are _exactly the same_.
Notice, the comparison operator will consider types, which implies that boolean true will _not_ be considered equal to the string
value of _"true"_, etc.

```
.src:int:5
eq
   get-value:x:@.src
   .:int:5
```

### [lt]

**[lt]** will do a comparison between its two arguments, and only return true if its first argument is _"less than"_
its seconds argument. Consider the following.

```
.src1:int:4
lt
   get-value:x:@.src1
   .:int:5
```

### [lte]

**[lte]** will do a comparison between its two arguments, and only return true if its first argument is _"less than or equal"_
to its seconds argument. Consider the following.

```
.src1:int:4
lte
   get-value:x:@.src1
   .:int:4
```

### [mt]

**[mt]** will do a comparison between its two arguments, and only return true if its first argument is _"more than"_
its seconds argument. Consider the following.

```
.src1:int:7
mt
   get-value:x:@.src1
   .:int:5
```

### [mte]

**[mte]** will do a comparison between its two arguments, and only return true if its first argument is _"more than or equal"_
to its seconds argument. Consider the following.

```
.src1:int:7
mte
   get-value:x:@.src1
   .:int:5
```

## Boolean logical conditions

### [exists]

**[exists]** will evaluate to true if its specified expression yields one or more results. If not, it will
return false.

```
.src1
   foo
.src2
exists:x:@.src1/*
exists:x:@.src2/*
```

### [and]

**[and]** requires two or more arguments, and will only evaluate to true, if all of its arguments evaluates to true. Consider
the following.

```
and
   .:bool:true
   .:bool:false
and
   .:bool:true
   .:bool:true
```

And will (of course) evaluate its arguments before checking if they evaluate to true, allowing you to use it as a part
of richer comparison trees, such as the following illustrates.

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

### [or]

**[or]** is similar to **[and]**, except it will evaluate to true if _any_ of its arguments evaluates to true, such
as the following illustrates. **[or]** will also evaluate its arguments, allowing you to use it as a part of richer comparison
trees, the same way **[and]** allows you to. Below is a simple example.

```
or
   .:bool:false
   .:bool:false
or
   .:bool:false
   .:bool:true
```

### [not]

**[not]** expects _exactly one argument_, and will negate its boolean value, whatever it is, such as the following illustrates.

```
not
   .:bool:true
not
   .:bool:false
```

**[not]** will also evaluate its argument, allowing you to use it in richer comparison trees, the same you could do
with both **[or]** and **[and]**.

## Modifying your graph

### [add]

This slot allows you to dynamically add nodes into a destination node. Its primary argument is the destination,
and it assumes that each children is a collection of nodes it should append to the destination node's children
collection. The reasons for this additional level of indirection, is because the **[add]** slot might have
children that are by themselves slot invocations, which it will evaluate before it starts adding the children
nodes of these arguments to its destination node's children collection. Below is an example.

```
.dest
add:x:@.dest
   .
      foo1:howdy
      foo2:world
   .
      bar1:hello
      bar2:world
```

Notice how all the 4 nodes above (foo1, foo2, bar1, bar2) are appended into the **[.dest]** node's children
collection. This allows you to evaluate slots and add the result of your slot invocation into the destination,
such as the following illustrates.

```
.src
   foo1:foo
   foo2:bar
.dest
add:x:@.dest
   get-nodes:x:@.src/*
```

**[add]** can also take an expression leading to multiple destinations as its main argument, allowing you to
add a copy of your source nodes into multiple node collections at the same time, with one invocation.

### [insert-before]

This slot functions exactly the same as the **[add]** node, except it will insert the nodes _before_ the
node(s) referenced in its main argument.

```
.foo
   foo1
   foo2
insert-before:x:@.foo/*/foo1
   .
      inserted
```

### [insert-after]

This slot functions exactly the same as the **[add]** node, except it will insert the nodes _after_ the
node(s) referenced in its main argument.

```
.foo
   foo1
   foo2
insert-after:x:@.foo/*/foo1
   .
      inserted
```

### [remove-nodes]

This slot will remove all nodes its expression is pointing to.

```
.data
   foo1
   foo2
   foo3
remove-nodes:x:@.data/*/foo2
```

### [set-value]

Changes the value of a node referenced as its main expression to whatever its single source happens to be.
Notice, when you invoke a slot that tries to change the value, name, or the node itself of some expression,
and you supply a source expression to your invocation - Then the result of the source expression
_cannot_ return more than one result. The destination expression however can modify multiple nodes
at the same time.

```
.foo
set-value:x:@.foo
   .:SUCCESS
```

### [set-name]

Changes the name of a node referenced as its main expression to whatever its single source happens to be.

```
.foo
   old-name
set-name:x:@.foo/*
   .:new-name
```

### [unwrap]

This slot is useful if you want to invoke another slot, but before you do, you want to evaluate some expressions
inside of some argument to your slot. Imagine the following.

```
.src:Hello World
unwrap:x:+
.dest:x:@.src
```

In the above example, before the **[.dest]** node is reached by the Hyperlambda instruction pointer, the value
of the **[.dest]** node will have been _"unwrapped"_ (evaluated), and its value will be _"Hello World"_.
When you invoke lambda objects that are cloned for some reasons, this slot becomes very handy, since
it allows you to _"forward evaluate"_ expressions inside your lambda object. It's also useful when
you have expressions inside for instance a **[return]** slot, and you want to return the _value_
the expression evaluates to, and not the expression itself.

## Source slots

### [get-value]

Returns the value of the node its expression is pointing to.

```
.data:Hello World
get-value:x:-
```

### [get-name]

Returns the name of the node referenced in its expression.

```
.foo
get-name:x:-
```

### [get-count]

This slot returns the number of nodes its expression is pointing to.

```
.data
   foo1
   foo2
get-count:x:@.data/*
```

### [get-nodes]

Returns the nodes its expression is referencing.

```
.data
   foo1
   foo2
get-nodes:x:-/*
```

### [reference]

This slot will evaluate its expression, and add the entire node the expression is pointing to, as a referenced node into
its value. This allows you to pass a node _into_ a slot by reference, and have that slot modify the node itself, or
its children. This might sometimes be useful to have slots modify some original graph object, or parts of a graph -
Or get access to iterate over parts of your graph object's children.

```
.foo
reference:x:@.foo
set-value:x:-/#
   .:Yup!
```

You can think of this slot as the singular version of **[get-nodes]**, except instead of returning multiple
nodes, it assumes its expression only points to a single node, and instead of returning a copy of the node,
it returns the actual node by reference.

**Notice** - The `#` iterator above, will enter into the node referenced as a value of its current
result - Implying it allows you to deeply traverse nodes passed in as references. This is sometimes
useful in combination with referenced nodes, passed in as values of other nodes.

### [convert]

This slot converts the value of an expression from its original type, to whatever **[type]** declaration you
supply as its argument.

```
.foo:57
convert:x:-
   type:int
```

**Notice** - You can also base64 encode and decode `byte[]` with this slot, by passing in _"base64"_ or
_"from-base64"_ as your **[type]** argument.

### [type]

This slot return the Hyperlambda type name of some value.

```
.foo:int:57
type:x:-
```

After invoking the above, the value of **[type]** will be `int`.

### [format]

This slot converts the format some expression or value according to some specified `String.Format` expression.
The following code will string format the number 57 making sure it's prefixed with leading zeros always ending
up having at least 5 digits. See .Net String.Format for which patterns you can use. The culture used will always
be the invariant one.

```
.foo:int:57
format:x:-
   pattern:"{0:00000}"
```

### [get-context]

This slot returns a context stack object, which is an object added to the stack using **[context]**.

## Exceptions

### [try]

This slot allows you to create a try/catch/finally block of lambda, from where exceptions are caught,
and optionally hadled in a **[.catch]** lambda, and/or a **[.finally]** lambda.

```
try
   throw:Whatever
.catch
   log.info:ERROR HAPPENED!! 42, 42, 42!
.finally
   log.info:Yup, we are finally there!
```

### [throw]

This slot simply throws an exception, with the exception message taken from its value.
See the **[try]** slot for an example. Notice, you can make the exception propagate to the client
by adding a **[public]** parameter, and set its value to boolean _"true"_. At which point
the exception will be returned to the client, even in release builds. Otherwise, the exception
will only be visible in debug builds, and never returned to the client. You can also modify
the **[status]** HTTP return value that's returned to the client, to become e.g. 404,
indicating _"not found"_, etc.

## Loops

### [for-each]

Iterates through each node as a result of an expression, and evaluates its lambda object,
passing in the currently iterated node as a **[.dp]** argument, containing the actual node
iterated by reference.

```
.data
   foo1
   foo2
for-each:x:-/*
   set-value:x:@.dp/#
      .:hello
```

See the documentation for the **[reference]** slot to understand how reference nodes works.

### [while]

Semantically similar to **[if]**, but instead of evaluating its lambda object once, will iterate it for
as long as the condition evaluates to true. Requires _exactly_ two arguments, the same way **[if]** does.

```
.no:int:0
.res
while
   lt
      get-value:x:@.no
      .:int:5
   .lambda
      add:x:@.res
         .
            foo
      math.increment:x:@.no
```

## Evaluating slots

### [eval]

Evaluates each lambda object found by either inspecting its children collection, or evaluating the
expression found in its value.

```
.res
.lambda
   set-value:x:@.res
      .:OK
eval:x:@.lambda
```

### [whitelist]

This slot temporarily within the given scope changes the available slots, allowing you to declare a block
of lambda, where only a sub set of your vocabulary is available for some piece of code to signal. This allows
you to relatively securely allow some partially untrusted source to pass in a piece of Hyperlambda, for then
to allow it to evaluate its own Hyperlambda. The slot takes two arguments.

* __[vocabulary]__ - Whitelisted slots
* __[.lambda]__ - Lambda object to evaluate for the given scope

```
.result
whitelist
   vocabulary
      set-value
   .lambda

      // Inside of this [.lambda] object, we can only invoke [set-value], and no other slots!
      set-value:x:@.result
         .:foo

      // Notice, the next line will throw an exception,
      // because [add] is not whitelisted in our above [vocabulary] declaration!
      add:x:@.result
         .
            foo:bar
```

### [context]

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
exists, and can be retrieved using **[get-context]**.

## Threading

### [fork]

Forks the given lambda into a new thread of execution, using a thread from the thread pool. This
slot is useful for creating _"fire and forget"_ lambda objects, where you don't need to wait
for the result of the execution before continuing executing the current scope.

```
fork
   info.log:I was invoked from another thread
```

### [semaphore]

Creates a named semaphore, where only one thread will be allowed to evaluate the same semaphore at
the same time. Notice, the semaphore to use is defined through its value, implying you can use the same
semaphore multiple places, by using the same value of your **[semaphore]** invocation.

```
semaphore:foo-bar
   /*
    * Only one thread will be allowed entrance into this piece of
    * code at the same time, ensuring synchronised access, for cases
    * where you cannot allow more than one thread to enter at the
    * same time.
    */
```

### [sleep]

This slot will sleep the current thread for x number of milliseconds, where x is an integer value, expected
to be passed in as its main value.

```
// Sleeps the main thread for 1 second, or 1000 milliseconds.
sleep:1000
```

## Miscellaneous slots

### [vocabulary]

Returns the name of every static slot in your system, optional passing in a string, or an expression leading to
a string, which is a filtering condition where the slot must _start_ with the filter in its name, to be considered
a part of the end result.

```
// Returns ALL slots in your system.
vocabulary

// Returns only slots starting with [io.file]
vocabulary:io.file
```

### [apply]

This slot takes an expression in addition to a list of arguments, and _"applies"_ the arguments unto the expression's
result, allowing you to perform dynamic substitutions on lambda hierarchies such as the following illustrates.

```
.lambda
   foo:{howdy}
apply:x:-
   howdy:world
```

After execution of the above Hyperlambda you will have s result resembling the following.

```
.lambda
   foo:{howdy}
apply
   foo:world
```

Only node values starting out with `{` and ending with `}` will be substituted, and you are expected to provide
all arguments found in the template lambda object, or the invocation will fail, resulting in an exception. This
allows you to create _"template lambda objects"_ which you dynamically transform into something else, without
really caring about its original structure, only its set of arguments.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda](https://github.com/polterguy/magic.lambda), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.
