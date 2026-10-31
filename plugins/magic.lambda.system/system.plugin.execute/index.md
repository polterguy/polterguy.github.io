---
title: "How to use [system.plugin.execute]"
description: "How to use [system.plugin.execute] - This is a short hand slot for dynamically loading a plugin and executing a lambda object with the plugin loaded, for then to automatically unload the plugin at the end of the scope."
generated: true
guide: true
---

The reference page of [`system.plugin.execute`](/reference/slots/system/system.plugin.execute/) has its arguments, constraints and declaration.

This is a short hand slot for dynamically loading a plugin and executing a lambda object with the plugin loaded, for then to automatically unload the plugin at the end of the scope. Below is an example of usage that dynamically compiles some C# code that creates a slot, for then to executing a lambda object having access to this slot, and finish the execution with automatically cleaning up and unloading the dynamically added plugin.

```
/*
 * Compiles a snippet of C# code down to a library,
 * for then to dynamically load it as a plugin.
 *
 * This particular code creates a slot, but you can create any
 * code you wish, and it doesn't have to be Hyperlambda related.
 */
system.compile
   references
      .:netstandard
      .:System.Runtime
      .:System.Private.CoreLib
      .:magic.node
      .:magic.signals.contracts
   code:@"

// Example C# code creating a Hyperlambda slot.
using System;
using magic.node;
using magic.signals.contracts;

// Our slot class.
[Slot(Name = "bar")]
public class Bar : ISlot
{
   public void Signal(ISignaler signaler, Node input)
   {
      input.Value = "Hello from C#";
   }
}"
   assembly-name:bar.dll

// Loading assembly now that we've created it.
system.plugin.execute:x:@system.compile

   // Invoking dynamically created C# slot.
   bar

/*
 * Now the [bar] slot is no longer available
 * since the assembly has been unloaded due to
 * having gone out of scope.
 */
system.plugin.list
```

This slot is probably the closest you come to being able to using C# as a dynamic _"scripting language"_, allowing you to use it more like an interpreted language than a compiled language - Even though internally it's actually compiled to IL code and executed as such - Only the loading of the assembly resulting from the compilation process is 100% dynamic and automatic, including the cleaning up and unloading of the assembly from the AppDomain once the code has been executed.

This slot accepts either a string or a byte array. If you give it a string, it assumes your string is a relative path to an assembly on disc. If you provide it with a byte array, it assumes it's your raw assembly content. In such a regard it works similarly to **[system.plugin.load]**.
