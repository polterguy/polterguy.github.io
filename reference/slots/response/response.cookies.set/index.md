---
title: "[response.cookies.set]"
description: "response.cookies.set is a slot in the response namespace of Magic Cloud. Sets a response cookie."
generated: true
llms: false
slot_json: "/reference/slots/response/response.cookies.set/slot.json"
---

`response.cookies.set` is a slot in the `response` namespace, in Hyperlambda, the language of Magic Cloud. Sets a response cookie.

* **Value** (`cookie-name`), required: Cookie name to set

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[value]` | string | yes | Cookie value. |
| `[expires]` | DateTime | no | Cookie expiration. |
| `[http-only]` | bool | no | Whether the cookie is HTTP-only. |
| `[secure]` | bool | no | Whether the cookie is secure. |
| `[domain]` | string | no | Cookie domain. |
| `[path]` | string | no | Cookie path. |
| `[same-site]` | string | no | Cookie SameSite mode: Strict, Lax, None, or Unspecified. |

### Guide

[How to use `response.cookies.set`](/plugins/magic.endpoint/response.cookies.set/)

### JSON declaration

This is the complete declaration of `response.cookies.set`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "response.cookies.set",
  "description": "Sets a response cookie",
  "signature": {
    "input": {
      "kind": "cookie-name",
      "description": "Cookie name to set",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "value": {
        "type": "string",
        "kind": "cookie-value,text",
        "description": "Cookie value",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "expires": {
        "type": "DateTime",
        "description": "Cookie expiration",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "http-only": {
        "type": "bool",
        "description": "Whether the cookie is HTTP-only",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "secure": {
        "type": "bool",
        "description": "Whether the cookie is secure",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "domain": {
        "type": "string",
        "kind": "cookie-domain",
        "description": "Cookie domain",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "path": {
        "type": "string",
        "kind": "cookie-path",
        "description": "Cookie path",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "same-site": {
        "type": "string",
        "kind": "cookie-same-site",
        "description": "Cookie SameSite mode: Strict, Lax, None, or Unspecified",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[all `response.*` slots](/reference/slots/response/) | [`response.headers.set` &rarr;](/reference/slots/response/response.headers.set/)

