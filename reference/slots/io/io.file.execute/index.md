---
title: "[io.file.execute]"
description: "io.file.execute is a slot in the io namespace of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.execute/slot.json"
---

`io.file.execute` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments].

* **Value** (`hyperlambda-file`), required: File path to execute
* **Returns**: Resolves to the executed file's value result and any returned child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the executed file as a child of [.arguments]. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the executed Hyperlambda file. Can be repeated. |

### Guide

<!-- guide -->
Executes the specified Hyperlambda file. Just like when evaluating a dynamic slot, you can
pass in an **[.arguments]** node to the file, which will be considered arguments to your file.
Hence, this slot allows you to invoke a file, as if it was a dynamically created slot, and there
is no semantic difference really between this slot and **[signal]** from the _magic.lambda.slots_
project.

```
io.file.execute:/misc/some-hyperlambda-file.hl
```

#### Executing files from whitelisted code

Both slots obey the rules of **[whitelist]** invocations from magic.lambda, which lets you decide exactly which
files some partially untrusted code may execute, by pinning the path in the whitelist's **[vocabulary]**.

```
whitelist

   vocabulary
      execute-file:/modules/reports/top-customers.hl
      io.file.load:/modules/reports/top-customers.hl

   .lambda

      // Allowed, since the path is pinned in the vocabulary.
      execute-file:/modules/reports/top-customers.hl

      // Throws, since no other file is pinned.
      execute-file:/modules/reports/payroll.hl
```

Once a file has been admitted this way, the whitelist no longer applies to the statements _inside_ that file,
exactly as it does inside a dynamic slot created with **[slots.create]**. The file can therefore use slots such
as **[data.connect]**, which the code that executed it was never allowed to invoke. This is how you give
untrusted code access to complex business logic, without giving it raw access to the databases, files and
APIs the logic uses - you write and review the file, and you grant the file, not the slots it invokes. The
code inside the file is trusted, so it must validate its own arguments, and it must never execute code that
its caller supplied. Notice that **[io.file.load]** is a separate slot with a separate pin, which you add
if the caller should be allowed to read the file's source, for instance to learn which arguments it takes.
See the [Sandbox API generator](/dashboard/endpoint-generator/#business-logic-without-raw-access) for a
complete example, with a wizard that writes these lines for you.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `io.file.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.execute",
  "description": "Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]",
  "signature": {
    "input": {
      "kind": "hyperlambda-file",
      "description": "File path to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Named argument passed to the executed file as a child of [.arguments]",
        "required": false,
        "mode": "Arguments",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "lambda-result",
      "description": "Resolves to the executed file's value result and any returned child nodes",
      "children": {
        "*": {
          "type": "lambda",
          "kind": "hyperlambda-result-node",
          "description": "Returned child node produced by the executed Hyperlambda file",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "Payload",
          "projection": "Self"
        }
      }
    }
  }
}
```

</details>

---

[&larr; `io.file.delete`](/reference/slots/io/io.file.delete/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.exists` &rarr;](/reference/slots/io/io.file.exists/)

