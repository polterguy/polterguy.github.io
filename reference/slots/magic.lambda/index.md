---
title: magic.lambda slot reference
description: Every slot in magic.lambda with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda](/plugins/magic.lambda/)._

## [add]

Appends source nodes to selected destination containers.

* **Value** (`node-list,single-object`), required: Expression selecting destination container node or nodes whose children should receive the source nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location |

Guide: [How to use [add]](/plugins/magic.lambda/nodes/#how-to-use-add)

## [and]

Returns true if all children evaluate to true.

* **Returns**: Resolves to true if all operands evaluate to true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [and]](/plugins/magic.lambda/conditions/#how-to-use-and)

## [apply]

Stamps a template lambda with values from child argument nodes, producing one fully-substituted output per [.dp].

* **Value** (`template,lambda-tree`), required: Expression selecting the template node or nodes to transform
* **Returns**: Resolves to the transformed template nodes after applying the supplied arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | no | Template replacement node matched by name; its value and children replace placeholders named {name} |

Guide: [How to use [apply]](/plugins/magic.lambda/types/#how-to-use-apply)

## [case]

Evaluates a single case branch inside [switch].

* **Value** (`switch-value`), required: Case value to match against the [switch] input value

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

## [compose]

Builds an expression at runtime by concatenating the evaluated child node values; useful for dynamic node selection.

* **Returns**: Resolves to the composed expression

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | string | yes | Expression segment evaluated and joined into the resulting expression |

Guide: [How to use [compose]](/plugins/magic.lambda/executing/#how-to-use-compose)

## [context]

Creates a named stack context object retrievable with [get-context] while evaluating a lambda block.

* **Value** (`context-name`), required: Context name to create on the stack while evaluating the lambda block

| Argument | Type | Required | Description |
|---|---|---|---|
| `[value]` | object | yes | Value stored in the named stack context |

Guide: [How to use [context]](/plugins/magic.lambda/types/#how-to-use-context)

## [convert]

Coerces a value to a different CLR type; useful for parsing strings into numbers, dates, booleans, or other strongly-typed values.

* **Value** (`single-object`), required: Expression selecting the value to convert
* **Returns**: Resolves to the value converted to the requested type

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | yes | Target Hyperlambda type name |

Guide: [How to use [convert]](/plugins/magic.lambda/types/#how-to-use-convert)

## [default]

Evaluates the default branch inside [switch].


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

## [else]

Evaluates its child lambda when every preceding [if] and [else-if] condition was false.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [else]](/plugins/magic.lambda/branching/#how-to-use-else)

## [else-if]

Evaluates the child lambda when its condition is true and no preceding [if]/[else-if] branch matched.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [else-if]](/plugins/magic.lambda/branching/#how-to-use-else-if)

## [eq]

Returns true if two operands are equal.

* **Returns**: Resolves to true if the operands are equal

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | yes | Operand evaluated before comparison |

Guide: [How to use [eq]](/plugins/magic.lambda/conditions/#how-to-use-eq)

## [eval]

Executes a lambda block; use it to run a node tree dynamically or to scope a group of statements.

* **Value** (`lambda-object,lambda-tree`), optional: Expression selecting the Hyperlambda nodes to evaluate; alternatively supply literal executable children

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [eval]](/plugins/magic.lambda/executing/#how-to-use-eval)

## [exists]

Returns true if the specified node or expression exists.

* **Value** (`node-list,single-object`), required: Expression selecting the nodes to test for
* **Returns**: Returns true if the expression resolves to one or more nodes

Guide: [How to use [exists]](/plugins/magic.lambda/nodes/#how-to-use-exists)

## [filter]

Filters selected nodes using the child lambda as a predicate.

* **Value** (`node-list`), required: Expression selecting the nodes to filter
* **Returns**: Resolves to clones of the selected nodes whose predicate body returns true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Predicate body evaluated once per selected node; the selected node is kept when the body returns true |

Guide: [How to use [filter]](/plugins/magic.lambda/nodes/#how-to-use-filter)

## [floatArray2bytes]

Serializes a sequence of float values into raw bytes; useful for embedding vectors or feeding binary APIs.

* **Value** (`float-list`), required: Float values to convert to bytes
* **Returns**: Resolves to the float array converted to bytes

Guide: [How to use [floatArray2bytes]](/plugins/magic.lambda/types/#how-to-use-floatarray2bytes)

## [for-each]

Iterates over the nodes matching the expression and evaluates the child lambda once per node as [.dp].

* **Value** (`node-list`), required: Expression selecting the nodes to iterate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [for-each]](/plugins/magic.lambda/loops/#how-to-use-for-each)

## [format]

Formats a value using a .NET format string and optional culture; useful for currencies, dates, and number rendering.

* **Value** (`scalar`), required: Value to format
* **Returns**: Resolves to the formatted string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[culture]` | string | no | Optional culture name used when formatting |
| `[pattern]` | string | yes | Composite format string |

Guide: [How to use [format]](/plugins/magic.lambda/types/#how-to-use-format)

## [get-context]

Returns a stack value or context object from the current execution context.

* **Value** (`context-name`), required: Context name to retrieve
* **Returns**: Resolves to the requested stack value or context object

Guide: [How to use [get-context]](/plugins/magic.lambda/nodes/#how-to-use-get-context)

## [get-count]

Returns the number of matching nodes.

* **Value** (`node-list`), required: Expression selecting the nodes to count
* **Returns**: Resolves to the number of nodes matched by the expression

Guide: [How to use [get-count]](/plugins/magic.lambda/nodes/#how-to-use-get-count)

## [get-first-value]

Returns the first non-null value produced by candidate child nodes.

* **Returns**: Resolves to the first non-null value produced by the candidate child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Candidate value source evaluated until the first non-null value is produced |

Guide: [How to use [get-first-value]](/plugins/magic.lambda/nodes/#how-to-use-get-first-value)

## [get-name]

Returns the name of the first matching node.

* **Value** (`single-object`), required: Expression selecting the node whose name should be retrieved
* **Returns**: Resolves to the name of the first matching node

Guide: [How to use [get-name]](/plugins/magic.lambda/nodes/#how-to-use-get-name)

## [get-nodes]

Returns clones of every node matching the expression as children of the current node.

* **Value** (`node-list`), required: Expression selecting the nodes to retrieve
* **Returns**: Resolves to the nodes matched by the expression as child nodes

Guide: [How to use [get-nodes]](/plugins/magic.lambda/nodes/#how-to-use-get-nodes)

## [get-value]

Returns the value of the first matching node.

* **Value** (`single-object`), required: Expression selecting the node whose value should be retrieved
* **Returns**: Resolves to the value of the first matching node

Guide: [How to use [get-value]](/plugins/magic.lambda/nodes/#how-to-use-get-value)

## [if]

Evaluates the child lambda only if the condition is true; chain with [else-if] and [else] for additional branches.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [if]](/plugins/magic.lambda/branching/#how-to-use-if)

## [include]

Evaluates child slots and includes all returned nodes into each selected node.

* **Value** (`node-list`), required: Expression selecting the destination node or nodes to include into
* **Returns**: Resolves to the matched destination nodes after all returned child nodes have been included

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Executable body evaluated once per selected node; all returned child nodes are included into that selected node |

Guide: [How to use [include]](/plugins/magic.lambda/nodes/#how-to-use-include)

## [insert-after]

Inserts nodes after the specified target node.

* **Value** (`node-list,single-object`), required: Expression selecting the target node or nodes to insert after

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location |

Guide: [How to use [insert-after]](/plugins/magic.lambda/nodes/#how-to-use-insert-after)

## [insert-before]

Inserts nodes before the specified target node.

* **Value** (`node-list,single-object`), required: Expression selecting the target node or nodes to insert before

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location |

Guide: [How to use [insert-before]](/plugins/magic.lambda/nodes/#how-to-use-insert-before)

## [int2words]

Spells an integer out in English words (e.g. 557 becomes 'five hundred and fifty seven'); handy for invoices and cheques.

* **Value** (`integer,number`), required: Integer value to convert to words
* **Returns**: Resolves to the supplied integer written as words

Guide: [How to use [int2words]](/plugins/magic.lambda/types/#how-to-use-int2words)

## [invoke]

Invokes a lambda expression as a callable slot.

* **Value** (`lambda-object,lambda-tree`), required: Expression yielding the single lambda node to invoke
* **Returns**: Resolves to the invoked lambda's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | no | Argument passed to the invoked lambda through its [.arguments] node |

Guide: [How to use [invoke]](/plugins/magic.lambda/executing/#how-to-use-invoke)

## [lt]

Returns true if the first operand is less than the second operand.

* **Returns**: Resolves to true if the first operand is less than the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | yes | Operand evaluated before comparison |

Guide: [How to use [lt]](/plugins/magic.lambda/conditions/#how-to-use-lt)

## [lte]

Returns true if the first operand is less than or equal to the second operand.

* **Returns**: Resolves to true if the first operand is less than or equal to the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | yes | Operand evaluated before comparison |

Guide: [How to use [lte]](/plugins/magic.lambda/conditions/#how-to-use-lte)

## [map]

Maps selected nodes into a new result set using the child lambda.

* **Value** (`node-list`), required: Expression selecting the nodes to map
* **Returns**: Resolves to one mapped output item per selected node, using the value or nodes returned by the child lambda

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | yes | Mapper body evaluated once per selected node; each returned value becomes a [.] node and returned child nodes are added to the mapped result |

Guide: [How to use [map]](/plugins/magic.lambda/loops/#how-to-use-map)

## [mt]

Returns true if the first operand is greater than the second operand.

* **Returns**: Resolves to true if the first operand is greater than the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | yes | Operand evaluated before comparison |

Guide: [How to use [mt]](/plugins/magic.lambda/conditions/#how-to-use-mt)

## [mte]

Returns true if the first operand is greater than or equal to the second operand.

* **Returns**: Resolves to true if the first operand is greater than or equal to the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | yes | Operand evaluated before comparison |

Guide: [How to use [mte]](/plugins/magic.lambda/conditions/#how-to-use-mte)

## [neq]

Returns true if two operands are not equal.

* **Returns**: Resolves to true if the operands are not equal

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | yes | Operand evaluated before comparison |

Guide: [How to use [neq]](/plugins/magic.lambda/conditions/#how-to-use-neq)

## [not]

Negates a boolean expression.

* **Returns**: Resolves to true if the operand evaluates to false

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [not]](/plugins/magic.lambda/conditions/#how-to-use-not)

## [not-exists]

Returns true if the specified node or expression does not exist.

* **Value** (`node-list,single-object`), required: Expression selecting the nodes to test for
* **Returns**: Returns true if the expression resolves to no nodes

Guide: [How to use [not-exists]](/plugins/magic.lambda/nodes/#how-to-use-not-exists)

## [not-null]

Returns true if the specified node or expression is not null.

* **Value** (`node-list,single-object`), required: Expression selecting the value to test for null
* **Returns**: Returns true if the expression resolves to a non-null value

Guide: [How to use [not-null]](/plugins/magic.lambda/nodes/#how-to-use-not-null)

## [null]

Returns true if the specified node or expression is null.

* **Value** (`node-list,single-object`), required: Expression selecting the value to test for null
* **Returns**: Returns true if the expression resolves to a null value

Guide: [How to use [null]](/plugins/magic.lambda/nodes/#how-to-use-null)

## [or]

Returns true if any child expression evaluates to true.

* **Returns**: Resolves to true if any operand evaluates to true

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [or]](/plugins/magic.lambda/conditions/#how-to-use-or)

## [reference]

Returns the first matched node as a live reference so callers can mutate it in place rather than copy its value.

* **Value** (`single-object`), required: Expression selecting the node to reference
* **Returns**: Resolves to a reference to the first matching node value

Guide: [How to use [reference]](/plugins/magic.lambda/nodes/#how-to-use-reference)

## [remove-nodes]

Removes nodes from the lambda graph.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes to remove

Guide: [How to use [remove-nodes]](/plugins/magic.lambda/nodes/#how-to-use-remove-nodes)

## [set-name]

Sets the name of matching nodes.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose name should be changed

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | string | no | Single source child evaluated to a string; the resolved value becomes the new node name. Omit to set the name to null. |

Guide: [How to use [set-name]](/plugins/magic.lambda/nodes/#how-to-use-set-name)

## [set-value]

Sets node values in the lambda graph.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose value should be changed

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | no | Single source child evaluated before its value is consumed; omit to set the destination to null |

Guide: [How to use [set-value]](/plugins/magic.lambda/nodes/#how-to-use-set-value)

## [set-x]

Sets node values without evaluating expressions in the source.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose value should be changed

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | object | no | Single source child evaluated before its value is consumed; omit to set the destination to null |

Guide: [How to use [set-x]](/plugins/magic.lambda/nodes/#how-to-use-set-x)

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

## [sort]

Sorts selected nodes using the child lambda as a comparer.

* **Value** (`node-list`), required: Expression selecting the nodes to sort
* **Returns**: Resolves to the sorted nodes selected by the expression as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [sort]](/plugins/magic.lambda/types/#how-to-use-sort)

## [switch]

Evaluates one of several branches based on the input value.

* **Value** (`switch-value`), required: Value to compare against the child [case] values

| Argument | Type | Required | Description |
|---|---|---|---|
| `[case]` | object | yes | Case branch matching the switch value |
| `[default]` |  | no | Fallback branch when no case matches |

Guide: [How to use [switch]](/plugins/magic.lambda/branching/#how-to-use-switch)

## [throw]

Aborts execution by throwing an exception with the given message; optionally attach status code and public flag.

* **Value** (`exception-message,text`), optional: Exception message to throw

| Argument | Type | Required | Description |
|---|---|---|---|
| `[public]` | bool | no | Whether the exception message may be returned to clients |
| `[status]` | int | no | HTTP status code associated with the exception |
| `[field]` | string | no | Optional form field or control ID associated with the exception |

Guide: [How to use [throw]](/plugins/magic.lambda/exceptions/#how-to-use-throw)

## [try]

Evaluates the protected body; pair with [.catch] to handle exceptions and/or [.finally] to always run cleanup.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [try]](/plugins/magic.lambda/exceptions/#how-to-use-try)

## [type]

Returns the CLR type name of a value.

* **Value** (`single-object`), required: Expression selecting the value whose CLR type should be inspected
* **Returns**: Resolves to the runtime type name of the first matching value

Guide: [How to use [type]](/plugins/magic.lambda/types/#how-to-use-type)

## [types]

Lists every CLR type name recognized by Hyperlambda; useful when [convert] or [type] needs a valid target.

* **Returns**: Resolves to one child node per known CLR type name

Guide: [How to use [types]](/plugins/magic.lambda/types/#how-to-use-types)

## [unwrap]

Forward-evaluates expression values on the selected nodes, replacing them with their resolved values; commonly used before [signal] or [add].

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose expressions should be unwrapped

| Argument | Type | Required | Description |
|---|---|---|---|
| `[apply-lists]` | bool | no | Whether list results should be applied while unwrapping |

Guide: [How to use [unwrap]](/plugins/magic.lambda/nodes/#how-to-use-unwrap)

## [vocabulary]

Lists available compiled slots.

* **Value** (`slot-name`), optional: Optional prefix filter for slot names
* **Returns**: Resolves to available slot names as child nodes

Guide: [How to use [vocabulary]](/plugins/magic.lambda/types/#how-to-use-vocabulary)

## [while]

Repeats execution while a condition is true.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` |  | no |  |
| `[*]` |  | no |  |
| `[.lambda]` |  | no |  |
| `[*]` |  | yes | Condition node evaluated for truthiness |

Guide: [How to use [while]](/plugins/magic.lambda/loops/#how-to-use-while)

## [whitelist]

Evaluates a lambda with a restricted whitelist of allowed slots.

* **Returns**: Resolves to the evaluated lambda's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[vocabulary]` | string | yes | Allowed slot names for the restricted evaluation scope |

Guide: [How to use [whitelist]](/plugins/magic.lambda/types/#how-to-use-whitelist)

