---
title: "[request.cookies.list]"
description: "request.cookies.list is a slot in the request namespace of Magic Cloud. Lists request cookies."
generated: true
llms: false
slot_json: "/reference/slots/request/request.cookies.list/slot.json"
---

`request.cookies.list` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Lists request cookies.

* **Returns**: Resolves to one child node per request cookie, with the cookie name as the node name and its value as the node value

### JSON declaration

This is the complete declaration of `request.cookies.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.cookies.list",
  "description": "Lists request cookies",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "cookie-map,lambda-tree",
      "element-kind": "cookie-value,text",
      "description": "Resolves to one child node per request cookie, with the cookie name as the node name and its value as the node value"
    }
  }
}
```

</details>

---

[&larr; `request.cookies.get`](/reference/slots/request/request.cookies.get/) | [all `request.*` slots](/reference/slots/request/) | [`request.headers.get` &rarr;](/reference/slots/request/request.headers.get/)

