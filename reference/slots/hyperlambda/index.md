---
title: hyperlambda.* slots
description: The 1 slots named hyperlambda.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [hyperlambda.verify-slots]

Verifies that all slots referenced in executable statement position of the specified Hyperlambda exist.

* **Value** (`hyperlambda`), optional: Hyperlambda text to verify; alternatively supply an already parsed lambda as children
* **Returns**: Resolves to true when every invocation is statically valid; otherwise lists missing slot names and invalid-invocation diagnostics as child nodes

Guide: [How to use [hyperlambda.verify-slots]](/plugins/magic.lambda.hyperlambda/#how-to-use-hyperlambdaverify-slots)

