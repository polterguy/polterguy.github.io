---
title: "log.* slots"
description: "The 9 slots named log.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

9 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`log.capabilities`](/reference/slots/log/log.capabilities/) | Returns capabilities of the current log provider. |
| [`log.count`](/reference/slots/log/log.count/) | Returns the total number of log entries, optionally restricted to a single content type. |
| [`log.debug`](/reference/slots/log/log.debug/) | Writes a debug-level log entry; useful during development for high-volume diagnostic detail. |
| [`log.error`](/reference/slots/log/log.error/) | Writes an error-level log entry; use for caught exceptions or failed operations that need follow-up. |
| [`log.fatal`](/reference/slots/log/log.fatal/) | Writes a fatal-level log entry; reserve for unrecoverable failures that warrant immediate attention. |
| [`log.get`](/reference/slots/log/log.get/) | Returns a log entry by ID. |
| [`log.info`](/reference/slots/log/log.info/) | Writes an informational log entry capturing routine, non-error events of interest. |
| [`log.query`](/reference/slots/log/log.query/) | Returns recent log entries with most-recent-first ordering; supports optional content-type filtering and pagination. |
| [`log.timeshift`](/reference/slots/log/log.timeshift/) | Aggregates log entries into time buckets. |

