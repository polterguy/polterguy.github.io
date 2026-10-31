---
title: "[signal]"
description: "signal is a core slot of Magic Cloud. Invokes a dynamic slot created with [slots.create], passing child nodes as its arguments."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/signal/slot.json"
---

`signal` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Invokes a dynamic slot created with [slots.create], passing child nodes as its arguments.

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
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot. Can be repeated. |

### Guide

<!-- guide -->
Invokes a previously created dynamic slot. Assuming you have created the foo slot from the create slot example,
you can invoke the slot using the following Hyperlambda.

```
signal:foo
```

After evaluating the above Hyperlambda, the **[signal]** node will end up having a value of _"57"_.

**Notice** - This slot obeys by the rules of **[whitelist]** invocations from magic.lambda, allowing you to
declare a list of dynamic slots, which are exclusively allowed to be invoked temporarily inside of an
invocation to whitelist, allowing you to restrict some piece of potentially unsafe code to *only* signal
a pre-defined list of dynamically created slots. Below is an example.

```
slots.create:foo1
   return-value:Safe

slots.create:foo2
   return-value:Unsafe

whitelist

   vocabulary
      signal
      signal:foo1

   .lambda

      // Assuming you have a [foo1] slot created, this will work
      signal:foo1

      // This will throw, since [foo2] is not whitelisted
      signal:foo2
```

Basically, _only_ the slots declared in the above **[vocabulary]** will be allowed to be invoked inside
of the above **[.lambda]** object. You must have your dynamic slots declared as **signal:slot-name**,
such as the above illustrates. And in order to signal dynamic slots *at all*, you'll need to (obviously)
whitelist **[signal]** itself, as illustrated in the above code. Read more about **[whitelist]** in 
the magic.lambda project. Inside your slots though any **[whitelist]** invocations will simply be ignored,
allowing you to whitelist a single dynamic slot, for then to ignore what the slot itself is doing internally.
This _might_ create security issues for you if you have dynamically created slots that for some reasons
execute lambda object supplied to them. Hence as a general rule of thumb, you should _avoid_ whitelisting
slots that executes lambda objects supplied to them. The same is true for Hyperlambda files executed with
**[execute-file]** or **[io.file.execute]**, which you can pin in a whitelist by path - see
[magic.lambda.io](/plugins/magic.lambda.io/).
<!-- /guide -->

### JSON declaration

This is the complete declaration of `signal`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "signal",
  "description": "Invokes a dynamic slot created with [slots.create], passing child nodes as its arguments",
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
          "description": "Returned child node produced by the invoked dynamic slot",
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

[&larr; `set-x`](/reference/slots/core/set-x/) | [all core slots](/reference/slots/core/) | [`sleep` &rarr;](/reference/slots/core/sleep/)

