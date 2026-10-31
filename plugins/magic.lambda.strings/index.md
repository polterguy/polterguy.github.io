---
title: magic.lambda.strings
moved_anchors: {"how-to-use-stringsbuilder": "/plugins/magic.lambda.strings/strings.builder/", "how-to-use-stringsbuilderappend": "/plugins/magic.lambda.strings/strings.builder.append/", "how-to-use-stringsbyte-count": "/plugins/magic.lambda.strings/strings.byte-count/", "how-to-use-stringscapitalize": "/plugins/magic.lambda.strings/strings.capitalize/", "how-to-use-stringsconcat": "/plugins/magic.lambda.strings/strings.concat/", "how-to-use-stringscontains": "/plugins/magic.lambda.strings/strings.contains/", "how-to-use-stringsends-with": "/plugins/magic.lambda.strings/strings.ends-with/", "how-to-use-stringshtml-decode": "/plugins/magic.lambda.strings/strings.html-decode/", "how-to-use-stringshtml-encode": "/plugins/magic.lambda.strings/strings.html-encode/", "how-to-use-stringsjoin": "/plugins/magic.lambda.strings/strings.join/", "how-to-use-stringslength": "/plugins/magic.lambda.strings/strings.length/", "how-to-use-stringsmatches": "/plugins/magic.lambda.strings/strings.matches/", "how-to-use-stringsmixin": "/plugins/magic.lambda.strings/strings.mixin/", "how-to-use-stringsregex-replace": "/plugins/magic.lambda.strings/strings.regex-replace/", "how-to-use-stringsreplace": "/plugins/magic.lambda.strings/strings.replace/", "how-to-use-stringsreplace-not-of": "/plugins/magic.lambda.strings/strings.replace-not-of/", "how-to-use-stringssplit": "/plugins/magic.lambda.strings/strings.split/", "how-to-use-stringsstarts-with": "/plugins/magic.lambda.strings/strings.starts-with/", "how-to-use-stringssubstring": "/plugins/magic.lambda.strings/strings.substring/", "how-to-use-stringsto-lower": "/plugins/magic.lambda.strings/strings.to-lower/", "how-to-use-stringsto-upper": "/plugins/magic.lambda.strings/strings.to-upper/", "how-to-use-stringstrim-stringstrim-start-stringstrim-end": "/plugins/magic.lambda.strings/strings.trim/", "how-to-use-stringsurl-decode": "/plugins/magic.lambda.strings/strings.url-decode/", "how-to-use-stringsurl-encode": "/plugins/magic.lambda.strings/strings.url-encode/"}
---

This project contains string manipulation slots for Magic. More specifically, it gives you the following slots.

* __[\[strings.replace\]](/plugins/magic.lambda.strings/strings.replace/)__ - Replaces occurrences of the specified argument with the value of its specified argument
* __[\[strings.replace-not-of\]](/plugins/magic.lambda.strings/strings.replace-not-of/)__ - Replaces all characters found in string, except those found in its single argument
* __[\[strings.capitalize\]](/plugins/magic.lambda.strings/strings.capitalize/)__ - Turns the first character in your string into a CAPS
* __[\[strings.concat\]](/plugins/magic.lambda.strings/strings.concat/)__ - Concatenates two or more strings
* __[\[strings.contains\]](/plugins/magic.lambda.strings/strings.contains/)__ - Returns true if specified string contains the given argument
* __[\[strings.ends-with\]](/plugins/magic.lambda.strings/strings.ends-with/)__ - Returns true if the specified string ends with the specified argument
* __[\[strings.starts-with\]](/plugins/magic.lambda.strings/strings.starts-with/)__ - Returns true if the specified string starts with its argument
* __[\[strings.join\]](/plugins/magic.lambda.strings/strings.join/)__ - Joins multiple strings together, with a separating string between each string joined
* __[\[strings.length\]](/plugins/magic.lambda.strings/strings.length/)__ - Returns the length in characters of the given string
* __[\[strings.byte-count\]](/plugins/magic.lambda.strings/strings.byte-count/)__ - Returns the UTF-8 byte length of the given string
* __[\[strings.regex-replace\]](/plugins/magic.lambda.strings/strings.regex-replace/)__ - Replaces occurrences matching the given regular expression with its argument
* __[\[strings.split\]](/plugins/magic.lambda.strings/strings.split/)__ - Splits a string into multiple strings on every match of its given argument
* __[\[strings.to-lower\]](/plugins/magic.lambda.strings/strings.to-lower/)__ - Returns the lower caps version of its given argument
* __[\[strings.to-upper\]](/plugins/magic.lambda.strings/strings.to-upper/)__ - Returns the upper caps version of its specified argument
* __[\[strings.trim\]](/plugins/magic.lambda.strings/strings.trim/)__ - Trims a string, optionally for all characters found in its argument
* __[\[strings.trim-start\]](/plugins/magic.lambda.strings/strings.trim/)__ - Trims a string only to its left, optionally for all characters found in its argument
* __[\[strings.trim-end\]](/plugins/magic.lambda.strings/strings.trim/)__ - Trims a string only to its right, optionally for all characters found in its argument
* __[\[strings.url-encode\]](/plugins/magic.lambda.strings/strings.url-encode/)__ - URL encodes the specified string
* __[\[strings.url-decode\]](/plugins/magic.lambda.strings/strings.url-decode/)__ - URL decodes the specified string
* __[\[strings.html-encode\]](/plugins/magic.lambda.strings/strings.html-encode/)__ - HTML encodes the specified string
* __[\[strings.html-decode\]](/plugins/magic.lambda.strings/strings.html-decode/)__ - HTML decodes the specified string
* __[\[strings.substring\]](/plugins/magic.lambda.strings/strings.substring/)__ - Returns the sub-string of the specified string
* __[\[strings.matches\]](/plugins/magic.lambda.strings/strings.matches/)__ - Returns the regular expression matches found from specified source
* __[\[strings.mixin\]](/plugins/magic.lambda.strings/strings.mixin/)__ - Allows for mixin logic of strings and Hyperlambda
* __[\[strings.builder\]](/plugins/magic.lambda.strings/strings.builder/)__ - Creates a string builder scope for **[strings.builder.append]**
* __[\[strings.builder.append\]](/plugins/magic.lambda.strings/strings.builder.append/)__ - Appends text to the current **[strings.builder]** scope


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
