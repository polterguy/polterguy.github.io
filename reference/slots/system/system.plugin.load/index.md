---
title: "[system.plugin.load]"
description: "system.plugin.load is a slot in the system namespace of Magic Cloud. Loads a plugin assembly."
generated: true
llms: "guide"
slot_json: "/reference/slots/system/system.plugin.load/slot.json"
---

`system.plugin.load` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Loads a plugin assembly.

* **Value** (`plugin-assembly,binary-content`), required: Plugin assembly filename or assembly bytes

### Guide

<!-- guide -->
This guide covers [`system.plugin.load`](/reference/slots/system/system.plugin.load/), [`system.plugin.unload`](/reference/slots/system/system.plugin.unload/) together.

These slots allow you to load and unload assemblies and instantiate any slots found in it, and such dynamically during runtime changes your available slots. If you imagine you saved the above resulting compiled assembly as _"/etc/foo.dll"_, and you want to load it as a plugin, you could use code resembling the following.

```
system.plugin.load:/etc/foo.dll
```

Once the above code has executed you will have a native C# Hyperlambda slot called **[foo]** that you can use. Plugins loaded this way will stay in memory as a part of your AppDomain until either the process restarts, and/or you explicitly unload the plugin - Implying if your process restarts you'll need to ensure the plugin is reloaded again if you wish to continue using it. Dynamically loaded plugins will _not_ be automatically reloaded in any ways.

To unload the plugin after having used the assembly and it is no longer required, you should use **[system.plugin.unload]** to unload the assembly. If you recompile some C# code using the same assembly name this will be automatically done for you by consecutive invocations to **[system.plugin.load]** as long as the **[assembly-name]** argument is the same (case sensitive).

If you unload an assembly previously loaded it will be collected by the garbage collector automatically as long as you don't have references to it from another native assembly.

You can also load an assembly as raw bytes, such as the following example illustrates.

```
/*
 * Compiles a snippet of C# code down to a library,
 * for then to dynamically load it as a plugin.
 */
system.compile
   references
      .:netstandard
      .:System.Runtime
      .:System.Private.CoreLib
      .:magic.node
      .:magic.node.extensions
      .:magic.signals.contracts
   code:@"

// Example C# code creating a Hyperlambda slot.
using System;
using magic.node;
using magic.node.extensions;
using magic.signals.contracts;

// Our slot class.
[Slot(Name = "foo")]
public class Foo : ISlot
{
   public void Signal(ISignaler signaler, Node input)
   {
      input.Value = $"Hi {input.GetEx<string>()}, how may I assist you?";
   }
}"
   assembly-name:foo.dll

// Loading assembly from raw bytes now that we've created it.
system.plugin.load:x:@system.compile

// Executing [foo] slot now dynamically injected into AppDomain.
.name:John Doe
foo:x:@.name

// Unloading plugin.
system.plugin.unload:foo.dll
```

Notice that in the last example above, we never actually save the assembly, but load it as a plugin from the raw `byte[]` returned from the **[system.compile]** invocation allowing you to dynamically compile and execute C# code without ever having to actually save the compiled result as a dll on disc. You still have to unload the assembly from your AppDomain using **[system.plugin.unload]**.

Also notice that the name of the assembly is not necessary the path of the assembly, but determined from **[assembly-name]**, allowing you to at least in theory have an assembly with _"/foo.dll"_ as its path, but _"bar.dll"_ being its name - Implying to unload the assembly you'll need to unload it as _"bar.dll"_, and listing it will return _"bar.dll"_ - While the physical location on disc of your assembly is _"/foo.dll"_.

Implying the assembly's name and its filename might differ.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `system.plugin.load`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.plugin.load",
  "description": "Loads a plugin assembly",
  "signature": {
    "input": {
      "kind": "plugin-assembly,binary-content",
      "description": "Plugin assembly filename or assembly bytes",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `system.plugin.list`](/reference/slots/system/system.plugin.list/) | [all `system.*` slots](/reference/slots/system/) | [`system.plugin.unload` &rarr;](/reference/slots/system/system.plugin.unload/)

