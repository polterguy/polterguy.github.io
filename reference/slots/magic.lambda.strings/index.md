---
title: magic.lambda.strings slot reference
description: Every slot in magic.lambda.strings with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.strings](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.strings). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.strings](/plugins/magic.lambda.strings/)._

## [strings.builder]

Creates a string builder scope for [strings.builder.append].

* **Returns**: Resolves to the text appended inside the builder scope

| Argument | Type | Required | Description |
|---|---|---|---|
| `[*]` | lambda | no | Executable child slot evaluated while the StringBuilder is scoped; use [strings.builder.append] to append text |

Guide: [How to use [strings.builder]](/plugins/magic.lambda.strings/#how-to-use-stringsbuilder)

## [strings.builder.append]

Appends text to the current [strings.builder] scope.

* **Value** (`text`), required: Text to append to the current [strings.builder] scope

Guide: [How to use [strings.builder.append]](/plugins/magic.lambda.strings/#how-to-use-stringsbuilderappend)

## [strings.byte-count]

Returns the UTF-8 byte length of a string; useful for size checks where multi-byte characters matter.

* **Value** (`text`), required: Text to measure
* **Returns**: Resolves to the number of bytes in the string

Guide: [How to use [strings.byte-count]](/plugins/magic.lambda.strings/#how-to-use-stringsbyte-count)

## [strings.capitalize]

Returns the input with its first character upper-cased; remainder is left untouched.

* **Value** (`text`), required: Text to capitalize
* **Returns**: Resolves to the capitalized string

Guide: [How to use [strings.capitalize]](/plugins/magic.lambda.strings/#how-to-use-stringscapitalize)

## [strings.concat]

Concatenates strings.

* **Value** (`string-list`), optional: Expression yielding the text segments to concatenate when not supplied as child nodes
* **Returns**: Resolves to the concatenated string

Guide: [How to use [strings.concat]](/plugins/magic.lambda.strings/#how-to-use-stringsconcat)

## [strings.contains]

Returns true if a string contains the specified text.

* **Value** (`text`), required: Text to search
* **Returns**: Returns true if the string contains the supplied text

Guide: [How to use [strings.contains]](/plugins/magic.lambda.strings/#how-to-use-stringscontains)

## [strings.ends-with]

Returns true if a string ends with the specified text.

* **Value** (`text`), required: Text to inspect
* **Returns**: Returns true if the string ends with the supplied text

Guide: [How to use [strings.ends-with]](/plugins/magic.lambda.strings/#how-to-use-stringsends-with)

## [strings.html-decode]

HTML decodes the specified string.

* **Value** (`html-encoded`), required: HTML encoded text to decode
* **Returns**: Resolves to the decoded HTML markup

Guide: [How to use [strings.html-decode]](/plugins/magic.lambda.strings/#how-to-use-stringshtml-decode)

## [strings.html-encode]

HTML encodes the specified string.

* **Value** (`html-unencoded,text`), required: Non-encoded HTML text to encode
* **Returns**: Resolves to the HTML-encoded string

Guide: [How to use [strings.html-encode]](/plugins/magic.lambda.strings/#how-to-use-stringshtml-encode)

## [strings.join]

Concatenates the values yielded by the expression, inserting the separator between adjacent items.

* **Value** (`string-list`), required: Expression yielding the values to join
* **Returns**: Resolves to the joined string

Guide: [How to use [strings.join]](/plugins/magic.lambda.strings/#how-to-use-stringsjoin)

## [strings.length]

Returns the length of a string.

* **Value** (`text`), required: Text to measure
* **Returns**: Resolves to the number of characters in the string

Guide: [How to use [strings.length]](/plugins/magic.lambda.strings/#how-to-use-stringslength)

## [strings.matches]

Returns regular expression matches, bounded by the execution deadline when set.

* **Value** (`text`), required: Text to match against the regular expression
* **Returns**: Returns one child node per regular expression match

Guide: [How to use [strings.matches]](/plugins/magic.lambda.strings/#how-to-use-stringsmatches)

## [strings.mixin]

Applies string interpolation from child expressions.

* **Value** (`mixin-template,text`), required: Template text to interpolate
* **Returns**: Resolves to the rendered string after applying codebehind and expressions

| Argument | Type | Required | Description |
|---|---|---|---|
| `[strip]` | bool | no | Whether to strip embedded Hyperlambda instead of executing it |
| `[*]` | string | no | Argument passed to embedded Hyperlambda snippets invoked from the template |

Guide: [How to use [strings.mixin]](/plugins/magic.lambda.strings/#how-to-use-stringsmixin)

## [strings.regex-replace]

Replaces text using a regular expression, bounded by the execution deadline when set.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after applying the regular-expression replacement

Guide: [How to use [strings.regex-replace]](/plugins/magic.lambda.strings/#how-to-use-stringsregex-replace)

## [strings.replace]

Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after replacing the specified substring

Guide: [How to use [strings.replace]](/plugins/magic.lambda.strings/#how-to-use-stringsreplace)

## [strings.replace-not-of]

Replaces characters not found in the supplied allow-list.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after replacing characters not found in the allowed set

Guide: [How to use [strings.replace-not-of]](/plugins/magic.lambda.strings/#how-to-use-stringsreplace-not-of)

## [strings.split]

Splits a string at every occurrence of the separator and returns each segment as an unnamed child node.

* **Value** (`text`), required: Text to split
* **Returns**: Returns one child node per split string item

Guide: [How to use [strings.split]](/plugins/magic.lambda.strings/#how-to-use-stringssplit)

## [strings.starts-with]

Returns true if a string starts with the specified text.

* **Value** (`text`), required: Text to inspect
* **Returns**: Returns true if the string starts with the supplied text

Guide: [How to use [strings.starts-with]](/plugins/magic.lambda.strings/#how-to-use-stringsstarts-with)

## [strings.substring]

Extracts a portion of a string starting at the given offset and optional length; out-of-range bounds throw.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the extracted substring

Guide: [How to use [strings.substring]](/plugins/magic.lambda.strings/#how-to-use-stringssubstring)

## [strings.to-lower]

Transforms input text to lowercase.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the lowercased string

Guide: [How to use [strings.to-lower]](/plugins/magic.lambda.strings/#how-to-use-stringsto-lower)

## [strings.to-upper]

Transforms input text to uppercase.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the uppercased string

Guide: [How to use [strings.to-upper]](/plugins/magic.lambda.strings/#how-to-use-stringsto-upper)

## [strings.trim]

Trims characters from both ends of the specified string.

* **Value** (`text`), required: Text to trim
* **Returns**: Resolves to the trimmed string

Guide: [How to use [strings.trim]](/plugins/magic.lambda.strings/#how-to-use-stringstrim-stringstrim-start-stringstrim-end)

## [strings.trim-end]

Trims characters from the end of the specified string.

* **Value** (`text`), required: Text to trim
* **Returns**: Resolves to the string with trailing characters removed

Guide: [How to use [strings.trim-end]](/plugins/magic.lambda.strings/#how-to-use-stringstrim-stringstrim-start-stringstrim-end)

## [strings.trim-start]

Trims characters from the start of the specified string.

* **Value** (`text`), required: Text to trim
* **Returns**: Resolves to the string with leading characters removed

Guide: [How to use [strings.trim-start]](/plugins/magic.lambda.strings/#how-to-use-stringstrim-stringstrim-start-stringstrim-end)

## [strings.url-decode]

URL decodes the specified string.

* **Value** (`url-encoded`), required: Text to decode
* **Returns**: Resolves to the URL-decoded string

Guide: [How to use [strings.url-decode]](/plugins/magic.lambda.strings/#how-to-use-stringsurl-decode)

## [strings.url-encode]

URL encodes the specified string.

* **Value** (`url-component,text`), required: Text to encode
* **Returns**: Resolves to the URL-encoded string

Guide: [How to use [strings.url-encode]](/plugins/magic.lambda.strings/#how-to-use-stringsurl-encode)

