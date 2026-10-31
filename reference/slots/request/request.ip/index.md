---
title: "[request.ip]"
description: "request.ip is a slot in the request namespace of Magic Cloud. Returns the client IP address for the current request."
generated: true
llms: false
slot_json: "/reference/slots/request/request.ip/slot.json"
---

`request.ip` is a slot in the `request` namespace, in Hyperlambda, the language of Magic Cloud. Returns the client IP address for the current request.

* **Returns**: Resolves to the client IP address for the requested IP version

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[version]` | string | no | IP version to return, either ipv4 or ipv6. |

### Guide

[How to use `request.ip`](/plugins/magic.endpoint/request.ip/)

### JSON declaration

This is the complete declaration of `request.ip`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "request.ip",
  "description": "Returns the client IP address for the current request",
  "signature": {
    "children": {
      "version": {
        "type": "string",
        "kind": "ip-version",
        "description": "IP version to return, either ipv4 or ipv6",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "ip-address,text",
      "description": "Resolves to the client IP address for the requested IP version"
    }
  }
}
```

</details>

---

[&larr; `request.host`](/reference/slots/request/request.host/) | [all `request.*` slots](/reference/slots/request/) | [`request.scheme` &rarr;](/reference/slots/request/request.scheme/)

