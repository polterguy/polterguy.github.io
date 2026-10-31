---
title: magic.lambda.slots slot reference
description: Every slot in magic.lambda.slots with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.slots](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.slots). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.slots](/plugins/magic.lambda.slots/)._

## [execute]

Invokes a dynamic slot after unwrapping descendant expressions.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to invoke
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

Guide: [How to use [execute]](/plugins/magic.lambda.slots/#how-to-use-execute)

## [function]

Creates a dynamic slot that can be invoked with [signal].

Aliases: **[slots.create]**

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to create

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | lambda | yes | Executable child slot stored as the dynamic slot body |

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

Guide: [How to use [function]](/plugins/magic.lambda.slots/#how-to-use-slotscreate)

## [return]

Returns a value, expression result, or child nodes to the nearest caller.

* **Value** (`return-value,node-list`), optional: Value or expression to return when no child nodes are supplied; one expression match returns its value, multiple matches return cloned nodes
* **Returns**: Resolves to the supplied value and/or returned child nodes captured by the nearest caller

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | no | Child node forwarded to the nearest caller without evaluation; when children exist, all children are returned as-is |

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

## [return-nodes]

Returns child nodes or evaluated nodes to the nearest caller.

* **Value** (`node-list`), optional: Expression evaluating to the nodes to return; omit to return the literal child nodes instead
* **Returns**: Returns child nodes to the nearest caller

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | lambda | no | Returned child node |

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

Guide: [How to use [return-nodes]](/plugins/magic.lambda.slots/#how-to-use-return-nodes)

## [return-value]

Returns a value to the caller.

* **Value** (`return-value`), required: Value to return to the nearest caller
* **Returns**: Resolves to a value to the caller

Guide: [How to use [return-value]](/plugins/magic.lambda.slots/#how-to-use-return-value)

## [signal]

Invokes a dynamic slot created with [slots.create], passing child nodes as its arguments.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to invoke
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

Guide: [How to use [signal]](/plugins/magic.lambda.slots/#how-to-use-signal)

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

## [try-signal]

Invokes a dynamic slot if it exists and ignores missing slots.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to try invoking
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

Guide: [How to use [try-signal]](/plugins/magic.lambda.slots/#how-to-use-try-signal)

## [yield]

Returns multiple child nodes or evaluated nodes to the caller.

* **Returns**: Returns child nodes to the caller

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | lambda | no | Returned child node after descendant expressions are unwrapped |

| Returned node | Type | Description |
|---|---|---|
| `[*]` | object |  |
| `[.lambda]` | lambda | Executable dynamic slot body |
| `[*]` | lambda |  |

