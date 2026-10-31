---
title: "Core keywords"
description: "The 89 slots that make up the core keywords in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

89 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`add`](/reference/slots/core/add/) | Appends source nodes to selected destination containers. |
| [`and`](/reference/slots/core/and/) | Returns true if all children evaluate to true. |
| [`apply`](/reference/slots/core/apply/) | Stamps a template lambda with values from child argument nodes, producing one fully-substituted output per [.dp]. |
| [`case`](/reference/slots/core/case/) | Evaluates a single case branch inside [switch]. |
| [`compose`](/reference/slots/core/compose/) | Builds an expression at runtime by concatenating the evaluated child node values; useful for dynamic node selection. |
| [`context`](/reference/slots/core/context/) | Creates a named stack context object retrievable with [get-context] while evaluating a lambda block. |
| [`convert`](/reference/slots/core/convert/) | Coerces a value to a different CLR type; useful for parsing strings into numbers, dates, booleans, or other strongly-typed values. |
| [`csv2lambda`](/reference/slots/core/csv2lambda/) | Transforms CSV into a lambda hierarchy. |
| [`default`](/reference/slots/core/default/) | Evaluates the default branch inside [switch]. |
| [`else`](/reference/slots/core/else/) | Evaluates its child lambda when every preceding [if] and [else-if] condition was false. |
| [`else-if`](/reference/slots/core/else-if/) | Evaluates the child lambda when its condition is true and no preceding [if]/[else-if] branch matched. |
| [`eq`](/reference/slots/core/eq/) | Returns true if two operands are equal. |
| [`eval`](/reference/slots/core/eval/) | Executes a lambda block; use it to run a node tree dynamically or to scope a group of statements. |
| [`execute`](/reference/slots/core/execute/) | Invokes a dynamic slot after unwrapping descendant expressions. |
| [`execute-file`](/reference/slots/core/execute-file/) | Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]. |
| [`exists`](/reference/slots/core/exists/) | Returns true if the specified node or expression exists. |
| [`filter`](/reference/slots/core/filter/) | Filters selected nodes using the child lambda as a predicate. |
| [`floatArray2bytes`](/reference/slots/core/floatArray2bytes/) | Serializes a sequence of float values into raw bytes; useful for embedding vectors or feeding binary APIs. |
| [`for-each`](/reference/slots/core/for-each/) | Iterates over the nodes matching the expression and evaluates the child lambda once per node as [.dp]. |
| [`fork`](/reference/slots/core/fork/) | Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately. |
| [`format`](/reference/slots/core/format/) | Formats a value using a .NET format string and optional culture; useful for currencies, dates, and number rendering. |
| [`get-context`](/reference/slots/core/get-context/) | Returns a stack value or context object from the current execution context. |
| [`get-count`](/reference/slots/core/get-count/) | Returns the number of matching nodes. |
| [`get-first-value`](/reference/slots/core/get-first-value/) | Returns the first non-null value produced by candidate child nodes. |
| [`get-name`](/reference/slots/core/get-name/) | Returns the name of the first matching node. |
| [`get-nodes`](/reference/slots/core/get-nodes/) | Returns clones of every node matching the expression as children of the current node. |
| [`get-value`](/reference/slots/core/get-value/) | Returns the value of the first matching node. |
| [`html-decode`](/reference/slots/core/html-decode/) | HTML decodes the specified string. |
| [`html2lambda`](/reference/slots/core/html2lambda/) | Transforms HTML into a lambda hierarchy. |
| [`html2markdown`](/reference/slots/core/html2markdown/) | Transforms HTML into Markdown. |
| [`html2pdf`](/reference/slots/core/html2pdf/) | Converts HTML into a PDF document. |
| [`hyper2lambda`](/reference/slots/core/hyper2lambda/) | Transforms Hyperlambda into a lambda hierarchy. |
| [`if`](/reference/slots/core/if/) | Evaluates the child lambda only if the condition is true; chain with [else-if] and [else] for additional branches. |
| [`include`](/reference/slots/core/include/) | Evaluates child slots and includes all returned nodes into each selected node. |
| [`insert-after`](/reference/slots/core/insert-after/) | Inserts nodes after the specified target node. |
| [`insert-before`](/reference/slots/core/insert-before/) | Inserts nodes before the specified target node. |
| [`int2words`](/reference/slots/core/int2words/) | Spells an integer out in English words (e.g. 557 becomes 'five hundred and fifty seven'); handy for invoices and cheques. |
| [`invoke`](/reference/slots/core/invoke/) | Invokes a lambda expression as a callable slot. |
| [`join`](/reference/slots/core/join/) | Waits for one or more child [fork] operations to finish before proceeding. |
| [`json2lambda`](/reference/slots/core/json2lambda/) | Transforms JSON into a lambda hierarchy. |
| [`json2lambda-stream`](/reference/slots/core/json2lambda-stream/) | Transforms JSON stream content into a lambda hierarchy. |
| [`json2yaml`](/reference/slots/core/json2yaml/) | Transforms JSON into YAML. |
| [`lambda2csv`](/reference/slots/core/lambda2csv/) | Transforms a lambda hierarchy into CSV. |
| [`lambda2html`](/reference/slots/core/lambda2html/) | Transforms a lambda hierarchy into HTML. |
| [`lambda2hyper`](/reference/slots/core/lambda2hyper/) | Transforms a lambda hierarchy into Hyperlambda. |
| [`lambda2json`](/reference/slots/core/lambda2json/) | Transforms a lambda hierarchy into JSON. |
| [`lambda2xml`](/reference/slots/core/lambda2xml/) | Converts a lambda object to an XML fragment or document. |
| [`lambda2yaml`](/reference/slots/core/lambda2yaml/) | Transforms a lambda hierarchy into YAML. |
| [`lt`](/reference/slots/core/lt/) | Returns true if the first operand is less than the second operand. |
| [`lte`](/reference/slots/core/lte/) | Returns true if the first operand is less than or equal to the second operand. |
| [`map`](/reference/slots/core/map/) | Maps selected nodes into a new result set using the child lambda. |
| [`markdown2html`](/reference/slots/core/markdown2html/) | Transforms Markdown into HTML. |
| [`mt`](/reference/slots/core/mt/) | Returns true if the first operand is greater than the second operand. |
| [`mte`](/reference/slots/core/mte/) | Returns true if the first operand is greater than or equal to the second operand. |
| [`neq`](/reference/slots/core/neq/) | Returns true if two operands are not equal. |
| [`not`](/reference/slots/core/not/) | Negates a boolean expression. |
| [`not-exists`](/reference/slots/core/not-exists/) | Returns true if the specified node or expression does not exist. |
| [`not-null`](/reference/slots/core/not-null/) | Returns true if the specified node or expression is not null. |
| [`null`](/reference/slots/core/null/) | Returns true if the specified node or expression is null. |
| [`or`](/reference/slots/core/or/) | Returns true if any child expression evaluates to true. |
| [`pdf2text`](/reference/slots/core/pdf2text/) | Extracts text from a PDF file or stream. |
| [`reference`](/reference/slots/core/reference/) | Returns the first matched node as a live reference so callers can mutate it in place rather than copy its value. |
| [`remove-nodes`](/reference/slots/core/remove-nodes/) | Removes nodes from the lambda graph. |
| [`return`](/reference/slots/core/return/) | Returns a value, expression result, or child nodes to the nearest caller. |
| [`return-nodes`](/reference/slots/core/return-nodes/) | Returns child nodes or evaluated nodes to the nearest caller. |
| [`return-value`](/reference/slots/core/return-value/) | Returns a value to the caller. |
| [`semaphore`](/reference/slots/core/semaphore/) | Serializes access to a critical section by name; only one thread at a time can enter a given semaphore. |
| [`set-name`](/reference/slots/core/set-name/) | Sets the name of matching nodes. |
| [`set-value`](/reference/slots/core/set-value/) | Sets node values in the lambda graph. |
| [`set-x`](/reference/slots/core/set-x/) | Sets node values without evaluating expressions in the source. |
| [`signal`](/reference/slots/core/signal/) | Invokes a dynamic slot created with [slots.create], passing child nodes as its arguments. |
| [`sleep`](/reference/slots/core/sleep/) | Delays execution for the specified number of milliseconds. |
| [`sort`](/reference/slots/core/sort/) | Sorts selected nodes using the child lambda as a comparer. |
| [`switch`](/reference/slots/core/switch/) | Evaluates one of several branches based on the input value. |
| [`throw`](/reference/slots/core/throw/) | Aborts execution by throwing an exception with the given message; optionally attach status code and public flag. |
| [`time`](/reference/slots/core/time/) | Constructs a TimeSpan value from child nodes. |
| [`try`](/reference/slots/core/try/) | Evaluates the protected body; pair with [.catch] to handle exceptions and/or [.finally] to always run cleanup. |
| [`try-signal`](/reference/slots/core/try-signal/) | Invokes a dynamic slot if it exists and ignores missing slots. |
| [`type`](/reference/slots/core/type/) | Returns the CLR type name of a value. |
| [`types`](/reference/slots/core/types/) | Lists every CLR type name recognized by Hyperlambda; useful when [convert] or [type] needs a valid target. |
| [`unwrap`](/reference/slots/core/unwrap/) | Forward-evaluates expression values on the selected nodes, replacing them with their resolved values; commonly used before [signal] or [add]. |
| [`version`](/reference/slots/core/version/) | Returns the Magic Cloud version to the caller. |
| [`vocabulary`](/reference/slots/core/vocabulary/) | Lists available compiled slots. |
| [`while`](/reference/slots/core/while/) | Repeats execution while a condition is true. |
| [`whitelist`](/reference/slots/core/whitelist/) | Evaluates a lambda with a restricted whitelist of allowed slots. |
| [`xml2lambda`](/reference/slots/core/xml2lambda/) | Transforms XML into a lambda hierarchy. |
| [`yaml2json`](/reference/slots/core/yaml2json/) | Transforms YAML into JSON. |
| [`yaml2lambda`](/reference/slots/core/yaml2lambda/) | Transforms YAML into a lambda hierarchy. |
| [`yield`](/reference/slots/core/yield/) | Returns multiple child nodes or evaluated nodes to the caller. |

