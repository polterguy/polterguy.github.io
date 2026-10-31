---
title: "[console.log]"
description: "console.log is a slot in the console namespace of Magic Cloud. Writes a message to the server console."
generated: true
llms: false
slot_json: "/reference/slots/console/console.log/slot.json"
---

`console.log` is a slot in the `console` namespace, in Hyperlambda, the language of Magic Cloud. Writes a message to the server console.

* **Value** (`log-message,text`), required: Message to write to the server console

### JSON declaration

This is the complete declaration of `console.log`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "console.log",
  "description": "Writes a message to the server console",
  "signature": {
    "input": {
      "kind": "log-message,text",
      "description": "Message to write to the server console",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[all `console.*` slots](/reference/slots/console/)

