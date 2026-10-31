---
title: response.* slots
description: The 3 slots named response.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [response.cookies.set]

Sets a response cookie.

* **Value** (`cookie-name`), required: Cookie name to set

| Argument | Type | Required | Description |
|---|---|---|---|
| `[value]` | string | yes | Cookie value. |
| `[expires]` | DateTime | no | Cookie expiration. |
| `[http-only]` | bool | no | Whether the cookie is HTTP-only. |
| `[secure]` | bool | no | Whether the cookie is secure. |
| `[domain]` | string | no | Cookie domain. |
| `[path]` | string | no | Cookie path. |
| `[same-site]` | string | no | Cookie SameSite mode: Strict, Lax, None, or Unspecified. |

## [response.headers.set]

Sets one or more response headers from key/value child nodes.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Response header name and value. Can be repeated. |

## [response.status.set]

Overrides the HTTP status code returned to the caller (e.g. 201 Created, 404 Not Found, 500 Internal Error).

* **Value** (`http-status-code,integer,number`), required: HTTP status code to set

