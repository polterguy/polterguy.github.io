---
title: "[system.execute]"
description: "system.execute is a slot in the system namespace of Magic Cloud. Spawns a shell process with the given command and arguments and returns its captured output."
generated: true
llms: false
slot_json: "/reference/slots/system/system.execute/slot.json"
---

`system.execute` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Spawns a shell process with the given command and arguments and returns its captured output.

* **Value** (`terminal-command`), required: Command to execute
* **Returns**: Resolves to the standard output from the executed command

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | string\|lambda | no | Process arguments as a shell-like string or child values. |
| `[args]` / _any node name_ | string | no | Single process argument. Can be repeated. |
| `[working-directory]` | string | no | Working directory for the process. |

### Guide

[How to use `system.execute`](/plugins/magic.lambda.system/system.execute/)

### JSON declaration

This is the complete declaration of `system.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.execute",
  "description": "Spawns a shell process with the given command and arguments and returns its captured output",
  "signature": {
    "input": {
      "kind": "terminal-command",
      "description": "Command to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "args": {
        "type": "string|lambda",
        "kind": "terminal-arguments",
        "description": "Process arguments as a shell-like string or child values",
        "required": false,
        "mode": "StructuredArguments",
        "cardinality": "ZeroOrOne",
        "role": "Arguments",
        "projection": "ArgumentBag",
        "children": {
          "*": {
            "type": "string",
            "kind": "terminal-argument",
            "description": "Single process argument",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Arguments",
            "projection": "Value"
          }
        }
      },
      "working-directory": {
        "type": "string",
        "kind": "folder-path",
        "description": "Working directory for the process",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "terminal-response,text",
      "description": "Resolves to the standard output from the executed command"
    }
  }
}
```

</details>

---

[&larr; `system.debug`](/reference/slots/system/system.debug/) | [all `system.*` slots](/reference/slots/system/) | [`system.is-os` &rarr;](/reference/slots/system/system.is-os/)

