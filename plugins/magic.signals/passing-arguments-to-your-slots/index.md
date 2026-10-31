---
title: "Passing arguments to your slots"
description: "Passing arguments to your slots - The Node class provides a graph object for you, allowing you to automagically pass in any arguments you wish."
generated: true
---

This page is part of the [magic.signals](/plugins/magic.signals/) documentation.

The Node class provides a graph object for you, allowing you to automagically pass in any arguments you wish.
Notice, the whole idea is to de-couple your assemblies, hence you shouldn't really pass in anything but native types,
such as for instance `System.String`, `System.DateTime`, integers, etc. However, most complex POD structures, can also
easily be represented using this `Node` class.

The Node class is basically a name/value/children graph object, where
the value can be any object, the name a string, and children is a list of children Nodes. In such a way, it provides
a more C# friendly graph object, kind of resembling JSON, allowing you to internally within your assemblies, pass
in a Node object as your parameters from the point of your signal, to the slot where you handle the signal.

The `Node` POCO class again, is a bi-directional POD instance, allowing you to both pass arguments _into_ the
slot, in addition to having the slot _return_ values back to the caller.

If you invoke `Signal` or `SignalAsync` from C#, you can optionally pass in a function object that will
be executed after the signal has been executed. This is useful for cases where you're creating an async signal
invocation, but not invoking it immediately, and rather returning it as a `Task` to some other parts of your
system, to ensure something occurs _after_ the signal has been executed. Below is an example.

```csharp
var args = new Node();
return signaler.SignalAsync("foo.bar", args, () => { /* ... This will happen AFTER execution of signal ... */ });

```

---

[&larr; Active Events or Super Signals internals](/plugins/magic.signals/active-events-or-super-signals-internals/) | [all of magic.signals](/plugins/magic.signals/)
