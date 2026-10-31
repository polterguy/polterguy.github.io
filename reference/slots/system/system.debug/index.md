---
title: "[system.debug]"
description: "system.debug is a slot in the system namespace of Magic Cloud. Evaluates the child lambda while recording every slot invocation, returning the recording."
generated: true
llms: "guide"
slot_json: "/reference/slots/system/system.debug/slot.json"
---

`system.debug` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Evaluates the child lambda while recording every slot invocation, returning the recording.

* **Returns**: Resolves to one node per executed slot, each with [slot], [path], [elapsed] and [lambda] being the entire lambda object after that slot was invoked

### Guide

<!-- guide -->
This slot evaluates its children the same way **[\[eval\]](/reference/slots/core/eval/)** does, but records every single slot invocation
as it happens, and returns the recording instead of leaving the lambda in place. This is what powers
[Rewind](/dashboard/hyper-ide/#rewind---stepping-through-an-execution) in Hyper IDE, allowing you
to step through an execution after it has already finished.

```
system.debug

   .no:int:0
   set-value:x:@.no
      .:int:5
   math.increment:x:@.no
   return:x:@.no
```

The above returns one node per executed slot, each having the following children.

* __[slot]__ - Name of the slot that was invoked
* __[path]__ - Index path to the node that was invoked, such as _"0.1"_ for the second child of the first node
* __[elapsed]__ - Number of milliseconds the invocation took
* __[lambda]__ - The **entire** lambda object as Hyperlambda, exactly as it looked immediately after the invocation

The last point above is the interesting one. Since each step carries the whole lambda object and not
just the node that ran, moving from one step to the next is watching the program's own state evolve,
which is a very different thing from reading a stack trace and guessing what the values were.

If the lambda returned something, the recording ends with a **[returned]** node. If the lambda threw,
it ends with an **[error]** node having the exception message as its value and a **[\[type\]](/reference/slots/core/type/)** child with
the CLR type of the exception. An execution that throws is precisely the one you want to look at, so
the exception is caught and returned as a part of the recording rather than being allowed to discard
everything leading up to it.

```
system.debug

   .data
      .
         name:Thomas
   throw:This is recorded, and so is everything above it
```

Some things to be aware of.

* The lambda is cloned into a detached root before it is evaluated, such that expressions navigating upwards resolve the same way they would if the lambda was executed normally. This implies the slot cannot see nodes outside of itself.
* A **[\[return\]](/reference/slots/core/return/)** inside the lambda terminates the lambda being debugged, and not whoever invoked **[system.debug]**.
* Slots executed on another thread through **[\[fork\]](/reference/slots/core/fork/)** are not recorded, since a fork creates its own signaler. **[\[join\]](/reference/slots/core/join/)** is recorded, but its children are not.
* Recording is turned on for the lambda passed into this slot only, and adds nothing to the execution speed of the language elsewhere.
* The recording contains a copy of the entire lambda object for every single step, so debugging a lambda that loops thousands of times produces a very large result. Recording therefore stops after 10,000 steps, and the recording's last step becomes a **[truncated]** node declaring this, rather than the recording silently ending.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.system](/plugins/magic.lambda.system/) plugin, which documents every slot it contains.

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

