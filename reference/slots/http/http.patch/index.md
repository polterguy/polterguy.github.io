---
title: "[http.patch]"
description: "http.patch is a slot in the http namespace of Magic Cloud. Issues an HTTP PATCH to the specified URL with a payload; used to apply partial updates to a remote resource."
generated: true
llms: false
slot_json: "/reference/slots/http/http.patch/slot.json"
---

`http.patch` is a slot in the `http` namespace, in Hyperlambda, the language of Magic Cloud. Issues an HTTP PATCH to the specified URL with a payload; used to apply partial updates to a remote resource.

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
| `[payload]` | object\|lambda | no | Request payload value or structured payload transformed according to Content-Type. |
| `[filename]` | string | no | File path to stream as the request payload. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

### Constraints

* **ExactlyOneOf**: Provide exactly one of [payload] or [filename] as the request body source (`[payload]`, `[filename]`)

Guide: [How to use [http.patch]](/plugins/magic.lambda.http/#how-to-use-httppatch)

### JSON declaration

This is the complete declaration of `http.patch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `http.get`](/reference/slots/http/http.get/) | [all `http.*` slots](/reference/slots/http/) | [`http.post` &rarr;](/reference/slots/http/http.post/)

