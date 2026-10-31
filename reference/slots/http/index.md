---
title: http.* slots
description: The 5 slots named http.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [http.delete]

Issues an HTTP DELETE to the specified URL; used to remove a remote resource.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.sse]` | lambda | no | Callback executed once per server-sent event line; receives the line in [.arguments/message]. |
| `[convert]` | bool | no | Whether to convert known response content types to lambda. Default: `false`. |
| `[headers]` | lambda | no | HTTP request headers. |
| `[headers]` / _any node name_ | string | no | HTTP header value. Can be repeated. |
| `[query]` | lambda | no | Query string parameters. |
| `[query]` / _any node name_ | string | no | Query parameter value. Can be repeated. |
| `[timeout]` | int | no | Request timeout in seconds. |
| `[token]` | string | no | Bearer token to add as Authorization header. |
| `[url-params]` | lambda | no | Named replacements for {placeholders} in the URL. |
| `[url-params]` / _any node name_ | string | no | URL placeholder replacement value. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

Guide: [How to use [http.delete]](/plugins/magic.lambda.http/#how-to-use-httpdelete)

## [http.get]

Issues an HTTP GET to the specified URL and returns the response body, status code, and headers.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.sse]` | lambda | no | Callback executed once per server-sent event line; receives the line in [.arguments/message]. |
| `[convert]` | bool | no | Whether to convert known response content types to lambda. Default: `false`. |
| `[headers]` | lambda | no | HTTP request headers. |
| `[headers]` / _any node name_ | string | no | HTTP header value. Can be repeated. |
| `[query]` | lambda | no | Query string parameters. |
| `[query]` / _any node name_ | string | no | Query parameter value. Can be repeated. |
| `[timeout]` | int | no | Request timeout in seconds. |
| `[token]` | string | no | Bearer token to add as Authorization header. |
| `[url-params]` | lambda | no | Named replacements for {placeholders} in the URL. |
| `[url-params]` / _any node name_ | string | no | URL placeholder replacement value. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

Guide: [How to use [http.get]](/plugins/magic.lambda.http/#how-to-use-httpget)

## [http.patch]

Issues an HTTP PATCH to the specified URL with a payload; used to apply partial updates to a remote resource.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

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

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

* **Constraint** (ExactlyOneOf): Provide exactly one of [payload] or [filename] as the request body source (`[payload]`, `[filename]`)

Guide: [How to use [http.patch]](/plugins/magic.lambda.http/#how-to-use-httppatch)

## [http.post]

Issues an HTTP POST to the specified URL with payload from [payload] or [filename]; returns the response body and headers.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

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

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

* **Constraint** (ExactlyOneOf): Provide exactly one of [payload] or [filename] as the request body source (`[payload]`, `[filename]`)

Guide: [How to use [http.post]](/plugins/magic.lambda.http/#how-to-use-httppost)

## [http.put]

Issues an HTTP PUT to the specified URL with a payload; commonly used to replace a remote resource in full.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

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

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| `[content]` | string\|byte[]\|lambda | no | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true. |
| `[headers]` | lambda | no | HTTP response headers returned by the server. |
| `[headers]` / _any node name_ | string | no | HTTP response header value; child name is the header name. Can be repeated. |

* **Constraint** (ExactlyOneOf): Provide exactly one of [payload] or [filename] as the request body source (`[payload]`, `[filename]`)

Guide: [How to use [http.put]](/plugins/magic.lambda.http/#how-to-use-httpput)

