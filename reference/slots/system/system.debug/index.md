---
title: "[system.debug]"
description: "system.debug is a slot in the system namespace of Magic Cloud. Evaluates the child lambda while recording every slot invocation, returning the recording."
generated: true
llms: false
slot_json: "/reference/slots/system/system.debug/slot.json"
---

`system.debug` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Evaluates the child lambda while recording every slot invocation, returning the recording.

* **Returns**: Resolves to one node per executed slot, each with [slot], [path], [elapsed] and [lambda] being the entire lambda object after that slot was invoked

### Guide

[How to use `system.debug`](/plugins/magic.lambda.system/system.debug/)

### JSON declaration

This is the complete declaration of `system.debug`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.debug",
  "description": "Evaluates the child lambda while recording every slot invocation, returning the recording",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "recording,node-list",
      "description": "Resolves to one node per executed slot, each with [slot], [path], [elapsed] and [lambda] being the entire lambda object after that slot was invoked"
    }
  }
}
```

</details>

---

[&larr; `system.compile`](/reference/slots/system/system.compile/) | [all `system.*` slots](/reference/slots/system/) | [`system.execute` &rarr;](/reference/slots/system/system.execute/)

