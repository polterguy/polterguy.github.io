---
title: "[semaphore]"
description: "semaphore is a core slot of Magic Cloud. Serializes access to a critical section by name; only one thread at a time can enter a given semaphore."
generated: true
llms: false
slot_json: "/reference/slots/core/semaphore/slot.json"
---

`semaphore` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Serializes access to a critical section by name; only one thread at a time can enter a given semaphore.

* **Value** (`semaphore-name`), required: Semaphore name used to serialize access
* **Scope**: provides `semaphore`

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child lambda object evaluated while the named semaphore is held. Can be repeated. |

Guide: [How to use [semaphore]](/plugins/magic.lambda.threading/#how-to-use-semaphore)

### JSON declaration

This is the complete declaration of `semaphore`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "semaphore",
  "description": "Serializes access to a critical section by name; only one thread at a time can enter a given semaphore",
  "signature": {
    "input": {
      "kind": "semaphore-name",
      "description": "Semaphore name used to serialize access",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child lambda object evaluated while the named semaphore is held",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "semaphore"
    }
  }
}
```

</details>

---

[&larr; `return-value`](/reference/slots/core/return-value/) | [all core slots](/reference/slots/core/) | [`set-name` &rarr;](/reference/slots/core/set-name/)

