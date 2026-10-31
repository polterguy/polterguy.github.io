---
title: date.* slots
description: The 6 slots named date.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [date.format]

Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging.

* **Value** (`date`), required: Date value to format
* **Returns**: Resolves to the formatted date string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string. |

Guide: [How to use [date.format]](/plugins/magic.lambda.dates/#how-to-use-dateformat)

## [date.from-unix]

Converts a Unix timestamp into a DateTime value.

* **Value** (`unix-timestamp,integer,number`), required: Unix timestamp to convert
* **Returns**: Resolves to the date represented by the supplied Unix timestamp

Guide: [How to use [date.from-unix]](/plugins/magic.lambda.dates/#how-to-use-datefrom-unix)

## [date.max]

Returns the maximum DateTime value.

* **Returns**: Resolves to the maximum supported DateTime value

Guide: [How to use [date.max]](/plugins/magic.lambda.dates/#how-to-use-datemax)

## [date.min]

Returns the minimum DateTime value.

* **Returns**: Resolves to the minimum supported DateTime value

Guide: [How to use [date.min]](/plugins/magic.lambda.dates/#how-to-use-datemin)

## [date.now]

Returns the current server time in UTC.

* **Returns**: Resolves to the current UTC date and time

Guide: [How to use [date.now]](/plugins/magic.lambda.dates/#how-to-use-datenow)

## [date.unix]

Returns the current UTC time as a Unix timestamp.

* **Returns**: Resolves to the current UTC Unix timestamp in milliseconds

Guide: [How to use [date.unix]](/plugins/magic.lambda.dates/#how-to-use-dateunix)

