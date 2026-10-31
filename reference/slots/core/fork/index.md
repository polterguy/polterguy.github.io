---
title: "[fork]"
description: "fork is a core slot of Magic Cloud. Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/fork/slot.json"
---

`fork` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately.

* **Scope**: provides `fork`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child slot evaluated on the forked thread. Can be repeated. |

### Guide

<!-- guide -->
Forks the given lambda into a new thread of execution, using a thread from the thread pool. This
slot is useful for creating _"fire and forget"_ lambda objects, where you don't need to wait
for the result of the execution before continuing executing the current scope.

```
fork
   info.log:I was invoked from another thread
```

To understand how **[fork]** works, you can imagine your computer's CPU as a single river,
running down hill, and at some point the river divides into two equally large rivers. This is
referred to as _"a fork"_. The analogy of the river becomes important for another reason, which
is the understanding of that the total amount of water is still the same, it's only parted
into two smaller rivers - Implying you cannot _"do more"_ with multi tasking, you can only
equally share the same amount of resources as you had before between two different tasks.
Multi threading does not make your CPU faster, it only schedules your CPU's time on multiple
things, doing these things concurrently. However, if you have multiple tasks where each
individual task needs to wait for IO data, threading typically speeds up your application,
since it can make multiple requests for IO simultaneously, and have other machines, and/or
processes working in parallel.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.threading](/plugins/magic.lambda.threading/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `fork`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "fork",
  "description": "Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot evaluated on the forked thread",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "fork"
    }
  }
}
```

</details>

---

[&larr; `for-each`](/reference/slots/core/for-each/) | [all core slots](/reference/slots/core/) | [`format` &rarr;](/reference/slots/core/format/)

