---
title: "[sleep]"
description: "sleep is a core slot of Magic Cloud. Delays execution for the specified number of milliseconds."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/sleep/slot.json"
---

`sleep` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Delays execution for the specified number of milliseconds.

* **Value** (`timeout-ms,integer,number`), required: Delay in milliseconds

### Guide

<!-- guide -->
This slot will sleep the current thread for x number of milliseconds, where x is an integer value, expected
to be passed in as its main value.

```
// Sleeps the main thread for 1 second, or 1000 milliseconds.
sleep:1000
```

**Notice** - This slot is typically releasing the thread back to the operating system, implying as
the current thread is _"sleeping"_, it will not be a blocking call, and require ZERO physical operating
system threads while it is sleeping. This is true because of Hyperlambda's 100% perfectly `async` nature.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.threading](/plugins/magic.lambda.threading/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sleep`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sleep",
  "description": "Delays execution for the specified number of milliseconds",
  "signature": {
    "input": {
      "kind": "timeout-ms,integer,number",
      "description": "Delay in milliseconds",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `signal`](/reference/slots/core/signal/) | [all core slots](/reference/slots/core/) | [`sort` &rarr;](/reference/slots/core/sort/)

