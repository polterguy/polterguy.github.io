
# Magic Signals

[![Build status](https://travis-ci.com/polterguy/magic.signals.svg?master)](https://travis-ci.com/polterguy/magic.signals)

Magic Signals is a _"Super Signals"_ implementation for .Net Core built on top of [Magic Node](https://github.com/polterguy/magic.node),
allowing you to invoke functions from one assembly in another assembly without having any direct references between the projects.

## Rationale

Below you can find a couple of articles written about the idea by yours truly.

* [Super Signals - DZone](https://dzone.com/articles/super-signals-in-aspnet-core)
* [Super Scalable Software Systems](https://dzone.com/articles/the-http-protocol-and-super-scalable-software-syst)

The above is made possible by always having a YALOA, allowing us to invoke methods in classes to the caller, through a _"magic string"_,
which references a type, in a dictionary, where the string is its key, and the types are dynamically load up during startup
of your AppDomain. Imagine the following code.

```csharp
[Slot(Name = "foo.bar")]
public class FooBar : ISlot
{
    public void Signal(ISignaler signaler, Node input)
    {
        input.Value = 42;
    }
}
```

The above declares a _"slot"_ for the signal **[foo.bar]**. In any other place in our AppDomain we can use an `ISignaler`
instance to Signal the above slot by using something such as the following.

```csharp
/*
 * This will invoke our Signal method above.
 */
var pars = new Node("foo.bar");
signaler.Signal(pars);

/*
 * The value of pars is now 42.
 */
Assert.Equal(42, pars.Value);
```

Notice that there are no shared types between the invoker and the handler, and there are no references necessary to
be shared between these two assemblies. This results in an extremely loosely coupled plugin architecture, where you can
dynamically add any plugin you wish into your AppDomain, by simply referencing whatever plugin assembly you
wish to bring into your AppDomain, and immediately start consuming your plugin's functionality - Or dynamically loading
it during runtime for that matter, resulting in that you instantly have access to its slots, without needing to create
cross projects references in any ways.

The Magic Signals implementation uses `IServiceProvider` to instantiate your above `FooBar` class when it
wants to evaluate your slot. This makes it behave as a good IoC citizen, allowing you to pass in for instance
interfaces into your constructor, and have the .Net Core dependency injection automatically create objects
of whatever interface your slot implementation requires.

```csharp
[Slot(Name = "foo.bar")]
public class FooBar : ISlotAsync
{
    public Task SignalAsync(ISignaler signaler, Node input)
    {
        input.Value = 42;
        await Task.Yield();
    }
}
```

It's a common practice to implements slots that recursively invokes other slots, by combining the above two constructs, into
one single class, using two different names for your slots, depending upon whether or not they're async or not. Below is an
example.

```csharp
[Slot(Name = "foo.bar")]
public class FooBar : ISlot, ISlotAsync
{
    // Sync version.
    public void Signal(ISignaler signaler, Node input)
    {
        input.Value = 42;
    }

    // Async version.
    public Task SignalAsync(ISignaler signaler, Node input)
    {
        input.Value = 42;
        await Task.Yield();
    }
}
```

## Passing arguments to your slots

The Node class provides a graph object for you, allowing you to automagically pass in any arguments you wish.
Notice, the whole idea is to de-couple your assemblies, hence you shouldn't really pass in anything but _"native types"_,
such as for instance `System.String`, `System.DateTime`, integers, etc. However, most complex POD structures, can also
easily be represented using this `Node` class. The Node class is basically a name/value/children graph object, where
the value can be any object, the name a string, and children is a list of children Nodes. In such a way, it provides
a more C# friendly graph object, kind of resembling JSON, allowing you to internally within your assemblies, pass
in a Node object as your parameters from the point of your signal, to the slot where you handle the signal.

## Magic Signals a DSL

A lot of the idea behind Magic Signals is that combined with [Magic Node](https://github.com/polterguy/magic.node),
and espcially its ability to parse _"Hyperlambda"_, it becomes a very good foundation for a DSL, or a Domain Specific
programming Language implementation, allowing you to easily create your own programming languages, and keywords,
based upon Hyperlambda syntax trees.
