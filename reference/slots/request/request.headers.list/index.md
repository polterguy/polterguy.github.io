---
title: "[request.headers.list]"
description: "request.headers.list is a slot in the request namespace of Magic Cloud. Lists request headers."
generated: true
llms: false
slot_json: "/reference/slots/request/request.headers.list/slot.json"
---

`request.headers.list` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Lists request headers.

* **Returns**: Resolves to one child node per request header, with the header name as the node name and its value as the node value

### Guide

[How to use `request.headers.list`](/plugins/magic.endpoint/request.headers.list/)

### JSON declaration

This is the complete declaration of `request.headers.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.headers.list",
  "description": "Lists request headers",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "http-header-map,lambda-tree",
      "element-kind": "http-header-value,text",
      "description": "Resolves to one child node per request header, with the header name as the node name and its value as the node value"
    }
  }
}
```

</details>

---

[&larr; `request.headers.get`](/reference/slots/request/request.headers.get/) | [all `request.*` slots](/reference/slots/request/) | [`request.host` &rarr;](/reference/slots/request/request.host/)

