---
title: "[request.headers.get]"
description: "request.headers.get is a slot in the request namespace of Magic Cloud. Returns a request header by name."
generated: true
llms: false
slot_json: "/reference/slots/request/request.headers.get/slot.json"
---

`request.headers.get` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns a request header by name.

* **Value** (`http-header-name`), required: Header name to retrieve
* **Returns**: Resolves to the value of the named request header, or null if it does not exist

### Guide

[How to use `request.headers.get`](/plugins/magic.endpoint/request.headers.get/)

### JSON declaration

This is the complete declaration of `request.headers.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.headers.get",
  "description": "Returns a request header by name",
  "signature": {
    "input": {
      "kind": "http-header-name",
      "description": "Header name to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "http-header-value,text",
      "description": "Resolves to the value of the named request header, or null if it does not exist"
    }
  }
}
```

</details>

---

[&larr; `request.cookies.list`](/reference/slots/request/request.cookies.list/) | [all `request.*` slots](/reference/slots/request/) | [`request.headers.list` &rarr;](/reference/slots/request/request.headers.list/)

