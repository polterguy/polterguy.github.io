---
title: request.* slots
description: The 9 slots named request.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

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

| Argument | Type | Required | Description |
|---|---|---|---|
| `[version]` | string | no | IP version to return, either ipv4 or ipv6. |

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

