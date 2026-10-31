---
title: "[response.headers.set]"
description: "response.headers.set is a slot in the response namespace of Magic Cloud. Sets one or more response headers from key/value child nodes."
generated: true
llms: false
slot_json: "/reference/slots/response/response.headers.set/slot.json"
---

`response.headers.set` is a slot in the `response` namespace, in Hyperlambda, the language of Magic Cloud. Sets one or more response headers from key/value child nodes.

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Response header name and value. Can be repeated. |

### JSON declaration

This is the complete declaration of `response.headers.set`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "response.headers.set",
  "description": "Sets one or more response headers from key/value child nodes",
  "signature": {
    "children": {
      "*": {
        "type": "string",
        "kind": "http-response-header-value",
        "description": "Response header name and value",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "OneOrMore",
        "role": "DynamicMap",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `response.cookies.set`](/reference/slots/response/response.cookies.set/) | [all `response.*` slots](/reference/slots/response/) | [`response.status.set` &rarr;](/reference/slots/response/response.status.set/)

