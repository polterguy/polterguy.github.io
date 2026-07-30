---
title: magic.lambda
description: The programming language keywords of Hyperlambda - branching, loops, comparisons, exception handling, and the slots that modify your lambda object.
---

magic.lambda is where you will find the _"programming language keywords"_ of Hyperlambda.
It is what makes Hyperlambda Turing complete, and contains slots such as **[for-each]**,
**[if]**, and **[while]**. If you want to learn more, this is probably where you should start.

Notice, you do _not_ need to master these slots to use Magic - the
[Hyperlambda Generator](/dashboard/hyperlambda-generator/) writes the code for you from plain
English. This reference exists for when you want to read, understand, or hand-modify what the
machine created.

## Reference documentation

The slot reference is organised by concept, with one page per concept.

* [Executing lambda objects](/plugins/magic.lambda/executing/) - **[compose]**, **[eval]** and **[invoke]**
* [Branching and conditional execution](/plugins/magic.lambda/branching/) - **[if]**, **[else-if]**, **[else]** and **[switch]**
* [Comparison and boolean logic](/plugins/magic.lambda/conditions/) - **[eq]**, **[neq]**, **[lt]**, **[lte]**, **[mt]**, **[mte]**, **[and]**, **[or]** and **[not]**
* [Modifying your lambda object](/plugins/magic.lambda/nodes/) - **[add]**, **[insert-before]**, **[set-value]**, **[unwrap]**, **[get-value]**, **[exists]**, **[reference]** and more
* [Hyperlambda exceptions](/plugins/magic.lambda/exceptions/) - **[try]** and **[throw]**
* [Hyperlambda loops](/plugins/magic.lambda/loops/) - **[for-each]** and **[while]**
* [Types and conversion](/plugins/magic.lambda/types/) - **[types]**, **[type]**, **[convert]**, **[format]**, **[int2words]** and **[vocabulary]**

## Hyperlambda internals

_Everything_ is a slot in Hyperlambda. This allows you to evaluate and extend its conditional operators and logical operators
the same way you would evaluate or create a function in a traditional programming language. This might at first seem a bit weird
if you come from a traditional programming language, but has a lot of advantages, such as allowing the computer to look
at the entirety of your function object as a hierarchical tree structure, parsing it as such, and executing your lambda
object as an _"execution tree"_.

In a normal programming language, the equal operator must have a left hand side (lhs), and a right hand
side (rhs). In Hyperlambda this is different, since the equal slot is the main invocation of a function, requiring two
arguments, allowing you to think about it as a _function_. To compare this to the way a traditional programming might
have implemented this, imagine the equal operator as a function, such as the following pseudo code illustrates.

```
equals(object lhs, object rhs)
```

The actual Hyperlambda code that would be the equivalent of the above pseudo code, can be found below, and this code
actually executes successfully if you execute it as Hyperlambda.

```
eq
   .:lhs
   .:rhs
```

As you study Hyperlambda it might be beneficial to use the _"Hyperlambda Playground"_ component that you can find in its
frontend dashboard. This component allows you to play with Hyperlambda in _"immediate mode"_,
experiment with Hyperlambda, execute it immediately from your browser, in a rich code editor,
providing syntax highlighting for you, autocomplete on slots, etc. The _"Hyperlambda Playground"_ component also allows
you to save your snippets for later on your server.

If you put your cursor on an empty line and click CTRL+SPACE or FN+CONTROL+SPACE on a Mac, you will be given
autocomplete, allowing you to easily see which slots are available for you.

Logically the Hyperlambda evaluator will signal each node in your Hyperlambda code sequentially, assuming
all of your nodes are referencing an `ISlot` class, unless the node's name starts with a _"."_ or has an empty name.
Most slots again are recursively executing their children slots, resulting in a recursively executed _"execution tree"_.

## Hyperlambda structure

Hyperlambda is the textual representation of a node structure, where each node has a name, an optional value,
and a collection of children nodes. Imagine the following Hyperlambda.

```
name:value
   child1
```

In the above Hyperlambda there is one root node. Its name is _"name"_, its value is _"value"_, and this node
has one child node, with the name of _"child1"_. Its child node does _not_ however have a value, which results
in its value being _"null"_. The reason why the Hyperlambda parser understands _"child1"_ as the child of 
the _"name"_ node, is because it is prefixed by 3 spaces (SP) relative to the _"name"_ node. This allows you
to create graph objects (tree structures) with any depth you wish, by simply starting out with the number of
spaces the node above has, add 3 additional spaces, and you have declared children nodes of the node above.

If you think of these nodes as a sequence of function invocations, from the top to bottom, where all of the
nodes are assumed to be referencing slots, and all children nodes arguments to your slots - You can imagine
how the tree structure resulting from parsing Hyperlambda into a graph object can easily be evaluated, due
to its recursive nature, making it easy to express idioms such as _"if"_, _"while"_, _"for-each"_, etc. In
fact logically this is similar to the way XSLT works, except there's no XML, only Hyperlambda, lambda objects,
and nodes.

Since each slot will be invoked with the node referencing the slot itself as the _"input"_ `Node`,
this makes the Hyperlambda evaluator recursive in nature, allowing a slot to evaluate all of its children,
after executing its custom logic, etc. And yes, before you ask, Hyperlambda has been heavily influenced by
LISP. In some ways Hyperlambda _is_ Lisp for C#, only with a completely different syntax, and without S-Expressions.

## Extending Hyperlambda with C#

To understand the relationship between C# and Hyperlambda, it might be beneficial for you to analyze the
following code. The following code creates a new `ISlot` for you, implementing the interface found in
the NuGet package called _"magic.signals.contracts"_.

```
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

Notice the relationship between the `[Slot(Name = "acme.foo")]` C# code and the way we invoke the **[acme.foo]**
slot from Hyperlambda afterwards. It might help to imagine Hyperlambda as a simple string/type Dictionary,
resolving an object from your IoC container using the name of the node as the key. And in fact, this
is exactly how Hyperlambda _is_ implemented - As a string/type dictionary, creating instances of your slot
classes using your IoC container, for then to invoke its `Signal` method, passing in the identity node to your slot,
where the identity node is the node invoking your signal from Hyperlambda.
To create your own C# or F# slots, you can follow the following recipe.

1. Reference the NuGet package `magic.signals.contracts` in your project.
2. Create your class, and implement the `ISlot` interface.
3. Mark your class with the `Slot` attribute, giving it an adequate `Name` property value.

**Notice** - You can also implement `ISlotAsync` if you want to support `async` invocations.

## How Hyperlambda invokes slots

At the heart of Hyperlambda is the **[eval]** slot. This slot is responsible for executing your lambda object
and follows a couple of simple rules. All nodes starting with a _"."_ will be ignored, and **[eval]** will not
try to raise these nodes as signals. This has two benefits.

1. You can create _"hidden"_ slots, that are only accessible from C#.
2. You can use nodes starting with _"."_ as data nodes, separating function invocations from data.

**[eval]** makes Hyperlambda _"super functional"_ in nature. Below is an example of a Hyperlambda
piece of code, that illustrates this, by adding a _"callback"_ lambda object to its **[while]** invocation
as a **[.lambda]** node, that will be invoked once for every iteration of your while loop.

```
.no:int:0

while
   lt
      get-value:x:@.no
      .:int:20
   .lambda

      // Your lambda goes here.
      log.info:Howdy from while
      math.increment:x:@.no
```

## Hyperlambda tokens

The separating of a node's name and its value is done by using a `:` character. To the left is the node's
name, and to the right is its value. The value of a node can also be a C# type of string, using double
quotes, and even single quotes, or prefix your opening double quote with an "@" character, allowing you
to use carriage returns in your strings the same way you can in for instance C#. Below are some examples.

```
.str1:"   This is a \r\n  string"
.str2:' This is also a string '
.str3:@"This
    is
  also a
      string"
```

Strings in Hyperlambda can be escaped with the exact same semantics as you would escape your C# strings,
including referencing UNICODE characters in your strings. Hyperlambda is _always_ serialized using UTF8,
so you can add any UNICODE characters in your Hyperlambda you wish. Just make sure you save your files
as UTF8 if you are using an external code editor to edit your Hyperlambda files.

## How to comment your Hyperlambda code

Hyperlambda accepts comments the exact same way C# does, and you can use either multiline comments
or single line comments, like the following example illustrates.

```
/*
 * Multiline comment.
 */

// Single line comment.
```

You _cannot_ put comments on lines containing nodes, and comments must be indented the same
amount of indentations as the nodes they are commenting, implying the nodes below them. Below is
an example.

```
.data
   foo1:bar1
   foo2:bar2

for-each:x:@.data/*

   // This is correct indentation.
   set-value:x:@.dp/#
      .:Loop was here ...
```

Since Hyperlambda is using spaces (SP characters) to denote scope, indentation _is important_,
also for comments. If you de-indent the above comment, you might get unpredictable results, in particular
if you're serializing and de-serializing your Hyperlambda preserving comments. Comments should as a general
rule of thumb be applied with the same amount of indentation as the node below them.

## Hyperlambda data segments

Hyperlambda does not separate between a _"variable"_ and a _"function invocation"_. Hence, a node
might serve as both at the same time. This allows you to dynamically modify your lambda structure, as you
traverse it and execute it. But this creates another problem for you, which is that you will need
a mechanism to store data. This is accomplished by prefixing a node's name with a `.` character, at which point
the Hyperlambda evaluator will ignore it, as it is traversing your tree, and _not_ attempt to signal
that particular node as a slot. Think of all nodes starting with a `.` character as _"data segments"_,
or variables for that matter. Below is an example where **[eval]** will simply ignore the **[.src]** node
and the **[.dest]** node, not attempting to invoke these as slots, but treat these as _"data nodes"_.

```
.src:foo
.dest
set-value:x:@.dest
   get-value:x:@.src
```

If you change name of the above **[.src]** node to simply **[src]**, your code will raise an exception,
with an error such as follows _"No slot exists for [src]"_ since this slot doesn't exist in your Hyperlambda
vocabulary - Unless you for some reasons have an installation where this slot has been explicitly added to
your vocabulary.

## Hyperlambda documentation conventions

When we document Hyperlambda slots, and nodes, which are almost the same, we will document the node's
name with square brackets surrounding it, such as **[this]** illustrates, where _"this"_ is referencing
a node, and is the name of a node. We will also make such node references **bold**, to make them
more easy to see.

## Lambda expressions

Hyperlambda is heavily using _"lambda expressions"_. Think of these like XPath, except instead
of referencing XML nodes they're referencing Hyperlambda nodes. You can find the documentation
for expressions in the [magic.node](https://docs.ainiro.io/plugins/magic.node/) project.
