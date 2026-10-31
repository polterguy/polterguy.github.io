---
title: "[system.plugin.execute]"
description: "system.plugin.execute is a slot in the system namespace of Magic Cloud. Loads, executes, and unloads a plugin in a single scope."
generated: true
llms: "guide"
slot_json: "/reference/slots/system/system.plugin.execute/slot.json"
---

`system.plugin.execute` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Loads, executes, and unloads a plugin in a single scope.

* **Value** (`plugin-assembly,binary-content`), required: Plugin assembly filename or assembly bytes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable body evaluated while the plugin is loaded. Can be repeated. |

### Guide

<!-- guide -->
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
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.system](/plugins/magic.lambda.system/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `system.plugin.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.plugin.execute",
  "description": "Loads, executes, and unloads a plugin in a single scope",
  "signature": {
    "input": {
      "kind": "plugin-assembly,binary-content",
      "description": "Plugin assembly filename or assembly bytes",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable body evaluated while the plugin is loaded",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    }
  }
}
```

</details>

---

[&larr; `system.os`](/reference/slots/system/system.os/) | [all `system.*` slots](/reference/slots/system/) | [`system.plugin.list` &rarr;](/reference/slots/system/system.plugin.list/)

