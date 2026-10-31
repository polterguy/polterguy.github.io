---
title: "[http.delete]"
description: "http.delete is a slot in the http namespace of Magic Cloud. Issues an HTTP DELETE to the specified URL; used to remove a remote resource."
generated: true
llms: "guide"
slot_json: "/reference/slots/http/http.delete/slot.json"
---

`http.delete` is a slot in the `http` namespace, in Hyperlambda, the language of Magic Cloud. Issues an HTTP DELETE to the specified URL; used to remove a remote resource.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[query]` | lambda | no | Query string parameters. |
| `[query]` / _any node name_ | string | no | Query parameter value. Can be repeated. |
| `[url-params]` | lambda | no | Named replacements for {placeholders} in the URL. |
| `[url-params]` / _any node name_ | string | no | URL placeholder replacement value. Can be repeated. |
| `[headers]` | lambda | no | HTTP request headers. |
| `[headers]` / _any node name_ | string | no | HTTP header value. Can be repeated. |
| `[token]` | string | no | Bearer token to add as Authorization header. |
| `[timeout]` | int | no | Request timeout in seconds. |
| `[convert]` | bool | no | Whether to convert known response content types to lambda. Default: `false`. |
| `[.sse]` | lambda | no | Callback executed once per server-sent event line; receives the line in [.arguments/message]. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

### Guide

<!-- guide -->
This slot accepts a URL as its value, and optionally HTTP headers as a **[headers]** argument. In its simplest version
it would resemble something such as the following.

```
http.delete:"https://your_website.com/your-delete-endpoint"
```

The slot returns the result of the specified HTTP DELETE invocation, including the HTTP headers returned from the endpoint,
and status code, in addition to the response object itself.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `http.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[all `http.*` slots](/reference/slots/http/) | [`http.get` &rarr;](/reference/slots/http/http.get/)

