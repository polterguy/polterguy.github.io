---
title: slot.* slots
description: The 2 slots named slot.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [slot.description]

Returns the description for a single compiled slot.

* **Value** (`slot-name`), required: Name of the compiled slot to inspect
* **Returns**: Resolves to the description of the requested slot

Guide: [How to use [slot.description]](/plugins/magic.lambda/types/#how-to-use-slotdescription)

## [slot.signature]

Returns the documented input and output contract for a single compiled slot.

* **Value** (`slot-name`), required: Name of the compiled slot to inspect
* **Returns**: Resolves to input and output contract metadata for the requested slot

Guide: [How to use [slot.signature]](/plugins/magic.lambda/types/#how-to-use-slotsignature)

