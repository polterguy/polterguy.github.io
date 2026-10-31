---
title: "[request.scheme]"
description: "request.scheme is a slot in the request namespace of Magic Cloud. Returns the scheme (http or https) of the current incoming request."
generated: true
llms: false
slot_json: "/reference/slots/request/request.scheme/slot.json"
---

`request.scheme` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns the scheme (http or https) of the current incoming request.

* **Returns**: Resolves to the scheme of the current request, such as http or https

### JSON declaration

This is the complete declaration of `request.scheme`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.scheme",
  "description": "Returns the scheme (http or https) of the current incoming request",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "http-scheme,text",
      "description": "Resolves to the scheme of the current request, such as http or https"
    }
  }
}
```

</details>

---

[&larr; `request.ip`](/reference/slots/request/request.ip/) | [all `request.*` slots](/reference/slots/request/) | [`request.url` &rarr;](/reference/slots/request/request.url/)

