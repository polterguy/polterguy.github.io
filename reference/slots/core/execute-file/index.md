---
title: "[execute-file]"
description: "execute-file is a core slot of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/execute-file/slot.json"
---

`execute-file` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments].

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
The **[execute-file]** slot is an alias for **[io.file.execute]**, but it will **[unwrap]** all children nodes,
automatically transform any expressions to their static value equivalents, allowing you to combine **[unwrap]**
and **[io.file.execute]** into one invocation. This makes usage slightly less verbose for cases such as the following.

```
.args
   foo1:bar1
   foo2:bar2
execute-file:/whatever-file.hl
   arg1:x:@.args/*/foo1
   arg2:x:@.args/*/foo2
```

In the above example both arguments to our _"/whatever-file.hl"_ file will be evaluated before the file is executed,
resulting in **[arg1]** and **[args2]** having the values of _"bar1"_ and _"bar2"_ respectively.

If you pass in a node named **[node_reference]** using the above syntax, this node will be especially handled, and
passed in by reference instead of evaluated as a single expression value. Consider the following alternative to
the above.

```
.args
   foo1:bar1
   foo2:bar2
execute-file:/whatever-file.hl
   node_reference:x:@.args
```

Inside your above _"/whatever-file.hl"_ file you will now have access to the entire **[.args]** node by reference.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `execute-file`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execute-file",
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
        "preprocess": "UnwrapExpressions",
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

[&larr; `execute`](/reference/slots/core/execute/) | [all core slots](/reference/slots/core/) | [`exists` &rarr;](/reference/slots/core/exists/)

