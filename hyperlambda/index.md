# Hyperlambda 101

Hyperlambda is similar to YAML. It therefor easily translates into a node structure,
where each node has a _"key"_, a _"value"_, and a bunch of _"children"_. This just
so happens to perfectly describe an execution syntax tree, where the name of a node
might reference a C# method, included into the core of the language using _"Super Signals"_.
Imagine the following piece of Hyperlambda code.

```
acme.foo
   first:7
   second:7
   third:7
```

The above basically becomes a reference to a C# class, which implements the `ISlot`
interface, where each of its children nodes are being passed into its `Signal` method
as arguments. Below is some C# code that illustrates how you could go about to
implement a _"slot"_ that is able to handle the above Hyperlambda invocation.

```csharp
using System;
using System.Linq;
using System.Collections.Generic;
using magic.node;
using magic.signals.contracts;

namespace acme
{
    [Slot(Name = "acme.foo")]
    public class Foo : ISlot
    {
        public void Signal(Node input)
        {
            input.Value = input.Children.Sum(x => x.Get<int>());
            input.Clear();
        }
    }
}
```

Assuming you have the above C# code in your application somehow, you can invoke
the Hyperlambda at the top, and your **[acme.foo]** invocation will return the
sum of all of its arguments, which for our example becomes 21. After evaluating
the above code, your result should resemble the following.

```
acme.foo:int:21
```

**Notice** - To _"register"_ your slots into Magic and make them available for
your Hyperlambda, you'll need to reference the assembly implementing your slot(s)
somehow into your _"magic.backend"_ project. Normally you'd create a new assembly
in the _"plugins"_ folder, create your slots in this assembly, and simply reference
your assembly into the _"magic.backend"_ project - And you'll have access to
it from your Hyperlambda.

## Evaluating custom Hyperlambda

Magic contains a Hyperlambda evaluator, where you can paste in Hyperlambda code,
to play around with. When Magic is running, you can access this
evaluator from the _"Evaluator"_ menu item. If you want to see all slots you
have at your disposal, you can make sure your cursor is at the beginning of
an empty line, and then click `CTRL+Space`. This pops up the autocompleter,
and gives you a list of all Hyperlambda _"keywords"_, or slots to be more accurate.

## Hyperlambda a DSL

At this point you probably realise that Magic and its Hyperlambda actually
is the perfect foundation for creating your own custom DSL, as 
in _"Domain Specific Language"_. And that would be a correct assessment.
Hyperlambda perfectly fits the requirements for creating your own high level
DSL programming languages, using the `ISlot` interface and its _"Super Signal"_
implementation. And in fact, the _"Crudifier"_ at its core is nothing but
an SQL DSL language implementation, of such a high level abstraction,
that the computer is able to automate the creation of the code needed
to wrap your database into HTTP REST CRUD endpoint(s).

[Home](/)
