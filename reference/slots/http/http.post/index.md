---
title: "[http.post]"
description: "http.post is a slot in the http namespace of Magic Cloud. Issues an HTTP POST to the specified URL with payload from [payload] or [filename]; returns the response body and headers."
generated: true
llms: "guide"
slot_json: "/reference/slots/http/http.post/slot.json"
---

`http.post` is a slot in the `http` namespace, in Hyperlambda, the language of Magic Cloud. Issues an HTTP POST to the specified URL with payload from [payload] or [filename]; returns the response body and headers.

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

### Guide

<!-- guide -->
This slot accepts a URL as its value, and optionally HTTP headers as a **[headers]** argument, and a mandatory
**[payload]** argument, being whatever payload you want to transfer to the endpoint. In its simplest version
it would resemble something such as the following.

```
http.post:"https://some_website.com/your-post-endpoint"
   payload:@"{""foo"": ""bar""}"
```

The slot returns the result of the specified HTTP POST invocation, including the HTTP headers returned from the endpoint,
and status code, in addition to the response object itself. To automatically convert the response object to whatever
type of response your URL returns, provide a **[convert]** argument, and set its value to true, such as follows.

```
http.post:"https://some_website.com/your-post-endpoint"
   payload:@"{""foo"": ""bar""}"
   convert:true
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.http](/plugins/magic.lambda.http/) plugin, which documents every slot it contains.
* Discussed in [Automatic conversion](/plugins/magic.lambda.http/automatic-conversion/).

### JSON declaration

This is the complete declaration of `http.post`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `http.patch`](/reference/slots/http/http.patch/) | [all `http.*` slots](/reference/slots/http/) | [`http.put` &rarr;](/reference/slots/http/http.put/)

