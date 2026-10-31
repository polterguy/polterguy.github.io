---
title: time.* slots
description: The 2 slots named time.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [time.format]

Formats a TimeSpan value.

* **Value** (`timespan`), required: Time span to format
* **Returns**: Resolves to the formatted time string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string. |

Guide: [How to use [time.format]](/plugins/magic.lambda.dates/#how-to-use-timeformat)

## [time.total-milliseconds]

Returns the total milliseconds for a TimeSpan value.

* **Value** (`timespan`), required: Time span to measure
* **Returns**: Resolves to the total number of milliseconds in the supplied time span

Guide: [How to use [time.total-milliseconds]](/plugins/magic.lambda.dates/#how-to-use-timetotal-milliseconds)

