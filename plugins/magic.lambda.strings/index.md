---
title: magic.lambda.strings
moved_anchors: {"how-to-use-stringsbuilder": "/reference/slots/strings/strings.builder/#guide", "how-to-use-stringsbuilderappend": "/reference/slots/strings/strings.builder.append/#guide", "how-to-use-stringsbyte-count": "/reference/slots/strings/strings.byte-count/#guide", "how-to-use-stringscapitalize": "/reference/slots/strings/strings.capitalize/#guide", "how-to-use-stringsconcat": "/reference/slots/strings/strings.concat/#guide", "how-to-use-stringscontains": "/reference/slots/strings/strings.contains/#guide", "how-to-use-stringsends-with": "/reference/slots/strings/strings.ends-with/#guide", "how-to-use-stringshtml-decode": "/reference/slots/strings/strings.html-decode/#guide", "how-to-use-stringshtml-encode": "/reference/slots/strings/strings.html-encode/#guide", "how-to-use-stringsjoin": "/reference/slots/strings/strings.join/#guide", "how-to-use-stringslength": "/reference/slots/strings/strings.length/#guide", "how-to-use-stringsmatches": "/reference/slots/strings/strings.matches/#guide", "how-to-use-stringsmixin": "/reference/slots/strings/strings.mixin/#guide", "how-to-use-stringsregex-replace": "/reference/slots/strings/strings.regex-replace/#guide", "how-to-use-stringsreplace": "/reference/slots/strings/strings.replace/#guide", "how-to-use-stringsreplace-not-of": "/reference/slots/strings/strings.replace-not-of/#guide", "how-to-use-stringssplit": "/reference/slots/strings/strings.split/#guide", "how-to-use-stringsstarts-with": "/reference/slots/strings/strings.starts-with/#guide", "how-to-use-stringssubstring": "/reference/slots/strings/strings.substring/#guide", "how-to-use-stringsto-lower": "/reference/slots/strings/strings.to-lower/#guide", "how-to-use-stringsto-upper": "/reference/slots/strings/strings.to-upper/#guide", "how-to-use-stringstrim-stringstrim-start-stringstrim-end": "/reference/slots/strings/strings.trim/#guide", "how-to-use-stringsurl-decode": "/reference/slots/strings/strings.url-decode/#guide", "how-to-use-stringsurl-encode": "/reference/slots/strings/strings.url-encode/#guide"}
---

This project contains string manipulation slots for Magic. More specifically, it gives you the following slots.

* __[\[strings.replace\]](/reference/slots/strings/strings.replace/)__ - Replaces occurrences of the specified argument with the value of its specified argument
* __[\[strings.replace-not-of\]](/reference/slots/strings/strings.replace-not-of/)__ - Replaces all characters found in string, except those found in its single argument
* __[\[strings.capitalize\]](/reference/slots/strings/strings.capitalize/)__ - Turns the first character in your string into a CAPS
* __[\[strings.concat\]](/reference/slots/strings/strings.concat/)__ - Concatenates two or more strings
* __[\[strings.contains\]](/reference/slots/strings/strings.contains/)__ - Returns true if specified string contains the given argument
* __[\[strings.ends-with\]](/reference/slots/strings/strings.ends-with/)__ - Returns true if the specified string ends with the specified argument
* __[\[strings.starts-with\]](/reference/slots/strings/strings.starts-with/)__ - Returns true if the specified string starts with its argument
* __[\[strings.join\]](/reference/slots/strings/strings.join/)__ - Joins multiple strings together, with a separating string between each string joined
* __[\[strings.length\]](/reference/slots/strings/strings.length/)__ - Returns the length in characters of the given string
* __[\[strings.byte-count\]](/reference/slots/strings/strings.byte-count/)__ - Returns the UTF-8 byte length of the given string
* __[\[strings.regex-replace\]](/reference/slots/strings/strings.regex-replace/)__ - Replaces occurrences matching the given regular expression with its argument
* __[\[strings.split\]](/reference/slots/strings/strings.split/)__ - Splits a string into multiple strings on every match of its given argument
* __[\[strings.to-lower\]](/reference/slots/strings/strings.to-lower/)__ - Returns the lower caps version of its given argument
* __[\[strings.to-upper\]](/reference/slots/strings/strings.to-upper/)__ - Returns the upper caps version of its specified argument
* __[\[strings.trim\]](/reference/slots/strings/strings.trim/)__ - Trims a string, optionally for all characters found in its argument
* __[\[strings.trim-start\]](/reference/slots/strings/strings.trim-start/)__ - Trims a string only to its left, optionally for all characters found in its argument
* __[\[strings.trim-end\]](/reference/slots/strings/strings.trim-end/)__ - Trims a string only to its right, optionally for all characters found in its argument
* __[\[strings.url-encode\]](/reference/slots/strings/strings.url-encode/)__ - URL encodes the specified string
* __[\[strings.url-decode\]](/reference/slots/strings/strings.url-decode/)__ - URL decodes the specified string
* __[\[strings.html-encode\]](/reference/slots/strings/strings.html-encode/)__ - HTML encodes the specified string
* __[\[strings.html-decode\]](/reference/slots/strings/strings.html-decode/)__ - HTML decodes the specified string
* __[\[strings.substring\]](/reference/slots/strings/strings.substring/)__ - Returns the sub-string of the specified string
* __[\[strings.matches\]](/reference/slots/strings/strings.matches/)__ - Returns the regular expression matches found from specified source
* __[\[strings.mixin\]](/reference/slots/strings/strings.mixin/)__ - Allows for mixin logic of strings and Hyperlambda
* __[\[strings.builder\]](/reference/slots/strings/strings.builder/)__ - Creates a string builder scope for **[strings.builder.append]**
* __[\[strings.builder.append\]](/reference/slots/strings/strings.builder.append/)__ - Appends text to the current **[strings.builder]** scope


## Usage

All the above slots that require two arguments, will use the first argument as its _"what"_ argument, and the second
as its _"with"_ argument. Avoiding naming these though, allows you to reference other slots, and use these as sources
to parametrize your invocations to the above slots. Below is an example of how this would look like.

```
.data:Hyperlambda is cool

strings.replace:x:-
   .:cool
   .:super cool
```
