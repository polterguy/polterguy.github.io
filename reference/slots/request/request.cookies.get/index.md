---
title: "[request.cookies.get]"
description: "request.cookies.get is a slot in the request namespace of Magic Cloud. Returns a request cookie by name."
generated: true
llms: false
slot_json: "/reference/slots/request/request.cookies.get/slot.json"
---

`request.cookies.get` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns a request cookie by name.

* **Value** (`cookie-name`), required: Cookie name to retrieve
* **Returns**: Resolves to the value of the named request cookie, or null if it does not exist

### Guide

[How to use `request.cookies.get`](/plugins/magic.endpoint/request.cookies.get/)

### JSON declaration

This is the complete declaration of `request.cookies.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.cookies.get",
  "description": "Returns a request cookie by name",
  "signature": {
    "input": {
      "kind": "cookie-name",
      "description": "Cookie name to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "cookie-value,text",
      "description": "Resolves to the value of the named request cookie, or null if it does not exist"
    }
  }
}
```

</details>

---

[all `request.*` slots](/reference/slots/request/) | [`request.cookies.list` &rarr;](/reference/slots/request/request.cookies.list/)

