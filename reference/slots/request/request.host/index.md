---
title: "[request.host]"
description: "request.host is a slot in the request namespace of Magic Cloud. Returns the host header (domain and optional port) of the current incoming request."
generated: true
llms: false
slot_json: "/reference/slots/request/request.host/slot.json"
---

`request.host` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns the host header (domain and optional port) of the current incoming request.

* **Returns**: Resolves to the host name from the current request

### JSON declaration

This is the complete declaration of `request.host`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.host",
  "description": "Returns the host header (domain and optional port) of the current incoming request",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "host-name,text",
      "description": "Resolves to the host name from the current request"
    }
  }
}
```

</details>

---

[&larr; `request.headers.list`](/reference/slots/request/request.headers.list/) | [all `request.*` slots](/reference/slots/request/) | [`request.ip` &rarr;](/reference/slots/request/request.ip/)

