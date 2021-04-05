# Magic Signals

Magic Signals is a _"Super Signals"_ implementation for .Net Core built on top of [Magic Node](https://github.com/polterguy/magic.node),
allowing you to invoke functions from one assembly in another assembly without having any direct references between the projects.

## Rationale

Below you can find a couple of articles written about the idea by yours truly.

* [Super Signals - DZone](https://dzone.com/articles/super-signals-in-aspnet-core)
* [Super Scalable Software Systems](https://dzone.com/articles/the-http-protocol-and-super-scalable-software-syst)

The above is made possible by always having a YALOA, allowing us to invoke methods in classes to the caller, through a _"magic string"_,
which references a type, in a dictionary, where the string is its key, and the types are dynamically loaded during startup
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
var args = new Node();
signaler.Signal("foo.bar", args);

/*
 * The value of args is now 42.
 */
Assert.Equal(42, args.Value);
```

Notice that there are no shared types between the invoker and the handler, and there are no references necessary to
be shared between these two assemblies. This results in an extremely loosely coupled plugin architecture, where you can
dynamically add any plugin you wish into your AppDomain, by simply referencing whatever plugin assembly you
wish to bring into your AppDomain, and immediately start consuming your plugin's functionality - Or dynamically loading
it during runtime for that matter, resulting in that you instantly have access to its slots, without needing to create
cross projects references in any ways.

This results in an extremely loosely coupled architecture of related components, where any one component can easily be
exchanged with any other component, as long as it is obeying by the implicit interface of the component you're replacing.
Completely eliminating _"strongly typing"_, making interchanging components with other components equally simply in a
static programming language such as the .Net CLR as providing a function object in JavaScript. In many ways, this
results in having all the advantages from a functional programming language in a static programming language - Allowing
you to choose which paradigm you want to use, based upon individual use cases, and not having the language and platform
dictate your choices in these regards.

The Magic Signals implementation uses `IServiceProvider` to instantiate your above `FooBar` class when it
wants to evaluate your slot. This makes it behave as a good IoC citizen, allowing you to pass in for instance
interfaces into your constructor, and have the .Net Core dependency injection automatically create objects
of whatever interface your slot implementation requires.

There is also an `async` interface, which allows you to declare async slots, transparently letting the runtime
choose which implementation to use, depending upon whether or not it is currently in an `async` execution context
or not. Below you can see how to accomplish the same as above, except this time the slot will be invoked within
an `async` context.

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

The above simple example is probably not that useful to implement as an `async` slot, but for other parts of your code,
where you for instance are accessing sockets, HTTP connections, or the file system for that matter - Creating
async slots will have huge advantages for your application's ability to scale, and handle multiple simultaneous
users and connections. The runtime will _"automagically"_ choose the correct implementation, being synchronous or
asynchronous, depending upon which execution context the execution object currently is within.

## Passing arguments to your slots

The Node class provides a graph object for you, allowing you to automagically pass in any arguments you wish.
Notice, the whole idea is to de-couple your assemblies, hence you shouldn't really pass in anything but _"native types"_,
such as for instance `System.String`, `System.DateTime`, integers, etc. However, most complex POD structures, can also
easily be represented using this `Node` class. The Node class is basically a name/value/children graph object, where
the value can be any object, the name a string, and children is a list of children Nodes. In such a way, it provides
a more C# friendly graph object, kind of resembling JSON, allowing you to internally within your assemblies, pass
in a Node object as your parameters from the point of your signal, to the slot where you handle the signal.
The `Node` POCO class again, is a dual direction POD instance, allowing you to both pass arguments _into_ the
slot, in addition to having the slot _return_ values back to the caller.

## Magic Signals a DSL

A lot of the idea behind Magic Signals is that combined with [Magic Node](https://github.com/polterguy/magic.node),
and especially its ability to parse _"Hyperlambda"_, it becomes a very good foundation for a DSL, or a Domain Specific
programming Language implementation, allowing you to easily create your own programming languages, and keywords,
based upon Hyperlambda syntax trees.

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.
