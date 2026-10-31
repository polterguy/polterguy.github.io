---
title: "[semaphore]"
description: "semaphore is a core slot of Magic Cloud. Serializes access to a critical section by name; only one thread at a time can enter a given semaphore."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/semaphore/slot.json"
---

`semaphore` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Serializes access to a critical section by name; only one thread at a time can enter a given semaphore.

* **Value** (`semaphore-name`), required: Semaphore name used to serialize access
* **Scope**: provides `semaphore`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child lambda object evaluated while the named semaphore is held. Can be repeated. |

### Guide

<!-- guide -->
Creates a named semaphore, where only one thread will be allowed to evaluate the same semaphore at
the same time. Notice, the semaphore to use is defined through its value, implying you can use the same
semaphore multiple places, by using the same value of your **[semaphore]** invocation.

```
semaphore:foo-bar
   /*
    * Only one thread will be allowed entrance into this piece of
    * code at the same time, ensuring synchronized access, for cases
    * where you cannot allow more than one thread to enter at the
    * same time.
    */
```

In the above semaphore _"foo-bar_" becomes the name of your semaphore. If you invoke **[semaphore]** in
any other parts of your Hyperlambda code, with _"foo-bar"_ as the value, only _one_ of your
lambda objects will be allowed to execute at the same time. This allows you to _"synchronize access"_
to shared resources, where only _one_ thread should be allowed to access the shared resource at the same
time. Such shared resources might be for instance files, or other things shared between multiuple threads,
where it's crucial that only one thread is allowed to access the shared resource at the same time.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.threading](/plugins/magic.lambda.threading/) plugin, which documents every slot it contains.

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

