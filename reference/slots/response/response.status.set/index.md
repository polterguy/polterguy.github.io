---
title: "[response.status.set]"
description: "response.status.set is a slot in the response namespace of Magic Cloud. Overrides the HTTP status code returned to the caller (e.g. 201 Created, 404 Not Found, 500 Internal Error)."
generated: true
llms: false
slot_json: "/reference/slots/response/response.status.set/slot.json"
---

`response.status.set` is a slot in the `response` namespace, in Hyperlambda, the language of Magic Cloud. Overrides the HTTP status code returned to the caller (e.g. 201 Created, 404 Not Found, 500 Internal Error).

* **Value** (`http-status-code,integer,number`), required: HTTP status code to set

### Guide

[How to use `response.status.set`](/plugins/magic.endpoint/response.status.set/)

### JSON declaration

This is the complete declaration of `response.status.set`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "response.status.set",
  "description": "Overrides the HTTP status code returned to the caller (e.g. 201 Created, 404 Not Found, 500 Internal Error)",
  "signature": {
    "input": {
      "kind": "http-status-code,integer,number",
      "description": "HTTP status code to set",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `response.headers.set`](/reference/slots/response/response.headers.set/) | [all `response.*` slots](/reference/slots/response/)

