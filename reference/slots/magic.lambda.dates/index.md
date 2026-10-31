---
title: magic.lambda.dates slot reference
description: Every slot in magic.lambda.dates with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.dates](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.dates). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.dates](/plugins/magic.lambda.dates/)._

## [date.format]

Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging.

* **Value** (`date`), required: Date value to format
* **Returns**: Resolves to the formatted date string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string |

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

## [time]

Constructs a TimeSpan value from child nodes.

* **Returns**: Resolves to the constructed TimeSpan value

| Argument | Type | Required | Description |
|---|---|---|---|
| `[days]` | int | no | Number of days |
| `[hours]` | int | no | Number of hours |
| `[minutes]` | int | no | Number of minutes |
| `[seconds]` | int | no | Number of seconds |
| `[milliseconds]` | int | no | Number of milliseconds |

Guide: [How to use [time]](/plugins/magic.lambda.dates/#how-to-use-time)

## [time.format]

Formats a TimeSpan value.

* **Value** (`timespan`), required: Time span to format
* **Returns**: Resolves to the formatted time string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string |

Guide: [How to use [time.format]](/plugins/magic.lambda.dates/#how-to-use-timeformat)

## [time.total-milliseconds]

Returns the total milliseconds for a TimeSpan value.

* **Value** (`timespan`), required: Time span to measure
* **Returns**: Resolves to the total number of milliseconds in the supplied time span

Guide: [How to use [time.total-milliseconds]](/plugins/magic.lambda.dates/#how-to-use-timetotal-milliseconds)

