---
title: "sql.* slots"
description: "The 4 slots named sql.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

4 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`sql.create`](/reference/slots/sql/sql.create/) | Builds a parameterized INSERT SQL statement. |
| [`sql.delete`](/reference/slots/sql/sql.delete/) | Builds a parameterized DELETE SQL statement; include a [where] child unless intentionally deleting every row in the table. |
| [`sql.read`](/reference/slots/sql/sql.read/) | Builds a parameterized SELECT SQL statement. |
| [`sql.update`](/reference/slots/sql/sql.update/) | Builds a parameterized UPDATE SQL statement; use [where] to constrain affected rows. |

