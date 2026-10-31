---
title: Core keywords
description: The 89 slots that make up the core keywords in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [add]

Appends source nodes to selected destination containers.

* **Value** (`node-list,single-object`), required: Expression selecting destination container node or nodes whose children should receive the source nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location. Can be repeated. |

Guide: [How to use [add]](/plugins/magic.lambda/nodes/#how-to-use-add)

## [and]

Returns true if all children evaluate to true.

* **Returns**: Resolves to true if all operands evaluate to true

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable operand returning a boolean value. |

Guide: [How to use [and]](/plugins/magic.lambda/conditions/#how-to-use-and)

## [apply]

Stamps a template lambda with values from child argument nodes, producing one fully-substituted output per [.dp].

* **Value** (`template,lambda-tree`), required: Expression selecting the template node or nodes to transform
* **Returns**: Resolves to the transformed template nodes after applying the supplied arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Template replacement node matched by name; its value and children replace placeholders named {name}. Can be repeated. |

Guide: [How to use [apply]](/plugins/magic.lambda/types/#how-to-use-apply)

## [case]

Evaluates a single case branch inside [switch].

* **Value** (`switch-value`), required: Case value to match against the [switch] input value

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Case branch body executed by the parent [switch]. Can be repeated. |

* **Constraint** (ParentMustBe): Parent node must have the listed slot name (`[switch]`)

## [compose]

Builds an expression at runtime by concatenating the evaluated child node values; useful for dynamic node selection.

* **Returns**: Resolves to the composed expression

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Expression segment evaluated and joined into the resulting expression. Can be repeated. |

Guide: [How to use [compose]](/plugins/magic.lambda/executing/#how-to-use-compose)

## [context]

Creates a named stack context object retrievable with [get-context] while evaluating a lambda block.

* **Value** (`context-name`), required: Context name to create on the stack while evaluating the lambda block
* **Scope**: provides `context` - Creates a named context scope retrievable by [get-context] using the same input value

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Body evaluated while the context value is scoped. |
| `[value]` | object | yes | Value stored in the named stack context. |

Guide: [How to use [context]](/plugins/magic.lambda/types/#how-to-use-context)

## [convert]

Coerces a value to a different CLR type; useful for parsing strings into numbers, dates, booleans, or other strongly-typed values.

* **Value** (`single-object`), required: Expression selecting the value to convert
* **Returns**: Resolves to the value converted to the requested type

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | yes | Target Hyperlambda type name. |

Guide: [How to use [convert]](/plugins/magic.lambda/types/#how-to-use-convert)

## [csv2lambda]

Transforms CSV into a lambda hierarchy.

* **Value** (`csv`), required: CSV text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes; each child is one CSV row containing column-named values

| Argument | Type | Required | Description |
|---|---|---|---|
| `[null-value]` | string | no | String used to represent null values. Default: `[NULL]`. |
| `[types]` | lambda | no | Column type conversions keyed by column name. |
| `[types]` / _any node name_ | string | yes | Type name for the column. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One CSV record returned as a child node; column values appear as named children keyed by the header column name. Can be repeated. |
| _unnamed child node_ / _any node name_ | string | no | CSV column value; child name is the header column name. Can be repeated. |

Guide: [How to use [csv2lambda]](/plugins/magic.lambda.csv/#how-to-use-csv2lambda)

## [default]

Evaluates the default branch inside [switch].

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Default branch body executed by the parent [switch]. Can be repeated. |

* **Constraint** (ParentMustBe): Parent node must have the listed slot name (`[switch]`)

## [else]

Evaluates its child lambda when every preceding [if] and [else-if] condition was false.

* **Scope**: provides `if`

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Fallback branch body evaluated when previous conditions fail. Can be repeated. |

* **Constraint** (PreviousSiblingMustBeOneOf): Previous sibling must be one of the listed slot names (`[if]`, `[else-if]`)

Guide: [How to use [else]](/plugins/magic.lambda/branching/#how-to-use-else)

## [else-if]

Evaluates the child lambda when its condition is true and no preceding [if]/[else-if] branch matched.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Condition node evaluated for truthiness. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

* **Constraint** (PreviousSiblingMustBeOneOf): Previous sibling must be one of the listed slot names (`[if]`, `[else-if]`)

Guide: [How to use [else-if]](/plugins/magic.lambda/branching/#how-to-use-else-if)

## [eq]

Returns true if two operands are equal.

* **Returns**: Resolves to true if the operands are equal

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [eq]](/plugins/magic.lambda/conditions/#how-to-use-eq)

## [eval]

Executes a lambda block; use it to run a node tree dynamically or to scope a group of statements.

* **Value** (`lambda-object,lambda-tree`), optional: Expression selecting the Hyperlambda nodes to evaluate; alternatively supply literal executable children

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated in order. Can be repeated. |

Guide: [How to use [eval]](/plugins/magic.lambda/executing/#how-to-use-eval)

## [execute]

Invokes a dynamic slot after unwrapping descendant expressions.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to invoke
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the dynamic slot as a child of [.arguments]. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot after descendant expressions are unwrapped. Can be repeated. |

Guide: [How to use [execute]](/plugins/magic.lambda.slots/#how-to-use-execute)

## [execute-file]

Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments].

* **Value** (`hyperlambda-file`), required: File path to execute
* **Returns**: Resolves to the executed file's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the executed file as a child of [.arguments]. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the executed Hyperlambda file. Can be repeated. |

Guide: [How to use [execute-file]](/plugins/magic.lambda.io/#how-to-use-execute-file)

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
| _any node name_ | lambda | yes | Predicate body evaluated once per selected node; the selected node is kept when the body returns true. Can be repeated. |

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
| _any node name_ | lambda | yes | Loop body evaluated once per selected node. Can be repeated. |

Guide: [How to use [for-each]](/plugins/magic.lambda/loops/#how-to-use-for-each)

## [fork]

Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately.

* **Scope**: provides `fork`

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child slot evaluated on the forked thread. Can be repeated. |

Guide: [How to use [fork]](/plugins/magic.lambda.threading/#how-to-use-fork)

## [format]

Formats a value using a .NET format string and optional culture; useful for currencies, dates, and number rendering.

* **Value** (`scalar`), required: Value to format
* **Returns**: Resolves to the formatted string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[culture]` | string | no | Optional culture name used when formatting. |
| `[pattern]` | string | yes | Composite format string. |

Guide: [How to use [format]](/plugins/magic.lambda/types/#how-to-use-format)

## [get-context]

Returns a stack value or context object from the current execution context.

* **Value** (`context-name`), required: Context name to retrieve
* **Returns**: Resolves to the requested stack value or context object
* **Scope**: requires `context` - Requires a named context created by [context] using the same input value

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
| _any node name_ | lambda | yes | Candidate value source evaluated until the first non-null value is produced. Can be repeated. |

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

## [html-decode]

HTML decodes the specified string.

* **Value** (`html-encoded`), required: HTML encoded text to decode
* **Returns**: Resolves to the decoded text

Guide: [How to use [html-decode]](/plugins/magic.lambda.html/#how-to-use-html-decode)

## [html2lambda]

Transforms HTML into a lambda hierarchy.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the parsed HTML hierarchy as child nodes

Guide: [How to use [html2lambda]](/plugins/magic.lambda.html/#how-to-use-html2lambda)

## [html2markdown]

Transforms HTML into Markdown.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the generated Markdown

| Argument | Type | Required | Description |
|---|---|---|---|
| `[code]` | bool | no | Whether code blocks should be emitted. Default: `true`. |
| `[images]` | bool | no | Whether images should be emitted. Default: `true`. |
| `[lists]` | bool | no | Whether lists should be emitted. Default: `true`. |
| `[url]` | string | no | Base URL used when resolving links. |

Guide: [How to use [html2markdown]](/plugins/magic.lambda.html/#how-to-use-html2markdown)

## [html2pdf]

Converts HTML into a PDF document.

* **Value** (`html`), required: HTML markup to convert
* **Returns**: Resolves to the generated PDF bytes

Guide: [How to use [html2pdf]](/plugins/magic.lambda.pdf/#how-to-use-html2pdf)

## [hyper2lambda]

Transforms Hyperlambda into a lambda hierarchy.

* **Value** (`hyperlambda`), required: Hyperlambda text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[comments]` | bool | no | Whether parser comment nodes should be preserved as [..] nodes with the comment text as value. Default: `false`. |

Guide: [How to use [hyper2lambda]](/plugins/magic.lambda.hyperlambda/#how-to-use-hyper2lambda)

## [if]

Evaluates the child lambda only if the condition is true; chain with [else-if] and [else] for additional branches.

* **Scope**: provides `if`

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Condition node evaluated for truthiness. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

Guide: [How to use [if]](/plugins/magic.lambda/branching/#how-to-use-if)

## [include]

Evaluates child slots and includes all returned nodes into each selected node.

* **Value** (`node-list`), required: Expression selecting the destination node or nodes to include into
* **Returns**: Resolves to the matched destination nodes after all returned child nodes have been included

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable body evaluated once per selected node; all returned child nodes are included into that selected node. Can be repeated. |

Guide: [How to use [include]](/plugins/magic.lambda/nodes/#how-to-use-include)

## [insert-after]

Inserts nodes after the specified target node.

* **Value** (`node-list,single-object`), required: Expression selecting the target node or nodes to insert after

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location. Can be repeated. |

Guide: [How to use [insert-after]](/plugins/magic.lambda/nodes/#how-to-use-insert-after)

## [insert-before]

Inserts nodes before the specified target node.

* **Value** (`node-list,single-object`), required: Expression selecting the target node or nodes to insert before

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location. Can be repeated. |

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
| _any node name_ | object | no | Argument passed to the invoked lambda through its [.arguments] node. Can be repeated. |

Guide: [How to use [invoke]](/plugins/magic.lambda/executing/#how-to-use-invoke)

## [join]

Waits for one or more child [fork] operations to finish before proceeding.

* **Returns**: Resolves to the completed [fork] child nodes with evaluated body node values and children preserved
* **Scope**: provides `join`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[fork]` | lambda | yes | Fork body to start and wait for; evaluated body node values and children are preserved in the completed fork node. Can be repeated. |

Guide: [How to use [join]](/plugins/magic.data.common/#differences-between-join-and-where)

## [json2lambda]

Transforms JSON into a lambda hierarchy.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

Guide: [How to use [json2lambda]](/plugins/magic.lambda.json/#how-to-use-json2lambda-and-lambda2json)

## [json2lambda-stream]

Transforms JSON stream content into a lambda hierarchy.

* **Value** (`stream`), required: JSON stream to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[encoding]` | string | no | Text encoding used to read the JSON stream. Default: `utf-8`. |

Guide: [How to use [json2lambda-stream]](/plugins/magic.lambda.json/#how-to-use-json2lambda-stream)

## [json2yaml]

Transforms JSON into YAML.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the generated YAML string

Guide: [How to use [json2yaml]](/plugins/magic.lambda.json/#how-to-use-yaml2json-and-json2yaml)

## [lambda2csv]

Transforms a lambda hierarchy into CSV.

* **Value** (`node-list`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the CSV content in value and column type nodes as children

| Argument | Type | Required | Description |
|---|---|---|---|
| `[null-value]` | string | no | String used to represent null values. Default: `[NULL]`. |

Guide: [How to use [lambda2csv]](/plugins/magic.lambda.csv/#how-to-use-lambda2csv)

## [lambda2html]

Transforms a lambda hierarchy into HTML.

* **Value** (`html-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated HTML markup

Guide: [How to use [lambda2html]](/plugins/magic.lambda.html/#how-to-use-lambda2html)

## [lambda2hyper]

Transforms a lambda hierarchy into Hyperlambda.

* **Value** (`lambda-tree,node-list`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated Hyperlambda source

| Argument | Type | Required | Description |
|---|---|---|---|
| `[comments]` | bool | no | Whether generated Hyperlambda should include comments. Default: `false`. |

Guide: [How to use [lambda2hyper]](/plugins/magic.lambda.hyperlambda/#how-to-use-lambda2hyper)

## [lambda2json]

Transforms a lambda hierarchy into JSON.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated JSON string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | bool | no | Whether to pretty-print the JSON output. Default: `false`. |

Guide: [How to use [lambda2json]](/plugins/magic.lambda.json/#how-to-use-json2lambda-and-lambda2json)

## [lambda2xml]

Converts a lambda object to an XML fragment or document.

* **Value** (`xml-tree`), required: Expression selecting a SINGLE lambda root to transform (XML has exactly one document root)
* **Returns**: Resolves to the generated XML string

Guide: [How to use [lambda2xml]](/plugins/magic.lambda.xml/#how-to-use-lambda2xml)

## [lambda2yaml]

Transforms a lambda hierarchy into YAML.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the generated YAML string

Guide: [How to use [lambda2yaml]](/plugins/magic.lambda.json/#how-to-use-yaml2lambda-and-lambda2yaml)

## [lt]

Returns true if the first operand is less than the second operand.

* **Returns**: Resolves to true if the first operand is less than the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [lt]](/plugins/magic.lambda/conditions/#how-to-use-lt)

## [lte]

Returns true if the first operand is less than or equal to the second operand.

* **Returns**: Resolves to true if the first operand is less than or equal to the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [lte]](/plugins/magic.lambda/conditions/#how-to-use-lte)

## [map]

Maps selected nodes into a new result set using the child lambda.

* **Value** (`node-list`), required: Expression selecting the nodes to map
* **Returns**: Resolves to one mapped output item per selected node, using the value or nodes returned by the child lambda

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Mapper body evaluated once per selected node; each returned value becomes a [.] node and returned child nodes are added to the mapped result. Can be repeated. |

Guide: [How to use [map]](/plugins/magic.lambda/loops/#how-to-use-map)

## [markdown2html]

Transforms Markdown into HTML.

* **Value** (`markdown`), required: Markdown text to transform
* **Returns**: Resolves to the HTML in value and any YAML front matter as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[media]` | bool | no | Whether media link extensions should be enabled. |

Guide: [How to use [markdown2html]](/plugins/magic.lambda.html/#how-to-use-markdown2html)

## [mt]

Returns true if the first operand is greater than the second operand.

* **Returns**: Resolves to true if the first operand is greater than the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [mt]](/plugins/magic.lambda/conditions/#how-to-use-mt)

## [mte]

Returns true if the first operand is greater than or equal to the second operand.

* **Returns**: Resolves to true if the first operand is greater than or equal to the second operand

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [mte]](/plugins/magic.lambda/conditions/#how-to-use-mte)

## [neq]

Returns true if two operands are not equal.

* **Returns**: Resolves to true if the operands are not equal

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [neq]](/plugins/magic.lambda/conditions/#how-to-use-neq)

## [not]

Negates a boolean expression.

* **Returns**: Resolves to true if the operand evaluates to false

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable operand returning a boolean value. |

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
| _any node name_ | lambda | yes | Executable operand returning a boolean value. |

Guide: [How to use [or]](/plugins/magic.lambda/conditions/#how-to-use-or)

## [pdf2text]

Extracts text from a PDF file or stream.

* **Value** (`pdf-file,pdf-content,binary-content`), required: PDF file path, bytes, or stream to extract text from
* **Returns**: Returns extracted text in value or, when preserving pages, one child node per page

| Argument | Type | Required | Description |
|---|---|---|---|
| `[preserve-pages]` | bool | no | Whether to return one child node per page instead of one combined value. Default: `false`. |

Guide: [How to use [pdf2text]](/plugins/magic.lambda.pdf/#how-to-use-pdf2text)

## [reference]

Returns the first matched node as a live reference so callers can mutate it in place rather than copy its value.

* **Value** (`single-object`), required: Expression selecting the node to reference
* **Returns**: Resolves to a reference to the first matching node value

Guide: [How to use [reference]](/plugins/magic.lambda/nodes/#how-to-use-reference)

## [remove-nodes]

Removes nodes from the lambda graph.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes to remove

Guide: [How to use [remove-nodes]](/plugins/magic.lambda/nodes/#how-to-use-remove-nodes)

## [return]

Returns a value, expression result, or child nodes to the nearest caller.

* **Value** (`return-value,node-list`), optional: Value or expression to return when no child nodes are supplied; one expression match returns its value, multiple matches return cloned nodes
* **Returns**: Resolves to the supplied value and/or returned child nodes captured by the nearest caller

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Child node forwarded to the nearest caller without evaluation; when children exist, all children are returned as-is. Can be repeated. |

## [return-nodes]

Returns child nodes or evaluated nodes to the nearest caller.

* **Value** (`node-list`), optional: Expression evaluating to the nodes to return; omit to return the literal child nodes instead
* **Returns**: Returns child nodes to the nearest caller

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node. Can be repeated. |

Guide: [How to use [return-nodes]](/plugins/magic.lambda.slots/#how-to-use-return-nodes)

## [return-value]

Returns a value to the caller.

* **Value** (`return-value`), required: Value to return to the nearest caller
* **Returns**: Resolves to a value to the caller

Guide: [How to use [return-value]](/plugins/magic.lambda.slots/#how-to-use-return-value)

## [semaphore]

Serializes access to a critical section by name; only one thread at a time can enter a given semaphore.

* **Value** (`semaphore-name`), required: Semaphore name used to serialize access
* **Scope**: provides `semaphore`

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child lambda object evaluated while the named semaphore is held. Can be repeated. |

Guide: [How to use [semaphore]](/plugins/magic.lambda.threading/#how-to-use-semaphore)

## [set-name]

Sets the name of matching nodes.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose name should be changed

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Single source child evaluated to a string; the resolved value becomes the new node name. Omit to set the name to null. |

Guide: [How to use [set-name]](/plugins/magic.lambda/nodes/#how-to-use-set-name)

## [set-value]

Sets node values in the lambda graph.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose value should be changed

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Single source child evaluated before its value is consumed; omit to set the destination to null. |

Guide: [How to use [set-value]](/plugins/magic.lambda/nodes/#how-to-use-set-value)

## [set-x]

Sets node values without evaluating expressions in the source.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose value should be changed

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Single source child evaluated before its value is consumed; omit to set the destination to null. |

Guide: [How to use [set-x]](/plugins/magic.lambda/nodes/#how-to-use-set-x)

## [signal]

Invokes a dynamic slot created with [slots.create], passing child nodes as its arguments.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to invoke
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the dynamic slot as a child of [.arguments]. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot. Can be repeated. |

Guide: [How to use [signal]](/plugins/magic.lambda.slots/#how-to-use-signal)

## [sleep]

Delays execution for the specified number of milliseconds.

* **Value** (`timeout-ms,integer,number`), required: Delay in milliseconds

Guide: [How to use [sleep]](/plugins/magic.lambda.threading/#how-to-use-sleep)

## [sort]

Sorts selected nodes using the child lambda as a comparer.

* **Value** (`node-list`), required: Expression selecting the nodes to sort
* **Returns**: Resolves to the sorted nodes selected by the expression as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Comparer body evaluated with [.lhs], [.rhs], and [.result] injected. Can be repeated. |

Guide: [How to use [sort]](/plugins/magic.lambda/types/#how-to-use-sort)

## [switch]

Evaluates one of several branches based on the input value.

* **Value** (`switch-value`), required: Value to compare against the child [case] values

| Argument | Type | Required | Description |
|---|---|---|---|
| `[case]` | object | yes | Case branch matching the switch value. Can be repeated. |
| `[case]` / _any node name_ | lambda | yes | Branch body executed when the case matches. Can be repeated. |
| `[default]` | lambda | no | Fallback branch when no case matches. |
| `[default]` / _any node name_ | lambda | yes | Fallback branch body. Can be repeated. |

* **Constraint** (OnlyChildren): Only the listed child names are accepted (`[case]`, `[default]`)

Guide: [How to use [switch]](/plugins/magic.lambda/branching/#how-to-use-switch)

## [throw]

Aborts execution by throwing an exception with the given message; optionally attach status code and public flag.

* **Value** (`exception-message,text`), optional: Exception message to throw

| Argument | Type | Required | Description |
|---|---|---|---|
| `[field]` | string | no | Optional form field or control ID associated with the exception. |
| `[public]` | bool | no | Whether the exception message may be returned to clients. Default: `false`. |
| `[status]` | int | no | HTTP status code associated with the exception. Default: `500`. |

Guide: [How to use [throw]](/plugins/magic.lambda/exceptions/#how-to-use-throw)

## [time]

Constructs a TimeSpan value from child nodes.

* **Returns**: Resolves to the constructed TimeSpan value

| Argument | Type | Required | Description |
|---|---|---|---|
| `[days]` | int | no | Number of days. Default: `0`. |
| `[hours]` | int | no | Number of hours. Default: `0`. |
| `[milliseconds]` | int | no | Number of milliseconds. Default: `0`. |
| `[minutes]` | int | no | Number of minutes. Default: `0`. |
| `[seconds]` | int | no | Number of seconds. Default: `0`. |

Guide: [How to use [time]](/plugins/magic.lambda.dates/#how-to-use-time)

## [try]

Evaluates the protected body; pair with [.catch] to handle exceptions and/or [.finally] to always run cleanup.

* **Scope**: provides `try`

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Protected body evaluated by [try]. Can be repeated. |

* **Constraint** (NextSiblingMustBeOneOf): Must be followed by [.catch] and/or [.finally]; a bare [try] is a no-op because uncaught exceptions re-throw and [.finally] alone would run regardless (`[.catch]`, `[.finally]`)

Guide: [How to use [try]](/plugins/magic.lambda/exceptions/#how-to-use-try)

## [try-signal]

Invokes a dynamic slot if it exists and ignores missing slots.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to try invoking
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the dynamic slot as a child of [.arguments]. Can be repeated. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot. Can be repeated. |

Guide: [How to use [try-signal]](/plugins/magic.lambda.slots/#how-to-use-try-signal)

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
| `[apply-lists]` | bool | no | Whether list results should be applied while unwrapping. Default: `false`. |

Guide: [How to use [unwrap]](/plugins/magic.lambda/nodes/#how-to-use-unwrap)

## [version]

Returns the Magic Cloud version to the caller.

* **Returns**: Resolves to the Magic Cloud version

## [vocabulary]

Lists available compiled slots.

* **Value** (`slot-name`), optional: Optional prefix filter for slot names
* **Returns**: Resolves to available slot names as child nodes

Guide: [How to use [vocabulary]](/plugins/magic.lambda/types/#how-to-use-vocabulary)

## [while]

Repeats execution while a condition is true.

* **Scope**: provides `while`

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Condition node evaluated for truthiness. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

Guide: [How to use [while]](/plugins/magic.lambda/loops/#how-to-use-while)

## [whitelist]

Evaluates a lambda with a restricted whitelist of allowed slots.

* **Returns**: Resolves to the evaluated lambda's value result and any returned child nodes
* **Scope**: provides `whitelist`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Executable lambda block. |
| `[vocabulary]` | lambda | yes | Allowed slot names for the restricted evaluation scope. |
| `[vocabulary]` / _any node name_ | string | yes | Allowed native slot name (e.g. add, set-value, if) that the body is permitted to invoke. Can be repeated. |

Guide: [How to use [whitelist]](/plugins/magic.lambda.io/#restricting-file-access-with-whitelist)

## [xml2lambda]

Transforms XML into a lambda hierarchy.

* **Value** (`xml`), required: XML text to transform
* **Returns**: Resolves to the parsed XML hierarchy as child nodes; attributes are emitted as @name child nodes, text as #text child nodes, and comments/whitespace-only text nodes are omitted

Guide: [How to use [xml2lambda]](/plugins/magic.lambda.xml/#how-to-use-xml2lambda)

## [yaml2json]

Transforms YAML into JSON.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the generated JSON string

Guide: [How to use [yaml2json]](/plugins/magic.lambda.json/#how-to-use-yaml2json-and-json2yaml)

## [yaml2lambda]

Transforms YAML into a lambda hierarchy.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

Guide: [How to use [yaml2lambda]](/plugins/magic.lambda.json/#how-to-use-yaml2lambda-and-lambda2yaml)

## [yield]

Returns multiple child nodes or evaluated nodes to the caller.

* **Returns**: Returns child nodes to the caller

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node after descendant expressions are unwrapped. Can be repeated. |

