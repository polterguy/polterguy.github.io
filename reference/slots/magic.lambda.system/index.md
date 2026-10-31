---
title: magic.lambda.system slot reference
description: Every slot in magic.lambda.system with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.system](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.system). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.system](/plugins/magic.lambda.system/)._

## [system.compile]

Compiles C# code from child nodes into an assembly.

* **Returns**: Resolves to the compiled assembly bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[code]` | string | yes | C# source code to compile |
| `[assembly-name]` | string | yes | Name of the generated assembly |
| `[references]` | lambda | yes | Assembly references required by the compilation |

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
| `[working-directory]` | string | no | Working directory for the process |
| `[*]` | string | no | Single process argument |

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
| `[*]` | lambda | no | Executable body evaluated while the plugin is loaded |

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

