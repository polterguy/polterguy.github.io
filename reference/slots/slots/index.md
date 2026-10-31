---
title: slots.* slots
description: The 5 slots named slots.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [slots.create]

Creates a dynamic slot that can be invoked with [signal].

Aliases: **[function]**

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to create

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child slot stored as the dynamic slot body. Can be repeated. |

Guide: [How to use [slots.create]](/plugins/magic.lambda.slots/#how-to-use-slotscreate)

## [slots.delete]

Deletes a dynamic slot.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to delete

Guide: [How to use [slots.delete]](/plugins/magic.lambda.slots/#how-to-use-slotsdelete)

## [slots.exists]

Returns true if a dynamic slot exists.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to test for
* **Returns**: Returns true if the slot exists

Guide: [How to use [slots.exists]](/plugins/magic.lambda.slots/#how-to-use-slotsexists)

## [slots.get]

Returns a dynamic slot by name.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to retrieve
* **Returns**: Resolves to the dynamic slot lambda body as child nodes

Guide: [How to use [slots.get]](/plugins/magic.lambda.slots/#how-to-use-slotsget)

## [slots.vocabulary]

Lists dynamically created slots.

* **Value** (`dynamic-slot-name`), optional: Optional filter for dynamic slot names
* **Returns**: Resolves to available dynamic slot names as child nodes

Guide: [How to use [slots.vocabulary]](/plugins/magic.lambda.slots/#how-to-use-slotsvocabulary)

