# Hyperlambda 101

Hyperlambda is similar to YAML. It therefor easily translates into a node structure,
where each node has a _"key"_, a _"value"_, and a bunch of _"children"_. This just
so happens to perfectly describe an execution syntax tree, where the name of a node
might reference a C# method, included into the core of the language using _"Super Signals"_.
Imagine the following piece of Hyperlambda code.

```
acme.foo
   first:int:7
   second:int:7
   third:int:7
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
        }
    }
}
```

Assuming you have the above C# code in your application somehow, you can invoke
the Hyperlambda at the top, and your **[acme.foo]** invocation will return the
sum of all of its arguments, which for our example becomes 21.

## Evaluating custom Hyperlambda

Magic contains a Hyperlambda evaluator, where you can paste in Hyperlambda code,
to play around with it yourself. When Magic is running, you can access this
evaluator from the _"Evaluator"_ menu item.

[Home](/)
