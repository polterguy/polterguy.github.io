---
title: Expressions, slots, and nodes in Hyperlambda
description: In this article you will learn the three most fundamental building blocks of Hyperlambda, being expressions, Hyperlambda's syntax, and how these relate to Hyperlambda's C# code, more specifically Magic's Node class.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-expressions.jpg"
---

# Expressions, slots, and nodes in Hyperlambda

This tutorial covers the following parts of Magic and Hyperlambda.

* Hyperlambda's syntax
* How Hyperlambda relates to C# and the Node class
* How expressions allows you to reference nodes
* How to modify your lambda objects during execution
* Creating slots from C#

Fundamentally Hyperlambda is just a text representation of a tree structure, the same
way XML, YAML, and JSON is. Hyperlambda's syntax is much simpler though, easier to read, and more easily
parsed than any of the alternatives, including YAML. To illustrate this let us look at some example
Hyperlambda.

```
.data
   item1:1
   item2:2
   item3:3

strings.concat
   get-value:x:@.data/*/item1
   get-value:x:@.data/*/item2
   get-value:x:@.data/*/item3
```

In the above Hyperlambda **[.data]** is a `Node`. This node has a name of _".data"_ and a null value.
In addition it has a list of children nodes being **[item1]**, **[item2]**, and **[item3]**. These children nodes
have values, that can be found to the right hand side of the `:`. A node resembles the following class in C#
or Java.

```csharp
class Node
{
    string Name;
    object Value;
    List<Node> Children;
}
```

The above example is _"pseudo code"_ intended to simplify understanding, but this is basically the main parts
of the `Node` class. If you compare the `Node` class to for instance JSON, you will see it has _one additional axiom_,
being an explicit children collection. JSON in such a regard is simpler, because it _only_ has a name and a value, in
addition to that in JSON the same name _cannot be repeated_ because JSON maps to fields on objects. Hence, substituting
Hyperlambda with JSON, would make things much more verbose, even though technically it _is_ possible. The same is
true for XML and YAML. Fundamentally Hyperlambda has only 3 tokens.

* A colon `:` separates a node's name from its value
* A carriage return ends the declaration of a node
* 3 additional spaces below a node declares its children collection

In addition Hyperlambda allows for declaring a node's value using the same semantics as a C# string. This
allows you to declare values with carriage returns, and any special character. As a final touch,
Hyperlambda also provides you with type support, allowing you to declare what type its value is.
Below is a Hyperlambda snippet that declares an `integer`, a `decimal`, and a `DateTime` value.

```
.data
   val1:int:5
   val2:decimal:5.5
   val3:date:"2021-01-01T23:59:00"
```

Type declarations are basically injected in between the node's name and its value, and are
referencing CLR types such as `System.DateTime`, `System.Decimal`, etc. The default type in Hyperlambda
if no type is explicitly declared is assumed to be string.
The typing system of Hyperlambda is crucial for what follows, and also makes it almost impossible
to substitute Hyperlamdba with JSON or YAML - In addition, substituting Hyperlambda with XML would
literally explode its verbosity, resulting in that the number of bytes required to represent the same
object in XML as you represent in Hyperlambda would probably increase the size of your files by one
order of magnitude. So Hyperlambda cannot easily be replaced, and it serves a very specific purpose.

## Executing Hyperlambda

If you break down the compilation process of for instance a C# method, you will see that the first
thing the compiler does, is to create a tree structure, or a graph object of your method. Below is
an example.

```csharp
if (foo)
{
   // Do something
}
else
{
   // Do something else
}
```

During compilation the above is broken down into a tree structure, where you have one root object,
being the method as a whole, and a list of children being the `if` and `else` parts in the above example.
This process is recursively applied for all of your C# code. As the compilation process is finished,
this temporary tree structure is discarded, and some sort of final executable is created as its result.
Hyperlambda is similar, except it skips the last parts, and ends up using this _"temporary tree structure"_
as its actual _"executable"_. Let's illustrate how the above code could be _"transpiled"_ into Hyperlambda
to clarify.

```
if
   foo
   .lambda
      // Do something
else
   // Do something else
```

The above is more or less the exact replica of the first C# code, except of course it is Hyperlambda.
As you execute the above code, what you're basically doing, is to provide the root `Node` as an executable
argument to Hyperlambda's **[eval]** slot, which again sequentially reads each child node of your execution node,
and unless the currently iterated child node starts with a period `.`, it is assumed to be a reference to
a _"slot"_. This slot is then _"signaled"_, implying some sort of CLR method on some class will be invoked.
This makes Hyperlambda super extendible, allowing you to extend it with your own C# methods as you see fit.
Below is an example.

```csharp
using magic.node;
using magic.signals.contracts;

namespace acme
{
    [Slot(Name = "foo")]
    public class Foo : ISlot
    {
        public void Signal(ISignaler signaler, Node input)
        {
            input.Value = true;
        }
    }
}
```

The above C# code creates a slot who's name is **[foo]** that you can invoke from your own
Hyperlambda code. Below is an example of consuming the above slot from Hyperlambda.

```
.result
if
   foo
   .lambda
      set-value:x:@.result
         .:[foo] is true
else
   set-value:x:@.result
      .:[foo] is false
```

The above code invokes your **[foo]** slot, and then the semantics of the **[if]** will check its first
argument after evaluating it, and if it's true, it will execute the **[.lambda]** node.
If **[foo]** is _not_ true, it will execute the **[else]** node. This process allows you to easily
extend Hyperlambda with your own custom slots, and in fact _everything_ in Hyperlambda is a slot -
Including the **[if]** and **[else]** parts from the above code. You can check out the code
for both of these two slots below to confirm that even the _"keywords"_ in Hyperlambda are in fact
implemented as _"slots"_.

* [The if slot](https://github.com/polterguy/magic.lambda/blob/master/magic.lambda/branching/If.cs)
* [The else slot](https://github.com/polterguy/magic.lambda/blob/master/magic.lambda/branching/Else.cs)

This makes Hyperlambda a DSL engine, or _"An engine to create your own Domain Specific Language"_.
Hence, the slots you create yourself is in no ways discriminated between that which you probably
perceive as _"keywords"_ in Hyperlambda - And you could replace the **[if]** slot quite easily with
your own custom implementation if you wanted. Or for that matter remove the **[if]** slot,
if you for some reasons don't want to have if statements in your own programming language.
Hence, Hyperlambda literally doesn't have keywords, only slots, and all slots are recursive in nature,
and lambda objects by themselves. Something you can verify by seeing how even the **[if]** slot
recursively invokes **[eval]** to evaluate its children.
This is true to such an extent that even what you'd imagine as _"operators"_ in traditional
programming languages are also slots. This has huge advantages, because it
allows you to declare your own _"operators"_, in addition to that Hyperlambda can easily be
traversed _semantically_, to see which operators it's using, and Hyperlambda files can also
easily be _"generated"_, by combining programming language fundamentals together, to create a
result of some sort - Which of course is the foundation for the _"CRUD"_ menu item in Magic.
If you find this structure to be weird, please realize the following.

> Hyperlambda is weird because it needs to be weird

## Variables

Hyperlambda _does not have variables_ - Or to be specific, _everything_ is a variable
in Hyperlambda. This is because of that Hyperlambda has the ability to change any node's value,
name, and/or children collection as it executes. Run the following code through for instance the _"Eval"_
menu item in Magic's dashboard to see this process.

```
.item1:foo
.item2:foo
.item3

set-value:x:@.item1
   .:bar

set-name:x:@.item2
   .:bar

add:x:@.item3
   .
      child1:value1
```

The above Hyperlambda changes the value of its first node, then it changes the name of its second node, for then
to finally add children nodes to its third node. This makes Hyperlambda
_extremely dynamic in nature_ - Much more dynamic than other dynamic programming languages, since the
code might change itself, as it is executing itself. The code is said to be
_"self evolving during its execution process"_. In fact, in Hyperlambda there is no differences between
creating code, modifying code, storing data, and executing code. These constructs are basically just aspects of the
same process in Hyperlambda, and of course the reason why it is so easy to create code that generates
code with Hyperlambda. Below is the result of executing the above Hyperlambda.

```
.item1:bar
bar:foo
.item3
   child1:value1
```

You can still provide _"data segments"_ in your code, which of course is crucial to hold
temporary variables as your code is executing. This is achieved by making sure you start your node's name
with a period (.). This works because the **[eval]** slot will ignore all nodes
having a name starting with a period, while all nodes not starting with a period will be
assumed to be slot invocations, and **[eval]** will try to signal these nodes as such.
Below is an example of a **[while]** snippet that increments some integer value, and iterates
500 times before ending its execution.

```
.no:int:500
while
   mt
      get-value:x:@.no
      .:int:0
   .lambda
      math.decrement:x:@.no
```

The **[mt]** slot above is an acronym for _"more than"_, and simply returns true as long as its value
is more than its second argument - And the **[math.decrement]** slot simply decrements the value of its
expression by one. This results in that the above **[.lambda]** object, which is an argument to the **[while]**
slot executes 500 times - Once for every value between 500 and 0. As **[mt]** returns false, the
while loop is stopped. The **[.no]** node above is a _data segment_.
Since Hyperlambda's **[eval]** slot is recursive in nature, this allows you to declare entire segments
of data using the same technique, without having to prefix children of data segments with a period. Below
is an example.

```
.data
   first_name:Thomas
   last_name:Hansen
   email:thomas@servergardens.com
// Do stuff with above data segment
```

The above **[.data]**  segment is ignored by **[eval]** and none of its children will be
signaled. Hence, inside of our data segment, we no longer need to prepend nodes' names with a period.

## Expressions

This is probably the most complex part of Hyperlambda, but if you have ever used XPath expressions,
it shouldn't be too problematic, since they are more or less similar in nature. An expression is basically
a _"pointer"_ into a sub-set of your node structure. For instance, the following
expression ...

```
../*/.data/*
```

... will return all children nodes of all nodes named **[.data]** that can be found as children of your root
node. This is because of that its first part `..` implies _"give me the root node"_. The second part `/*`
implies give me all its children. The third part `/.data` implies filter out all nodes not named _".data"_.
The last part `/*` implies give me all its children nodes again. This gives you _query capabilities_
into your node structure, allowing one node to reference other nodes. Combined with for instance
the **[get-value]** or the **[get-name]** slots, this allows you to retrieve any parts of any other nodes
in your tree. Below is an example.

```
.data:Howdy World
get-value:x:../*/.data
```

An expression is composed of iterators. An iterator is basically an `IEnumerable<Node>` function object,
where the result of the first iterator in the chain is applied as the input to the next iterator,
resulting in that the expression as a whole yields a list of nodes. The above expression being
the value of the **[get-value]** slot for instance has 3 iterators. Magic contains many
iterators, allowing you to query your node structure any ways you see fit. Further down you can find
the links to the reference documentation for these parts of Magic.

### Extrapolated expressions

Hyperlambda also allows you to nest expressions, or create extrapolated expressions. This is
quite useful since it allows you to parametrise expressions, such that parts of your expressions
are dynamically changing according to the value of a nested expression. To understand the idea
imagine the following.

```
.result
.arg1:foo2

.data
   foo1:John
   foo2:Thomas
   foo3:Peter

set-value:x:@.result
   get-value:x:@.data/*/{@.arg1}
```

The above basically substitutes the `{@.arg1}` parts of your expression with the
value of the node referenced by your `@.arg1` expression, before the outermost expression is
evaluated - Resulting in that the outermost expression becomes `@.data/*/foo2` before it is being
evaluated. This technique allows you to nest expressions as deep as you wish, and use as many
_"dynamic"_ segments as you wish in your expressions.

* [Read more about expressions, nodes and Hyperlambda](/documentation/magic.node/)
* [Read more about eval and its programming language constructs](/documentation/magic.lambda/)

## Modifying your tree

Hyperlambda contains a whole range of slots that allows you to dynamically modify your lambda
objects as they are executing. Below are the most important slots related to this.

* __[set-value]__ - Changes the value of a node
* __[set-name]__ - Changes the name of a node
* __[add]__ - Appends children to a node's children collection
* __[insert-before]__ - Injects a node _before_ some node
* __[insert-after]__ - Injects a node _after_ some node

All of the above slots requires a destination expression as their primary value, and
one or more arguments beings its _"source"_. Notice though that these destination expressions
can reference _multiple_ nodes, implying one invocation might in theory change multiple nodes.
Refer to [magic.lambda](/documentation/magic.lambda/) for details about how these slots works.

## Wrapping up

This was probably the hardest tutorial we've gone through so far, but once you understand
expressions, nodes, Hyperlambda, and its relationship to slots and signals - Everything becomes
easy. In this tutorial we covered the following subjects.

* Hyperlambda syntax
* The Node class
* Executing lambda objects or nodes
* Creating slots from C#
* Variables
* Expressions
* Modifying your lambda object

### Golly gosh this is weird!

Hyperlambda is _"weird"_, but it needs to be weird in order to facilitate for what it does.
Every time you think about how weird it is, and this bothers you, please realize that without
this _"weirdness"_, things such as the automatic creation of your CRUD backends, etc, would simply
not be possible. We didn't create it weird because we wanted it to be weird. We created it weird
because it _needed_ to be weird. To understand why it needs to be weird, please realise the following.

> Hyperlambda's purpose is to have your computer understand Hyperlambda

Whether or not you actually understand it is second priority. This trait of Hyperlambda
allows for the computer to create programs that runs on other computers, or itself for that matter -
And that is its purpose; **To replace the need for manually creating code**.

* Continue with [Loops and branching in Hyperlambda](/tutorials/loops-and-conditions/)
