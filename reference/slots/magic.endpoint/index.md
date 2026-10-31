---
title: magic.endpoint slot reference
description: Every slot in magic.endpoint with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.endpoint](https://github.com/polterguy/magic/tree/master/plugins/magic.endpoint). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.endpoint](/plugins/magic.endpoint/)._

## [endpoints.list]

Lists dynamic Hyperlambda endpoints with metadata.

* **Returns**: Resolves to one child node per discovered endpoint, including its endpoint metadata

## [mime.add]

Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses.

* **Value** (`content-type`), required: File extension or MIME type key to register

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.]` |  | yes | MIME type value for the extension/key |

Guide: [How to use [mime.add]](/plugins/magic.endpoint/#how-to-use-mimeadd)

## [mime.list]

Lists registered MIME type mappings.

* **Returns**: Resolves to one named child node per registered MIME type mapping, where the child name is the file extension and the value is the MIME type

Guide: [How to use [mime.list]](/plugins/magic.endpoint/#how-to-use-mimelist)

## [request.cookies.get]

Returns a request cookie by name.

* **Value** (`cookie-name`), required: Cookie name to retrieve
* **Returns**: Resolves to the value of the named request cookie, or null if it does not exist

## [request.cookies.list]

Lists request cookies.

* **Returns**: Resolves to one child node per request cookie, with the cookie name as the node name and its value as the node value

## [request.headers.get]

Returns a request header by name.

* **Value** (`http-header-name`), required: Header name to retrieve
* **Returns**: Resolves to the value of the named request header, or null if it does not exist

## [request.headers.list]

Lists request headers.

* **Returns**: Resolves to one child node per request header, with the header name as the node name and its value as the node value

## [request.host]

Returns the host header (domain and optional port) of the current incoming request.

* **Returns**: Resolves to the host name from the current request

## [request.ip]

Returns the client IP address for the current request.

* **Returns**: Resolves to the client IP address for the requested IP version

## [request.scheme]

Returns the scheme (http or https) of the current incoming request.

* **Returns**: Resolves to the scheme of the current request, such as http or https

## [request.url]

Returns the requested URL path and exposes each query-string parameter as a child node.

* **Returns**: Resolves to the full request URL in value and the parsed query string parameters as child nodes

## [request.verb]

Returns the HTTP verb (get, post, put, delete, etc.) of the current incoming request.

* **Returns**: Resolves to the HTTP verb of the current request

Guide: [How to use [request.verb]](/plugins/magic.endpoint/#how-to-use-requestverb)

## [response.cookies.set]

Sets a response cookie.

* **Value** (`cookie-name`), required: Cookie name to set

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expires]` | DateTime | no | Cookie expiration |
| `[http-only]` | bool | no | Whether the cookie is HTTP-only |
| `[secure]` | bool | no | Whether the cookie is secure |

## [response.headers.set]

Sets one or more response headers from key/value child nodes.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Response header name and value |

## [response.status.set]

Overrides the HTTP status code returned to the caller (e.g. 201 Created, 404 Not Found, 500 Internal Error).

* **Value** (`http-status-code,integer,number`), required: HTTP status code to set

## [server.ip]

Returns the server's local IP address (IPv4 by default); useful for logging or building absolute URLs.

* **Returns**: Resolves to the server IP address for the requested IP version

