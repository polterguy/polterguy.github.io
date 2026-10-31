---
title: "[slots.create]"
description: "slots.create is a slot in the slots namespace of Magic Cloud. Creates a dynamic slot that can be invoked with [signal]."
generated: true
llms: "guide"
slot_json: "/reference/slots/slots/slots.create/slot.json"
---

`slots.create` is a slot in the `slots` namespace, in Hyperlambda, the language of Magic Cloud. Creates a dynamic slot that can be invoked with [signal].

Also known as: [`function`](/reference/slots/core/function/).

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to create

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child slot stored as the dynamic slot body. Can be repeated. |

### Guide

<!-- guide -->
Creates a dynamic slot that can be invoked using **[signal]**. Below is an example.

```
slots.create:foo
   return-value:int:57
```

Notice, the above slot aren't persisted in any ways, implying if your web server restarts its process, your
slot is removed. If you want to make sure your slots become a permanent part of your application, you need to
make sure you are somehow creating it during server startup, which can normally be done on a per module basis, by putting
a Hyperlambda file into your module's _"magic.startup"_ folder, which makes sure the code is executed during startup
of your web app.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.slots](/plugins/magic.lambda.slots/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `slots.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slots.create",
  "description": "Creates a dynamic slot that can be invoked with [signal]",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to create",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot stored as the dynamic slot body",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "SerializeLambda",
        "projection": "Self"
      }
    }
  }
}
```

</details>

---

[all `slots.*` slots](/reference/slots/slots/) | [`slots.delete` &rarr;](/reference/slots/slots/slots.delete/)

