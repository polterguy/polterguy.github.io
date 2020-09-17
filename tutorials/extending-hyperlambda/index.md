# Extending Hyperlambda with C#

A 5 minute long read, about how you can extend Hyperlambda, with your own
C# methods. After all, what would a DLS engine be without the ability to
extend it with your own keywords?

What our previous [sending emails tutorial](/tutorials/send-email) tried
to hint at, is that Magic is more than CRUD. In this tutorial, we
will show you just that, by creating our own Hyperlambda keyword, that
invokes your own C# method, resulting in that Magic and Hyperlambda
perfectly ties into C#, and its possibilities effectively becomes
endless.

First expand your _"backend/slots/"_ folder, and create a new file,
and name it _"Add.cs_". Add the following content to it.

```csharp
using magic.node;
using magic.node.extensions;
using magic.signals.contracts;

namespace tutorials.examples
{
    [Slot(Name = "tutorials.add")]
    public class Add : ISlot
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

Congratulations, you have now created your first Hyperlambda
keyword. The above keyword, simply adds to integer values, and
returns the result. If you recompile your Magic backend, you can
immediately consume your keyword in an HTTP endpoint, by creating
a new file in your _"/modules/tutorials/"_ folder, and name your
file _"add.get.hl"_. Put the following content into your file.

```
.arguments
   arg1:int
   arg2:int
add:x:../*/tutorials.add
   get-nodes:x:@.arguments/*
tutorials.add
unwrap:x:+/*
return
   result:x:@tutorials.add
```

Then go to your endpoints, and invoke the file, and make sure
you pass in integer values for its _"arg1"_ and _"arg2"_ QUERY
parameters. Needless to say, but after invoking your endpoint,
you have the result of adding those two arguments.

## Custom slots

Fundamentally, there is _zero difference_ between the above
`ISlot` class you just created, and any other slot you invoke
using Hyperlambda - It's _the exact same thing_ in fact.

The way this works, is that as Magic starts, it will run
through your assembly, find all classes implementing the
`ISlot` interface, retrieve its `Slot` attribute's name
property, and use that as the _"key"_ to your slot. Later
as you invoke the slot in Hyperlambda, the key will be used
to retrieve an instance of your slot, and its `Signal`
method will be invoked.

If you want to create async slots, you'll have to
implement the `ISlotAsync` interface, and make sure your
prefix your slot's name with _"wait."_ - And yes, you can
of course implement _both_ interfaces on the same class,
and also have multiple `Slot` attributes, with different
names on the same class too. This allows you to create both
a synchronous version, and an async version, of the same
slot, on the same class. And in fact, this is the way
most slots in Magic are implemented.

## Expressions

So far, we have largely ignored lambda expressions.
However, now they become more important to understand. An
expression is basically any value of a node in Hyperlambda that
resembles the following.

```
.foo:x:@.arguments/*
```

The above expression, which is the same expression as the
one we used in our above **[get-nodes]** invocation, happens
to return all nodes that are inside of our **[.arguments]**
node. To translate it into humanly understandable language,
it becomes as follows.

> Find the first node who's name is '.arguments', then return that node's children to me

Inside of our C# slots again, we can evaluate such expressions
if we want to. The above `Get` method, in our C# slot, only returns
the raw value of our slot. But if you use its `GetEx` version instead,
all expressions will be evaluated, until we're left with a
non-expression value, and then that value will be returned.

This means that the following Hyperlambda

```
.arguments
   foo:int:5
get-value:x:@.arguments/*/foo
```

Will result in that the value of the **[get-value]** node, after
having been evaluated, will be `5`. To understand more about how
expressions works, in combination with nodes, and Hyperlambda's
typing system, you might benefit from reading the following.

* [magic.node reference documentation](/magic.node)

The above URL explains expressions, nodes, how they tie into
Hyperlambda, and how the typing system in Hyperlambda works.
