---
title: magic.lambda.http slot reference
description: Every slot in magic.lambda.http with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.http](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.http). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.http](/plugins/magic.lambda.http/)._

## [http.delete]

Issues an HTTP DELETE to the specified URL; used to remove a remote resource.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Returned node | Type | Description |
|---|---|---|
| `[timeout]` | int | Request timeout in seconds |
| `[convert]` | bool | Whether to convert known response content types to lambda |
| `[content]` | string\|byte[]\|lambda | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true |
| `[*]` | lambda | HTTP response headers returned by the server |

Guide: [How to use [http.delete]](/plugins/magic.lambda.http/#how-to-use-httpdelete)

## [http.get]

Issues an HTTP GET to the specified URL and returns the response body, status code, and headers.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Returned node | Type | Description |
|---|---|---|
| `[timeout]` | int | Request timeout in seconds |
| `[convert]` | bool | Whether to convert known response content types to lambda |
| `[content]` | string\|byte[]\|lambda | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true |
| `[*]` | lambda | HTTP response headers returned by the server |

Guide: [How to use [http.get]](/plugins/magic.lambda.http/#how-to-use-httpget)

## [http.patch]

Issues an HTTP PATCH to the specified URL with a payload; used to apply partial updates to a remote resource.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[payload]` | object\|lambda | no | Request payload value or structured payload transformed according to Content-Type |

| Returned node | Type | Description |
|---|---|---|
| `[timeout]` | int | Request timeout in seconds |
| `[convert]` | bool | Whether to convert known response content types to lambda |
| `[content]` | string\|byte[]\|lambda | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true |
| `[*]` | lambda | HTTP response headers returned by the server |

Guide: [How to use [http.patch]](/plugins/magic.lambda.http/#how-to-use-httppatch)

## [http.post]

Issues an HTTP POST to the specified URL with payload from [payload] or [filename]; returns the response body and headers.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[payload]` | object\|lambda | no | Request payload value or structured payload transformed according to Content-Type |

| Returned node | Type | Description |
|---|---|---|
| `[timeout]` | int | Request timeout in seconds |
| `[convert]` | bool | Whether to convert known response content types to lambda |
| `[content]` | string\|byte[]\|lambda | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true |
| `[*]` | lambda | HTTP response headers returned by the server |

Guide: [How to use [http.post]](/plugins/magic.lambda.http/#how-to-use-httppost)

## [http.put]

Issues an HTTP PUT to the specified URL with a payload; commonly used to replace a remote resource in full.

* **Value** (`url-template`), required: URL to send the request to; supports {placeholder} segments substituted from [url-params]
* **Returns**: Resolves to the HTTP status code in value and response headers and content as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[payload]` | object\|lambda | no | Request payload value or structured payload transformed according to Content-Type |

| Returned node | Type | Description |
|---|---|---|
| `[timeout]` | int | Request timeout in seconds |
| `[convert]` | bool | Whether to convert known response content types to lambda |
| `[content]` | string\|byte[]\|lambda | HTTP response body; text responses are returned as string, binary responses as byte[], and converted known content types as child nodes when [convert] is true |
| `[*]` | lambda | HTTP response headers returned by the server |

Guide: [How to use [http.put]](/plugins/magic.lambda.http/#how-to-use-httpput)

