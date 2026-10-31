---
title: "[http.post]"
description: "http.post is a slot in the http namespace of Magic Cloud. Issues an HTTP POST to the specified URL with payload from [payload] or [filename]; returns the response body and headers."
generated: true
llms: false
slot_json: "/reference/slots/http/http.post/slot.json"
---

`http.post` is a slot in the `http` namespace, in Hyperlambda, the language of Magic Cloud. Issues an HTTP POST to the specified URL with payload from [payload] or [filename]; returns the response body and headers.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.sse]` | lambda | no | Callback executed once per server-sent event line; receives the line in [.arguments/message]. |
| `[convert]` | bool | no | Whether to convert known response content types to lambda. Default: `false`. |
| `[filename]` | string | no | File path to stream as the request payload. |
| `[headers]` | lambda | no | HTTP request headers. |
| `[headers]` / _any node name_ | string | no | HTTP header value. Can be repeated. |
| `[payload]` | object\|lambda | no | Request payload value or structured payload transformed according to Content-Type. |
| `[query]` | lambda | no | Query string parameters. |
| `[query]` / _any node name_ | string | no | Query parameter value. Can be repeated. |
| `[timeout]` | int | no | Request timeout in seconds. |
| `[token]` | string | no | Bearer token to add as Authorization header. |
| `[url-params]` | lambda | no | Named replacements for {placeholders} in the URL. |
| `[url-params]` / _any node name_ | string | no | URL placeholder replacement value. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

### Constraints

* **ExactlyOneOf**: Provide exactly one of [payload] or [filename] as the request body source (`[payload]`, `[filename]`)

Guide: [How to use [http.post]](/plugins/magic.lambda.http/#how-to-use-httppost)

### JSON declaration

This is the complete declaration of `http.post`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `http.patch`](/reference/slots/http/http.patch/) | [all `http.*` slots](/reference/slots/http/) | [`http.put` &rarr;](/reference/slots/http/http.put/)

