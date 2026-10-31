---
title: "[server.ip]"
description: "server.ip is a slot in the server namespace of Magic Cloud. Returns the server's local IP address (IPv4 by default); useful for logging or building absolute URLs."
generated: true
llms: false
slot_json: "/reference/slots/server/server.ip/slot.json"
---

`server.ip` is a slot in the `server` namespace, in Hyperlambda, the language of Magic Cloud. Returns the server's local IP address (IPv4 by default); useful for logging or building absolute URLs.

* **Returns**: Resolves to the server IP address for the requested IP version

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[version]` | string | no | IP version to return, either ipv4 or ipv6. |

### Guide

[How to use `server.ip`](/plugins/magic.endpoint/server.ip/)

### JSON declaration

This is the complete declaration of `server.ip`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "server.ip",
  "description": "Returns the server's local IP address (IPv4 by default); useful for logging or building absolute URLs",
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
      "description": "Resolves to the server IP address for the requested IP version"
    }
  }
}
```

</details>

---

[all `server.*` slots](/reference/slots/server/)

