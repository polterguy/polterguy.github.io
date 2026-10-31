---
title: "[execute]"
description: "execute is a core slot of Magic Cloud. Invokes a dynamic slot after unwrapping descendant expressions."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/execute/slot.json"
---

`execute` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Invokes a dynamic slot after unwrapping descendant expressions.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to invoke
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the dynamic slot as a child of [.arguments]. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot after descendant expressions are unwrapped. Can be repeated. |

### Guide

<!-- guide -->
The **[execute]** slot is an alias for **[signal]**, but it will **[unwrap]** all children nodes, automatically
transform any expressions to their static value equivalents, allowing you to combine **[unwrap]** and **[signal]**
into one invocation. This makes usage slightly less verbose for cases such as the following.

```
.args
   foo1:bar1
   foo2:bar2
execute:whatever-slot
   arg1:x:@.args/*/foo1
   arg2:x:@.args/*/foo2
```

In the above example both arguments to our _"whatever-slot"_ invocation will be evaluated before the slot is invoked,
resulting in **[arg1]** and **[args2]** having the values of _"bar1"_ and _"bar2"_ respectively.

If you pass in a node named **[node_reference]** using the above syntax, this node will be especially handled, and
passed in by reference instead of evaluated as a single expression value. Consider the following alternative to
the above.

```
.args
   foo1:bar1
   foo2:bar2
execute:whatever-slot
   node_reference:x:@.args
```

Inside your above _"whatever-slot"_ you will now have access to the entire **[.args]** node by reference.
It might help to execute the following to understand.

```
.args
   foo1:howdy
   foo2:world
slots.create:foo
   lambda2hyper:x:../*
   return:x:-
execute:foo
   node_reference:x:@.args/*
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.slots](/plugins/magic.lambda.slots/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execute",
  "description": "Invokes a dynamic slot after unwrapping descendant expressions",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to invoke",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Named argument passed to the dynamic slot as a child of [.arguments]",
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
      "description": "Resolves to the invoked slot's value result and any returned child nodes",
      "children": {
        "*": {
          "type": "lambda",
          "kind": "dynamic-slot-result-node",
          "description": "Returned child node produced by the invoked dynamic slot after descendant expressions are unwrapped",
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

[&larr; `eval`](/reference/slots/core/eval/) | [all core slots](/reference/slots/core/) | [`execute-file` &rarr;](/reference/slots/core/execute-file/)

