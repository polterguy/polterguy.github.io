---
title: "[sleep]"
description: "sleep is a core slot of Magic Cloud. Delays execution for the specified number of milliseconds."
generated: true
llms: false
slot_json: "/reference/slots/core/sleep/slot.json"
---

`sleep` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Delays execution for the specified number of milliseconds.

* **Value** (`timeout-ms,integer,number`), required: Delay in milliseconds

### Guide

[How to use `sleep`](/plugins/magic.lambda.threading/sleep/)

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

