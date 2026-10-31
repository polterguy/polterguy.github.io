---
title: system.* slots
description: The 9 slots named system.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [system.compile]

Compiles C# code from child nodes into an assembly.

* **Returns**: Resolves to the compiled assembly bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[assembly-name]` | string | yes | Name of the generated assembly. |
| `[code]` | string | yes | C# source code to compile. |
| `[references]` | lambda | yes | Assembly references required by the compilation. |
| `[references]` / _unnamed child node_ | string | yes | Assembly reference. Can be repeated. |

Guide: [How to use [system.compile]](/plugins/magic.lambda.system/#how-to-use-systemcompile)

## [system.debug]

Evaluates the child lambda while recording every slot invocation, returning the recording.

* **Returns**: Resolves to one node per executed slot, each with [slot], [path], [elapsed] and [lambda] being the entire lambda object after that slot was invoked

Guide: [How to use [system.debug]](/plugins/magic.lambda.system/#how-to-use-systemdebug)

## [system.execute]

Spawns a shell process with the given command and arguments and returns its captured output.

* **Value** (`terminal-command`), required: Command to execute
* **Returns**: Resolves to the standard output from the executed command

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | string\|lambda | no | Process arguments as a shell-like string or child values. |
| `[args]` / _any node name_ | string | no | Single process argument. Can be repeated. |
| `[working-directory]` | string | no | Working directory for the process. |

Guide: [How to use [system.execute]](/plugins/magic.lambda.system/#how-to-use-systemexecute)

## [system.is-os]

Returns true if the current operating system matches the specified platform.

* **Value** (`os-name`), required: Operating system platform name to compare against, typically WINDOWS, LINUX, OSX, or FREEBSD
* **Returns**: Returns true if the current operating system matches the supplied platform name

## [system.os]

Returns a description of the current operating system.

* **Returns**: Resolves to the current operating system name

## [system.plugin.execute]

Loads, executes, and unloads a plugin in a single scope.

* **Value** (`plugin-assembly,binary-content`), required: Plugin assembly filename or assembly bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable body evaluated while the plugin is loaded. Can be repeated. |

Guide: [How to use [system.plugin.execute]](/plugins/magic.lambda.system/#systempluginexecute)

## [system.plugin.list]

Lists dynamically loaded plugins.

* **Returns**: Returns one child node per dynamically loaded plugin name

Guide: [How to use [system.plugin.list]](/plugins/magic.lambda.system/#systempluginlist)

## [system.plugin.load]

Loads a plugin assembly.

* **Value** (`plugin-assembly,binary-content`), required: Plugin assembly filename or assembly bytes

Guide: [How to use [system.plugin.load]](/plugins/magic.lambda.system/#how-to-use-systempluginload-and-systempluginunload)

## [system.plugin.unload]

Unloads a plugin assembly.

* **Value** (`plugin-assembly-name`), required: Assembly name to unload

Guide: [How to use [system.plugin.unload]](/plugins/magic.lambda.system/#how-to-use-systempluginload-and-systempluginunload)

