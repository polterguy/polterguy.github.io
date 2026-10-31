---
title: magic.lambda.system
moved_anchors: {"how-to-use-systemcompile": "/plugins/magic.lambda.system/system.compile/", "how-to-use-systemdebug": "/plugins/magic.lambda.system/system.debug/", "how-to-use-systemexecute": "/plugins/magic.lambda.system/system.execute/", "how-to-use-systempluginload-and-systempluginunload": "/plugins/magic.lambda.system/system.plugin.load/", "systempluginexecute": "/plugins/magic.lambda.system/system.plugin.execute/", "systempluginlist": "/plugins/magic.lambda.system/system.plugin.list/"}
---

This project contains _"system slots"_ to be able to invoke system commands, and/or dynamically compile and load plugins, etc. More specifically the project contains the following slots.

* __[\[system.compile\]](/plugins/magic.lambda.system/system.compile/)__ - Compiles a piece of C# code and returns the result as raw bytes
* __[\[system.plugin.load\]](/plugins/magic.lambda.system/system.plugin.load/)__ - Loads the specified assembly and initialises any slots found in it
* __[\[system.plugin.unload\]](/plugins/magic.lambda.system/system.plugin.load/)__ - Unloads a previously loaded plugin assembly and unregister any slots
* __[\[system.plugin.execute\]](/plugins/magic.lambda.system/system.plugin.execute/)__ - Short hand combining load with unload and a lambda object
* __[\[system.plugin.list\]](/plugins/magic.lambda.system/system.plugin.list/)__ - Lists all dynamically loaded plugins
* __[\[system.execute\]](/plugins/magic.lambda.system/system.execute/)__ - Execute the specified command returning the result to caller
* __[\[system.debug\]](/plugins/magic.lambda.system/system.debug/)__ - Evaluates a lambda object while recording every slot invocation, and returns the recording
* __[\[system.os\]](/plugins/magic.lambda.system/system.os/)__ - Returns description of your operating system
* __[\[system.is-os\]](/plugins/magic.lambda.system/system.is-os/)__ - Returns true if your underlying operating system is of the specified type

The most important feature of this project is probably that it gives you the ability to dynamically compile C# code, persist to an assembly/dll, and dynamically load this assembly as if it was a _"plugin"_.


## Querying operating system version

In addition to the above slots this project also contains the following slots.

* __[\[system.os\]](/plugins/magic.lambda.system/system.os/)__ - Returns description of your operating system
* __[\[system.is-os\]](/plugins/magic.lambda.system/system.is-os/)__ - Returns true if your underlying operating system is of the specified type

The last slot above takes an argument such as _"Windows"_, _"OSX_, _"Linux"_, etc, and will return true
of the operating system you are currently running on belongs to the specified family of operating systems.
Below is example usage of both.

```
system.is-os:OSX
system.os
```
