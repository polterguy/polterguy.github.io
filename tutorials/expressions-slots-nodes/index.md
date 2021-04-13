
# Expressions, slots, and nodes

Fundamentally Hyperlambda is just a text representation of a tree structure, the same way XML, YAML and JSON is.
Hyperlambda's syntax though is both simpler, more humanly readable, and more easily parsed than any of the
alternatives - Including YAML. To illustrate this let us look at some example Hyperlambda.

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

In the above Hyperlambda the **[.data]** parts is a `Node`. This node has a name of _".data"_ and a null value.
In addition it has a list of children nodes being **[item1]**, **[item2]** and **[item3]**. These children nodes
have values though, which can be found to the right hand side of the `:` parts. To understand this, realise that
the `Node` class again looks roughly like the following.

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
addition to that in JSON the same name _cannot be repeated_ because JSON maps to fields on classes - So substituting
Hyperlambda with JSON, would make things much more verbose, even though technically it _is_ possible. The same is
true for XML and YAML.

Fundamentally Hyperlambda has only 3 tokens.

* A colon `:` separates a node's name from its value
* A carriage return ends the declaration of a node
* 3 additional spaces below a node declares its children collection

In addition Hyperlambda allows for declaring node's values using the same semantics as a C# string, which
allows you to declare values with carriage returns, and other special characters. As a final touch,
Hyperlambda also allows you to declare _types_, allowing you to declare what type its value parts is.
Below is a Hyperlambda snippet that declares an `integer`, a `decimal`, and a `DateTime` value.

```
.data
   val1:int:5
   val2:decimal:5.5
   val3:date:"2021-01-01T23:59:00"
```

Type declarations are basically injected in between the node's name and its value, and are simply
references to CLR types such as `System.DateTime`, `System.Decimal`, etc. The default type of no
type is explicitly supplied is string.

The typing system of Hyperlambda is crucial for what follows, and also makes it almost impossible
to substitute Hyperlamdba with JSON or YAML - In addition, substituting Hyperlambda with XML, would
literally explode its verbosity, resulting in that the number of bytes required to represent the same
object in XML as you represent in Hyperlambda, would probably increase the size of your files by one
order of magnitude, possibly more. So Hyperlambda cannot easily be replaced, and it serves
a _very specific purpose_, which you can read about in what follows.

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
As you execute the above code, what you're basically doing, is to provide the root `Node` as an argument
to Hyperlambda's **[eval]** slot, which again sequentially reads each child node of your execution node,
and unless the node starts with a period `.`, it is assumed to be a reference to a _"slot"_. This slot
is then _"signaled"_, implying some sort of CLR method on some class will be invoked. This makes Hyperlambda
super extendible, allowing you to extend it with your own C# methods as you see fit. Below is an example.

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
for both of these two slots below to confirm that even the _"keywords"_ in Hyperlambda are just simple
slots.

* [The if slot](https://github.com/polterguy/magic.lambda/blob/master/magic.lambda/branching/If.cs)
* [The else slot](https://github.com/polterguy/magic.lambda/blob/master/magic.lambda/branching/Else.cs)

This makes Hyperlambda a DSL engine, or _"An engine to create your own Domain Specific Language"_.
Hence, the slots you create yourself is in no ways discriminated between that which you probably
perceive as _"keywords"_ in Hyperlambda - And you could replace the **[if]** slot quite easily with
your own custom implementation if you wanted. Or for that matter simply remove the **[if]** slot,
if you for some reasons don't want to have if statements in your own programming language.

Hence, Hyperlambda _doesn't have keywords_, only slots, and all slots are recursive in nature,
and lambda objects by themselves. Something you can verify by seeing how even the **[if]** slot
recursively invokes **[eval]** to evaluate its children.

## Variables

Hyperlambda literally _does not have variables_ - Or to be specific, _everything_ is a variable
in Hyperlambda. This is because of thet Hyperlambda has the ability to change any node's value,
name, and/or children collection. Run the following code through for instance the _"Evaluator"_
in Magic's dashboard to see this process.

```
.item1:foo
.item2:foo
set-value:x:@.item1
   .:bar
set-name:x:@.item2
   .:bar
```

The above Hyperlambda changes the value of one node, and the name of another node. This makes Hyperlambda
_extremely dynamic in nature_ - Much more dynamic than other dynamic programming languages, since the
code might change itself, during the execution of itself. The code is _"self evolving during its execution process"_.

However, you can still provide _"data segments"_ in your code, which of course is crucial to hold
temporary variables as your code is executing. This is achieved by making sure you start your node's name
with a period `.` - Which only works because the **[eval]** keyword will simply ignore all nodes
starting with a period in their names. Below is an example of a **[while]** snippet that increments
some integer value, and iterates 500 times before ending its iteration.

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
slot executes 500 times - Once for every value between 500 and 0. As the **[mt]** returns false, the
while loop is stopped. The **[.no]** node above is said to be a _data segment_.

> Every node starting with a period (.) is ignored by the Hyperlambda execution engine, and assumed to be a data node

Since the Hyperlambda **[eval]** slot is recursive in nature, this allows you to declare entire segments
of data using the same technique, without having to prefix children of data segments with a period. Below
is an example.

```
.data
   first_name:Thomas
   last_name:Hansen
   email:thomas@servergardens.com
// Do stuff with above data segment
```

Since the above **[.data]**  segment is ignored by **[eval]** as a whole, none of its children will be
raised as signals, and inside of our data segment, we no longer need to prepend nodes' names with a `.`.

## Expressions

This is probably the most complex part of Hyperlambda, but if you have ever used XPath expressions,
it shouldn't be too problematic, since they're more or less similar in nature. An expression is basically
a _"pointer"_ into a sub-set hierarchy of your node structure. For instance, the following
expression ...

```
../*/.data/*
```

... will return all children nodes of all nodes named **[.data]** that can be found as children of your root
node. This is because of that its first part `..` implies _"give me the root node"_. The second part `/*`
implies give me all its children. The third part `/.data` implies filter out all nodes not named _".data"_.
The last part `/*` implies give me all its children nodes again. This gives you _query capabilities_
into your node structure, allowing one node to reference other nodes. Combined with for instance
the **[get-value]** or the **[get-name]** slots, this allows you to retrieve any parts of ay other nodes
in your tree. Below is an example.

```
.data:Howdy World
get-value:x:../*/.data
```

An expression is composed of iterators, which are basically `IEnumerable<Node>` function objects,
where the result of the first iterator is applied as the input of the next iterator in a chain,
resulting in that the expression as a whole yields a list of nodes. The above expression being
the value of the **[get-value]** slot for instance has 3 iterators.

* [Read more about expressions, nodes and Hyperlambda](/documentation/magic.node/)
* [Read more about eval and the language constructs](/documentation/magic.lambda/)

## Wrapping up

This was probably the hardest tutorial we've gone through so far - But once you understand
expressions, nodes, Hyperlambda, and its relationship to slots and signals - Everything becomes
easy. In this tutorial we covered the following subjects.

* Hyperlambda syntax
* The Node class
* Executing lambda objects or nodes
* Creating slots from C#
* Variables
* Expressions

Hyperlambda is _"weird"_, but it needs to be weird, in order to facilitate for that which it does.
Every time you think about how weird it is, and this bothers you, please realise that without
this _"weirdness"_, things such as the automatic generating of your HTTP backends, etc, would simply
not be possible. I didn't create it weird because I wanted it to be weird, I created it weird
because it _needed_ to be weird.

* [Documentation](/documentation/)
