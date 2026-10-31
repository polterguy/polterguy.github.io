---
title: "How to use [system.compile]"
description: "How to use [system.compile] - This method allows you to compile a piece of C# code and returns the assembly as a raw array of bytes."
generated: true
guide: true
---

This is the guide to [`system.compile`](/reference/slots/system/system.compile/), whose reference page has its arguments, constraints and declaration.

This method allows you to compile a piece of C# code and returns the assembly as a raw array of bytes. Example usage can be found below.

```
/*
 * Compiles a piece of C# and returns the compiled CLR assembky code as raw bytes.
 */
system.compile
   assembly-name:foo.dll
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
[Slot(Name = "foo")]
public class Foo : ISlot
{
   public void Signal(ISignaler signaler, Node input)
   {
      input.Value = "Foo was here!";
   }
}"
```

The slot takes three arguments being as follows;

* __[assembly-name]__ - The name of your assembly
* __[references]__ - Being what references your code requires to compile. Notice, these are taken from the current AppDomain's assemblies, and assumes you've already got the assembly somehow loaded into your AppDomain. If you need to add assemblies that doesn't exist in your AppDomain you can use **[system.plugin.load]** before you compile your code.
* __[code]__ - Your actual C# code

If you want to persist the created assembly to disc you can use the **[io.file.save.binary]** slot from the _"magic.lambda.io"_ project.

## Dependency Injection and your IoC container

Because the IoC DI container is built as your assembly starts, you cannot rely upon the DI container in your code the way you can in normal statically compiled code. This implies you'll have to use the _"service locator"_ pattern to resolve services in your C# code. The service locator pattern is considered an _"anti pattern"_, but there aren't really many options here.

Below is an example of some C# code dynamically instantiating your `IMagicConfiguration` service while creating a slot that returns a configuration value to the caller.

```csharp

// Example C# code creating a Hyperlambda slot.
using System;

using magic.node;
using magic.library;
using magic.signals.contracts;
using magic.node.contracts;

// Our slot class.
[Slot(Name = "foo")]
public class Foo : ISlot
{
    readonly IServiceProvider _services;

    public Foo(IServiceProvider services)
    {
        _services = services;
    }

    public void Signal(ISignaler signaler, Node input)
    {
        var configuration = (IMagicConfiguration)_services.GetService(typeof(IMagicConfiguration));
        input.Value = configuration["magic:smtp:host"];
    }
}
```

If you save the above code to _"/etc/foo.cs"_ you can compile it and save it using the following code.

```
/*
 * The following code compiles the "/etc/foo.cs" file and saves it as an assembly
 * in "/etc/foo.dll".
 */
io.file.load:/etc/foo.cs
system.compile
   references
      .:netstandard
      .:System.Runtime
      .:System.Console
      .:System.Private.Uri
      .:System.ComponentModel
      .:System.Private.CoreLib
      .:System.Net.Primitives
      .:magic.node
      .:magic.node.extensions
      .:magic.library
      .:magic.signals.contracts
   code:x:@io.file.load
   assembly-name:foo.dll

// Saving our compiled CLR assembly to '/etc/foo.dll'.
io.file.save.binary:/etc/foo.dll
   get-value:x:@system.compile
```
