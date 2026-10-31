---
title: "[request.verb]"
description: "request.verb is a slot in the request namespace of Magic Cloud. Returns the HTTP verb (get, post, put, delete, etc.) of the current incoming request."
generated: true
llms: false
slot_json: "/reference/slots/request/request.verb/slot.json"
---

`request.verb` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns the HTTP verb (get, post, put, delete, etc.) of the current incoming request.

* **Returns**: Resolves to the HTTP verb of the current request

Guide: [How to use [request.verb]](/plugins/magic.endpoint/#how-to-use-requestverb)

### JSON declaration

This is the complete declaration of `request.verb`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.verb",
  "description": "Returns the HTTP verb (get, post, put, delete, etc.) of the current incoming request",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "http-method,text",
      "description": "Resolves to the HTTP verb of the current request"
    }
  }
}
```

</details>

---

[&larr; `request.url`](/reference/slots/request/request.url/) | [all `request.*` slots](/reference/slots/request/)

