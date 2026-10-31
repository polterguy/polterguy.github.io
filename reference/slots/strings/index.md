---
title: "strings.* slots"
description: "The 26 slots named strings.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

26 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`strings.builder`](/reference/slots/strings/strings.builder/) | Creates a string builder scope for [strings.builder.append]. |
| [`strings.builder.append`](/reference/slots/strings/strings.builder.append/) | Appends text to the current [strings.builder] scope. |
| [`strings.byte-count`](/reference/slots/strings/strings.byte-count/) | Returns the UTF-8 byte length of a string; useful for size checks where multi-byte characters matter. |
| [`strings.capitalize`](/reference/slots/strings/strings.capitalize/) | Returns the input with its first character upper-cased; remainder is left untouched. |
| [`strings.concat`](/reference/slots/strings/strings.concat/) | Concatenates strings. |
| [`strings.contains`](/reference/slots/strings/strings.contains/) | Returns true if a string contains the specified text. |
| [`strings.ends-with`](/reference/slots/strings/strings.ends-with/) | Returns true if a string ends with the specified text. |
| [`strings.html-decode`](/reference/slots/strings/strings.html-decode/) | HTML decodes the specified string. |
| [`strings.html-encode`](/reference/slots/strings/strings.html-encode/) | HTML encodes the specified string. |
| [`strings.join`](/reference/slots/strings/strings.join/) | Concatenates the values yielded by the expression, inserting the separator between adjacent items. |
| [`strings.length`](/reference/slots/strings/strings.length/) | Returns the length of a string. |
| [`strings.matches`](/reference/slots/strings/strings.matches/) | Returns regular expression matches, bounded by the execution deadline when set. |
| [`strings.mixin`](/reference/slots/strings/strings.mixin/) | Applies string interpolation from child expressions. |
| [`strings.regex-replace`](/reference/slots/strings/strings.regex-replace/) | Replaces text using a regular expression, bounded by the execution deadline when set. |
| [`strings.replace`](/reference/slots/strings/strings.replace/) | Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches. |
| [`strings.replace-not-of`](/reference/slots/strings/strings.replace-not-of/) | Replaces characters not found in the supplied allow-list. |
| [`strings.split`](/reference/slots/strings/strings.split/) | Splits a string at every occurrence of the separator and returns each segment as an unnamed child node. |
| [`strings.starts-with`](/reference/slots/strings/strings.starts-with/) | Returns true if a string starts with the specified text. |
| [`strings.substring`](/reference/slots/strings/strings.substring/) | Extracts a portion of a string starting at the given offset and optional length; out-of-range bounds throw. |
| [`strings.to-lower`](/reference/slots/strings/strings.to-lower/) | Transforms input text to lowercase. |
| [`strings.to-upper`](/reference/slots/strings/strings.to-upper/) | Transforms input text to uppercase. |
| [`strings.trim`](/reference/slots/strings/strings.trim/) | Trims characters from both ends of the specified string. |
| [`strings.trim-end`](/reference/slots/strings/strings.trim-end/) | Trims characters from the end of the specified string. |
| [`strings.trim-start`](/reference/slots/strings/strings.trim-start/) | Trims characters from the start of the specified string. |
| [`strings.url-decode`](/reference/slots/strings/strings.url-decode/) | URL decodes the specified string. |
| [`strings.url-encode`](/reference/slots/strings/strings.url-encode/) | URL encodes the specified string. |

