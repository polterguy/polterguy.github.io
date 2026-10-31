---
title: "[request.url]"
description: "request.url is a slot in the request namespace of Magic Cloud. Returns the requested URL path and exposes each query-string parameter as a child node."
generated: true
llms: false
slot_json: "/reference/slots/request/request.url/slot.json"
---

`request.url` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns the requested URL path and exposes each query-string parameter as a child node.

* **Returns**: Resolves to the full request URL in value and the parsed query string parameters as child nodes

### Guide

[How to use `request.url`](/plugins/magic.endpoint/request.url/)

### JSON declaration

This is the complete declaration of `request.url`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.url",
  "description": "Returns the requested URL path and exposes each query-string parameter as a child node",
  "signature": {
    "output": {
      "mode": "Both",
      "kind": "url,text",
      "description": "Resolves to the full request URL in value and the parsed query string parameters as child nodes"
    }
  }
}
```

</details>

---

[&larr; `request.scheme`](/reference/slots/request/request.scheme/) | [all `request.*` slots](/reference/slots/request/) | [`request.verb` &rarr;](/reference/slots/request/request.verb/)

