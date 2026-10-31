---
title: "[python.execute]"
description: "python.execute is a slot in the python namespace of Magic Cloud. Runs a Python script or file in a subprocess and captures stdout, stderr, and exit code."
generated: true
llms: false
slot_json: "/reference/slots/python/python.execute/slot.json"
---

`python.execute` is a slot in the `python` namespace, in Hyperlambda, the language of Magic Cloud. Runs a Python script or file in a subprocess and captures stdout, stderr, and exit code.

* **Returns**: Returns stdout in value and stderr and exit code as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[code]` | string | no | Inline Python code to execute. |
| `[file]` | string | no | Python file to execute. |
| `[args]` | string\|lambda | no | Command-line arguments as a shell-like string or child values. |
| `[args]` / _any node name_ | string | no | Single command-line argument. Can be repeated. |
| `[stdin]` | string | no | Text written to standard input. |
| `[working-directory]` | string | no | Working directory for the Python process. |
| `[timeout]` | int | no | Execution timeout in seconds. Default: `30`. |

### Constraints

* **ExactlyOneOf**: Exactly one code source must be supplied (`[code]`, `[file]`)

Guide: [How to use [python.execute]](/plugins/magic.lambda.python/#how-to-use-pythonexecute)

### JSON declaration

This is the complete declaration of `python.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "python.execute",
  "description": "Runs a Python script or file in a subprocess and captures stdout, stderr, and exit code",
  "signature": {
    "children": {
      "code": {
        "type": "string",
        "kind": "python-code",
        "description": "Inline Python code to execute",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "file": {
        "type": "string",
        "kind": "python-file",
        "description": "Python file to execute",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "args": {
        "type": "string|lambda",
        "kind": "terminal-arguments",
        "description": "Command-line arguments as a shell-like string or child values",
        "required": false,
        "mode": "StructuredArguments",
        "cardinality": "ZeroOrOne",
        "role": "Arguments",
        "projection": "ArgumentBag",
        "children": {
          "*": {
            "type": "string",
            "kind": "terminal-argument",
            "description": "Single command-line argument",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Arguments",
            "projection": "Value"
          }
        }
      },
      "stdin": {
        "type": "string",
        "kind": "stdin-text",
        "description": "Text written to standard input",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "working-directory": {
        "type": "string",
        "kind": "folder-path",
        "description": "Working directory for the Python process",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "timeout": {
        "type": "int",
        "description": "Execution timeout in seconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "30",
        "role": "Option",
        "projection": "Value"
      }
    },
    "constraints": [
      {
        "description": "Exactly one code source must be supplied",
        "values": [
          "code",
          "file"
        ],
        "kind": "ExactlyOneOf"
      }
    ],
    "output": {
      "mode": "Both",
      "kind": "terminal-response,text",
      "description": "Returns stdout in value and stderr and exit code as child nodes"
    }
  }
}
```

</details>

---

[all `python.*` slots](/reference/slots/python/)

