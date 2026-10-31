---
title: magic.lambda.logging slot reference
description: Every slot in magic.lambda.logging with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.logging](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.logging). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.logging](/plugins/magic.lambda.logging/)._

## [log.capabilities]

Returns capabilities of the current log provider.

* **Returns**: Returns [can-filter] and [can-timeshift] capability nodes for the current log provider

## [log.count]

Returns the total number of log entries, optionally restricted to a single content type.

* **Value** (`content-type`), optional: Optional content type filter
* **Returns**: Resolves to the number of log entries matching the optional query

## [log.debug]

Writes a debug-level log entry; useful during development for high-volume diagnostic detail.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | string | no | Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment |

## [log.error]

Writes an error-level log entry; use for caught exceptions or failed operations that need follow-up.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

| Argument | Type | Required | Description |
|---|---|---|---|
| `[exception]` | string | no | Exception text attached to error and fatal log entries |

## [log.fatal]

Writes a fatal-level log entry; reserve for unrecoverable failures that warrant immediate attention.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

| Argument | Type | Required | Description |
|---|---|---|---|
| `[exception]` | string | no | Exception text attached to error and fatal log entries |

## [log.get]

Returns a log entry by ID.

* **Value** (`log-entry-id,integer,number`), required: ID of the log entry to retrieve
* **Returns**: Resolves to the log entry as child nodes

## [log.info]

Writes an informational log entry capturing routine, non-error events of interest.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | string | no | Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment |

## [log.query]

Returns recent log entries with most-recent-first ordering; supports optional content-type filtering and pagination.

* **Value** (`content-type`), optional: Optional content type filter
* **Returns**: Returns matching log entries as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Maximum number of log entries to return |
| `[from]` | object | no | Cursor or timestamp to query from |

## [log.timeshift]

Aggregates log entries into time buckets.

* **Value** (`log-search`), required: Search string or log entry type to aggregate over the last two weeks
* **Returns**: Returns one child node per day with [when] and [count] values for the time bucket

Guide: [How to use [log.timeshift]](/plugins/magic.lambda.logging/#how-to-use-logtimeshift)

