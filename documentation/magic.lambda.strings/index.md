
# Magic Lambda Strings

This project contains string manipulation slots for Magic. More specifically, it gives you the following slots.

* __[strings.replace]__ - Replaces occurrencies of the specified argument with the value of its specified argument
* __[strings.replace-not-of]__ - Replaces all characters found in string, except those found in its single argument
* __[strings.capitalize]__ - Turns the first character in your string into a CAPS
* __[strings.concat]__ - Concatenates two or more strings
* __[strings.contains]__ - Returns true if specified string contains the given argument
* __[strings.ends-with]__ - Returns true if the specified string ends with the specified argument
* __[strings.starts-with]__ - Returns true if the specified string starts with its argument
* __[strings.join]__ - Joins multiple strings together, with a separating character between each
* __[strings.length]__ - Returns the length in characters of the given string
* __[strings.regex-replace]__ - Replaces occurrencies matching the given regular expression with its argument
* __[strings.split]__ - Splits a string into multiple strings on every match of its given argument
* __[strings.to-lower]__ - Returns the lower caps version of its given argument
* __[strings.to-upper]__ - Returns the upper caps version of its specified argument
* __[strings.trim]__ - Trims a string, optionally for all characters found in its argument
* __[strings.trim-start]__ - Trims a string only to its left, optionally for all characters found in its argument
* __[strings.trim-end]__ - Trims a string only to its right, optionally for all characters found in its argument
* __[strings.url-encode]__ - URL encodes the specified string
* __[strings.substring]__ - Returns the sub-string of the specified string
* __[strings.matches]__ - Returns the regular expression matches found from specified source

## Usage

All the above slots that requires two arguments, will use the first argument as its _"what"_ argument, and the second
as its _"with"_ argument. Avoiding naming these though, allows you to reference other slots, and use these as sources
to parametrize your invocations to the above slots.

### [strings.replace]

This slot replaces occurrencies of a string inside a string, with some other string. The simplest version is like
follows.

```
.foo:thomas hansen
strings.replace:x:-
   .:hansen
   .:tjobing hansen
```

You can also reference slots and dynamic slots for that matter, assuming your slots somehow returns strings,
or something that can be converted into a string, such as the following illustrates. Notice, this code will
throw an exception, since there are probably no slots called _"some-slot-returning-string"_ in your installation.

```
.what:hansen
.foo:thomas hansen
strings.replace:x:-
   get-value:x:@.what
   signal:some-slot-returning-string
      arg1-to-slot:foo
      arg2-to-slot:foo
```

Above the first argument is _"what to look for"_, and the second argument is _"what to substitute it with"_.

The above is a general pattern for most of these slots, where the node arguments supplied to the slot will be
evaluated as a lambda object, before the arguments are consumed, allowing you to use arguments that are the
result of invoking other slots as arguments to your original outer most slot.

### [strings.replace-not-of]

This slot will replace every single character in your original string, that cannot be found in its first
argument, with the value of its second argument. This slot is useful if you want to remove all characters
that cannot be found in another character set, such as the following illustrates.

```
strings.replace-not-of:foo bar1howdy
   .:abcdefghijklmnopqrstuvwxyz
   .:-
```

The above will result in the following result 

```
strings.replace-not-of:foo-bar-howdy
```

### [strings.capitalize]

Turns the first character of your string into a CAPS character.

```
strings.capitalize:thomas

/*
 * Resulting in "Thomas" after invocation.
 */
```

### [strings.concat]

Concatenates a list of strings into one string. Similar to **[strings.join]**, except it doesn't take a
separating character.

```
.bar:Bar
strings.concat
   .:Thomas
   .:" "
   .:Hansen
   .:" "
   .:Foo
   .:" "
   get-value:x:@.bar

/*
 * Resulting in "Thomas Hansen Foo Bar" after invocation.
 */
```

### [strings.contains]

Returns true if the specified string contains some sequence of characters.

```
// Returns true
strings.contains:Thomas Hansen Is Cool
   .:Hansen
```

### [strings.ends-with]

Returns true if the specified string ends with some sequence of characters.

```
// Returns true
strings.ends-with:Thomas Hansen Is Cool
   .:Cool

// Returns false
strings.ends-with:Thomas Hansen Is Coolio
   .:Cool
```

### [strings.starts-with]

Returns true if the specified string starts with some sequence of characters.

```
// Returns true
strings.ends-with:Thomas Hansen Is Cool
   .:Thomas

// Returns false
strings.ends-with:Thomas Hansen Is Cool
   .:Hansen
```

### [strings.join]

Similar to **[strings.concat]**, except it also takes an optional separating character, allowing you to
concatenate a bunch of strings, and making sure each original string is separated by some sequence of strings.

```
.src
   .:foo
   .:bar
strings.join:x:@.src/*
   .:,

/*
 * Results in "foo,bar"
 */
```

### [strings.length]

Returns the length of a string as an integer number.

```
// Returns 6
strings.length:thomas
```

### [strings.regex-replace]

Replaces matches of the given regular expression with some static sequence of characters.

```
// Results in "FOO bar hansen"
strings.regex-replace:foo bar hansen
   .:fo+
   .:FOO
```

The first argument is what regular expression to match, the second argument is what to replace
all matches with.

### [strings.split]

Splits a string into multiple strings, where a sequence of characters can be found, removing the original
sequence of characters from the resulting node set.

```
.foo:some input string
strings.split:x:-
   .:' '
```

The above will result in the following result.

```
.foo:some input string
strings.split:x:-
   .:some
   .:input
   .:string
```

### [strings.to-lower]

Turns every single character in your input string into a lowercase character.

```
strings.to-lower:Thomas Hansen Is Cool

// Results in "thomas hansen is cool"
```

### [strings.to-upper]

Turns every single character in your input string into a UPPER case character.

```
strings.to-upper:Thomas Hansen Is Cool

// Results in "THOMAS HANSEN IS COOL"
```

### [strings.trim], [strings.trim-start], [strings.trim-end]

Trims a string, either both sides, only the start of it, or only the end of it, for
occurrencies of characters found in the sequence of characters provided as its argument.

```
strings.trim:09thomas12
   .:1234567890

// Results in "thomas"
```

### [strings.url-encode]

URL encodes a string. Example can be found below.

```
strings.url-encode:thomas@servergardens.com
```

Resulting in the following after execution.

```
strings.url-encode:thomas%40servergardens.com
```

### [strings.substring]

Returns a substring of the specified string.

```
.input:Foo Bar Howdy World
strings.substring:x:-
   .:5
   .:7
```

The above will result in the following.

```
strings.substring:ar Howd
```

Notice, the second argument is the _number of characters to return_ and not the offset into the string
of where to stop returning. In such a regard, it works the same way as the C# `Substring` method.

### [strings.matches]

Returns all regular expression matches from specified source string.

```
.input:Foo Bar Howdy World {match1} and {match2} and that was it
strings.matches:x:-
   .:"\\{.+?\\}"
```

The above will result in the following.

```
strings.matches
   .:{match1}
   .:{match2}
```

Notice, the second argument is the _number of characters to return_ and not the offset into the string
of where to stop returning. In such a regard, it works the same way as the C# `Substring` method.


## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.strings](https://github.com/polterguy/magic.lambda.strings), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.strings)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)
