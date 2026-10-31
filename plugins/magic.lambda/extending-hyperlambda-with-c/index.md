---
title: "Extending Hyperlambda with C#"
description: "Extending Hyperlambda with C# - To understand the relationship between C# and Hyperlambda, it might be beneficial for you to analyze the following code."
generated: true
---

This page is part of the [magic.lambda](/plugins/magic.lambda/) documentation.

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

---

[&larr; Hyperlambda structure](/plugins/magic.lambda/hyperlambda-structure/) | [all of magic.lambda](/plugins/magic.lambda/)
